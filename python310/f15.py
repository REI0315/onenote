import hashlib
import os
import re
import shutil
import stat
import time
import traceback
from pathlib import Path
from threading import Thread

import git
from PySide6.QtCore import QRect, QObject, Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QComboBox, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox

from auto_config import AutoConfig
from config import Config
from model import project
from model.plugins import Plugins
from model.project import Project
from roading import Roading
from ui.getcode_ui import Ui_getcode
from util.get_project_msg import Project_Msg


class MySignals(QObject):
    plugins_update = Signal()
    branch_dialog = Signal(str, str, str, str)
    no_file_dialog = Signal(str, object)
    all_task_finish = Signal(object)
    # branch_update_singal = Signal()
    # task_end_singal = Signal()


def get_size(path):
    return str(os.path.getsize(path))


def get_sha1(path):
    with open(path, "rb", encoding='utf-8') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        return sha1obj.hexdigest()


def get_meta_data(path):
    path = str(path)
    return {
        'size': get_size(path),
        'sha1': get_sha1(path)
    }


class CodeWindow(QMainWindow):

    def __init__(self, project):
        super(CodeWindow, self).__init__()
        self.project = project
        self.ui = Ui_getcode()  # UI类的实例化()
        self.ui.setupUi(self)
        self.signals = MySignals()
        self.plugins_task_status = {}
        self.config_window = None
        self.project_path = ''
        self.plugins_fail = []

        self.band()

    def band(self):
        self.setWindowTitle('拉取项目及其插件')
        # 绑定路径
        self.ui.pushButton_2.clicked.connect(self.select_paht)
        # self.ui.pushButton_2.changeEvent.connect(self.project_path_change)
        # 下载项目
        self.ui.pushButton_3.clicked.connect(self.down_project)
        # 下载插件
        self.ui.pushButton.clicked.connect(self.down_plugins)

        # 所有任务完成时出现该弹窗
        self.signals.all_task_finish.connect(self.all_task_finish)
        self.signals.plugins_update.connect(self.plugins_update)
        self.signals.branch_dialog.connect(self.branch_dialog)
        self.ui.label.setText(self.project.name)
        for branch in self.project.branch:
            self.ui.comboBox.addItem(branch)
        self.project.now_branch = self.ui.comboBox.currentText()
        self.ui.comboBox.currentTextChanged.connect(self.select_branch)
        self.signals.no_file_dialog.connect(self.no_file_dialog)
        # 进入页面时 不能被点击
        self.ui.pushButton.setEnabled(False)
        # 如果没有分支，则拉取项目按钮不能点击
        if not self.project.branch:
            self.ui.pushButton_3.setEnabled(False)
        # self.project.plugins =
        self.all_plugins = Project_Msg().plugins.copy()
        for v, plug in enumerate(self.all_plugins, start=1):
            label = QLabel(self)
            label.setObjectName(u"label")
            label.setGeometry(QRect(30, (v + 4) * 30, 251, 61))
            text = '' + plug.name if plug.has_permission else '【无权限】 ' + plug.name
            label.setText(text)
            comboBox = QComboBox(self)
            comboBox.setObjectName(u"comboBox")
            comboBox.setGeometry(QRect(210, ((v + 4) * 30) + 20, 280, 20))
            for branch in plug.branch:
                comboBox.addItem(branch)
            comboBox.addItem('不拉取该插件')
            plug.set_comboBox(comboBox, label)
            comboBox.setEnabled(False)

    # def project_path_change(self):
    #     try:
    #         self.ui.label_3.setText(Path(self.ui.lineEdit.text()).joinpath(self.project.name))
    #     except Exception as e :
    #         pass

    def all_task_finish(self, plugins_fail):
        if not plugins_fail:
            self.dia.close_window()
            choice = QMessageBox.question(self, '任务完成',
                                          '所有插件都拉取完毕,是否进行后续配置操作',
                                          )
        else:
            time.sleep(1)
            self.dia.close_window()
            pf = ','.join(plugins_fail)
            choice = QMessageBox.question(self, '任务完成',
                                          f'{pf}未拉取,因为插件目录已存在文件.其他插件拉取完毕,是否进行后续配置操作',
                                          )
        if choice == QMessageBox.Yes:
            window = AutoConfig(self.project_path, self.project)  # 实例化主窗口
            self.config_window = window
            window.show_window()  # 展示主窗口
            window.setWindowTitle('自动配置后续步骤')
        elif choice == QMessageBox.No:
            pass
        # QMessageBox.information(self, '任务成功！',
        #                     '任务成功！')

    def no_file_dialog(self, path, obj):
        # self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.dia.set_task_msg(path+f'目录已存在文件！故此项目无法拉取{str(obj.name)}')
        # qmb = QMessageBox.warning(self, '目录已存在文件！', path + '目录已存在文件！且不是一个git仓库\n' + '故此项目无法拉取')
        # qmb.setWindowFlags(Qt.WindowStaysOnTopHint)
        if isinstance(obj, Project):
            QMessageBox.warning(self, '目录已存在文件！',
                                path + f'目录已存在文件！且不是该项目{obj.name}的git仓库\n' + '故此项目无法拉取')
        elif isinstance(obj, Plugins):
            self.plugins_task_status[obj.name] = True
            if obj.name not in self.plugins_fail:
                self.plugins_fail.append(obj.name)

        # self.dia.close_window()

    def plugins_update(self):
        self.dia.close_window()
        # 此处项目已经拉取成功，可以显示下载插件按钮
        self.ui.pushButton.setEnabled(True)
        cspath = Path(self.project_path).joinpath('Source').joinpath(self.project.name).joinpath(
            self.project.name + ".Build.cs")
        plugins = self.get_relyon_plugins(cspath)
        for p in plugins:
            for pm in self.all_plugins:
                print(p, pm.name)
                if p == pm.name:
                    if pm.name != 'Puerts':
                        self.project.plugins.append(pm)
                        print('识别到一个依赖插件', pm.name)
        # 此处加入一些固定插件
        for pm in self.all_plugins:
            if pm.name == 'v8' or pm.name == 'UEPuerts' or pm.name == 'UEReactUMG' or pm.name == 'VKBCommon':
                self.project.plugins.append(pm)
                print('增加固定依赖插件', pm.name)

        self.ui.label_2.setVisible(False)
        for plug in self.project.plugins:
            plug.comboBox.setEnabled(True)

        for noplug in self.all_plugins:
            if not noplug in self.project.plugins:
                noplug.comboBox.setVisible(False)
                noplug.label.setVisible(False)

    def select_branch(self):
        self.project.now_branch = self.ui.comboBox.currentText()

    def select_paht(self):
        file_path = QFileDialog.getExistingDirectory(self, '项目')
        self.ui.lineEdit.setText(file_path)
        print(file_path)

    def down_project(self):
        # 点击下载项目时，给 project 赋值
        self.project_path = self.ui.lineEdit.text()
        if self.project_path == '':
            QMessageBox.warning(self, '没有选择项目目录',
                                '没有选择项目目录')
            return
        else:
            try:
                repo = git.Repo(self.project_path)
            except Exception as e:
                self.project_path = str(Path(self.project_path).joinpath(self.project.name))
                self.ui.label_3.setText("您拉取的项目最终将生成在：" + self.project_path)
                self.down_project2()
            else:
                res = repo.git.remote('-v')
                res = res.split()
                print(res[1])
                print(self.project.http_url)
                if res[1] == self.project.http_url:
                    self.ui.label_3.setText("您拉取的项目最终将生成在：" + self.project_path)
                    self.down_project2()
                else:
                    self.signals.no_file_dialog.emit(self.project_path, self.project)
                    return

    def down_project2(self):
        if Path(self.project_path).exists():
            choice = QMessageBox.question(self, '识别到本地存在该项目目录',
                                          '确定要将项目文件拉取到' + self.project_path + "吗？\n这将使用该目录同步远程代码"
                                          )
            if choice == QMessageBox.Yes:
                pass
            elif choice == QMessageBox.No:
                return

        self.down_file_for_git(self.project_path, self.project.now_branch, self.project.http_url, self.project)
        self.show_dialog('正在拉取项目...')
        for v, plug in enumerate(self.all_plugins, start=1):
            plug.comboBox.setVisible(True)
            plug.label.setVisible(True)
            plug.comboBox.setEnabled(False)
            plug.comboBox.setEnabled(False)

    def down_plugins(self):
        """下载插件"""
        self.plugins_fail = []
        tast_plugins = set(self.project.plugins)
        for p in tast_plugins:
            if not p.now_branch == '不拉取该插件':
                print('开始下载插件', p.name, p.now_branch, p.http_url, p.has_permission)
                # 该插件是否有权限
                if p.has_permission:
                    path_ = self.project_path.strip('/').strip('\\') + '\Plugins\\' + str(p.name)
                    # print(path_)
                    if not p.name == 'v8':
                        self.down_file_for_git(path_, p.now_branch, p.http_url, p)
                else:
                    self.down_file_for_minio(self.project_path.strip('/').strip('\\') + '\Plugins\\' + str(p.name),
                                             str(Path(p.name).joinpath(p.now_branch).joinpath(p.name)).replace('\\',
                                                                                                               '/'),
                                             p)
                # 设置任务开始标记
                self.plugins_task_status[p.name] = False
            else:
                pass
        # 设置wile循环，验证各个任务是否OK
        self.show_dialog('正在拉取各个插件...')

        # time.sleep(1)
        def innerFunc():
            v8flag = True
            while True:
                flag = True
                for key in self.plugins_task_status:
                    print('检查插件拉取状态', key, ':', self.plugins_task_status[key])
                    if self.plugins_task_status[key] == False:
                        flag = False
                    if self.plugins_task_status.get('Puerts') != False and self.plugins_task_status.get(
                            'UEPuerts') != False:
                        if v8flag:
                            # 开始拉取V8
                            for p in tast_plugins:
                                if p.name == 'v8' and p.now_branch != '不拉取该插件':
                                    # joinpath('Puerts').joinpath('ThirdParty').joinpath('v8')
                                    v8path = self.project_path.strip('/').strip(
                                        '\\') + '\Plugins\\' + 'Puerts\\' + 'ThirdParty\\' + str(p.name)
                                    self.down_file_for_git(v8path, p.now_branch, p.http_url, p)
                            v8flag = False
                if flag == True:
                    # 结束弹窗
                    self.signals.all_task_finish.emit(self.plugins_fail)
                    break
                time.sleep(1)

        thr = Thread(target=innerFunc)
        thr.start()

    def show_dialog(self, text):
        self.dia = Roading()
        self.dia.setText(text)
        self.dia.show_window()

    def branch_dialog(self, title, msg, path, branch):
        self.dia.close_window()

        choice = QMessageBox.question(self, title,
                                      msg,
                                      )
        if choice == QMessageBox.Yes:
            choice = QMessageBox.question(self, title, '请确认要丢弃修改吗（推荐先提交或者暂存修改）')
            if choice == QMessageBox.Yes:
                self.dia.show()
                self.hard_reset(path, branch)
                self.dia.close_window()
            if choice == QMessageBox.No:
                pass
        elif choice == QMessageBox.No:
            pass

    def down_file_for_git(self, path, branch, http_url, obj):
        """
        给一个路径，通过git下载文件
        :param path:  绝对路径，代表git项目的本地路径，   可能路径是不存在的，这时需要新建仓库，如果存在，则直接拉
        :param branch: 分支名字
        :param http_url: 项目的远端clone地址
        :return:
        """

        # self.show_dialog('正在拉取项目文件...')
        # time.sleep(1)
        # self.dia.close_window()

        # def qmb():
        #     QMessageBox.warning(self, '目录已存在文件！', self.project_path+'目录已存在文件！且不是一个git仓库\n'+'项目路径最终应指向一个空文件夹或者git仓库')

        # if obj.name == 'v8':
        #     path = Path(path).parent.joinpath('Puerts').joinpath('ThirdParty').joinpath('v8')
        #     while not path.exists():
        #         time.sleep(0.5)
        def clone_code():
            # 本地地址无仓库，克隆代码
            try:
                git.Repo.init(path=path)
                _path = os.path.join(path, '.git')
                shutil.rmtree(_path, onerror=self.delete)
                new_repo = git.Repo.clone_from(http_url, to_path=path, branch=branch)
                print('本地地址无仓库，克隆代码')
            except Exception as e:
                # self.dia.close_window()
                if isinstance(obj, Project):
                    self.dia.close_window()
                    self.signals.no_file_dialog.emit(str(path), obj)
                # self.dia.close_window()
                else:
                    self.signals.no_file_dialog.emit(str(path), obj)
                print(e)
                raise Exception

        def checkout_or_pull(repo):
            # 存在目录,切换分支拉取代码
            try:
                # repo = git.Repo(path)
                # repo.git.config("--global", "--add", "safe.directory", "'*'")
                repo.git.fetch("--all")
                repo.git.checkout(f"{branch}")
                repo.git.pull()
            except Exception as e:
                print('要操作的git路径为：', path)
                if e.__str__().__contains__(
                        'Your local changes to the following files would be overwritten by checkout'):
                    print('path', type(path))
                    self.signals.branch_dialog.emit('警告！', '检测到您在本地分支有修改，若切换该分支会丢弃本地修改',
                                                    str(path), branch)
                elif e.__str__().__contains__(
                        'Your local changes to the following files would be overwritten by merge'):
                    self.signals.branch_dialog.emit('警告！',
                                                    '检测到您本地修改和远程库有冲突，若继续拉取将丢弃本地修改',
                                                    str(path), branch)
                else:
                    raise e

        def innerFunc():
            try:
                # print()
                # if look_git:
                #     while not self.plugins_task_status[look_git]:
                #         print('等待git拉取结束',str(look_git))
                #         time.sleep(1)
                print('开始拉取插件', path)
                if not os.path.exists(path):
                    os.makedirs(path, mode=0o777, exist_ok=False)
                    clone_code()
                else:
                    try:
                        repo = git.Repo(path)
                    except Exception as e:
                        # print('出现了',str(e),'异常')
                        traceback.print_exc()
                        print('尝试使用其他办法拉取')
                        # shutil.rmtree(path, onerror=self.delete)
                        # os.makedirs(path, mode=0o777, exist_ok=False)
                        clone_code()
                    else:
                        checkout_or_pull(repo)


            except Exception as e:
                # self.dia.close_window()
                print("线程异常：", e)
            else:
                # cs文件的路径生成
                if isinstance(obj, project.Project):
                    # self.dia.set_task_msg(obj.name + '项目代码已拉取完成')
                    self.signals.plugins_update.emit()
                else:
                    # self.dia.set_task_msg(obj.name+'插件代码已拉取完成')
                    self.plugins_task_status[obj.name] = True

        path = Path(path)
        if obj.name == 'UEPuerts':
            path = path.parent.joinpath('Puerts')
        if obj.name == 'UEReactUMG':
            path = path.parent.joinpath('ReactUMG')
        # look_git = None
        # if obj.name == 'v8':
        #     # 需要等到UEPuerts下载完毕
        #     look_git = 'UEPuerts'
        #     path = path.parent.joinpath('Puerts').joinpath('ThirdParty').joinpath('v8')

        thr = Thread(target=innerFunc)
        thr.start()

    def hard_reset(self, path, branch):
        """
        强制切分支
        :return:
        """
        try:
            print('开始强制切分支:', path, " b=", branch)
            repo = git.Repo(path)
            repo.git.reset("--hard", f"origin/{branch}")
            repo.git.checkout(f"{branch}")
        except Exception as e:
            raise e

    def get_relyon_plugins(self, file_path):
        """
            D:\projcets\vkplivebroadcast\Source\VKPLiveBroadcast\VKPLiveBroadcast.Build.cs
        :param file_path: 根据一个文件路径，识别该项目的所有依赖
        :return:
        """
        file_path = Path(file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            txt = f.read()
            txt = txt.replace(' ', '').replace('	', '')
            a = txt.index('PublicDependencyModuleNames.AddRange(newstring[]')
            print('$$$$$', txt[a + 49:-1])
            # 获得插件列表
            expand_result = []
            for exname in txt[a + 49:-1].split('\n'):
                # print('@@',exname)
                if exname == '});':
                    break
                elif '//' in exname:
                    continue
                else:
                    for exname_extract in exname.split(','):
                        if exname_extract != '':
                            expand_result.append(exname_extract.replace('"', ''))
                        print(exname_extract)
            return expand_result

    def delete(self, func, path, execinfo):
        os.chmod(path, stat.S_IWUSR)
        func(path)

    def down_file_for_minio(self, path, minio_path, obj):
        """
        将 minio上这个路径下全部的文件，都下载到本地 path绝对路径下， 要校验sha1值
        :param path: 本地绝对路径  xxxproject/plugins/VKBCommon 这样，本地可能不存在该路径
        :param minio_path: minio上的路径  vkb-plugins/VKBCommon/test_vesion_0.1/VKBCommon
        :return:
        """
        p = Path(path)
        print("minio_path:", minio_path)
        minio_path = minio_path + "/"

        def innerFunc():
            try:
                def list_objects(prefix=minio_path):
                    for f in Config().client.list_objects(Config().BUCKET_NAME, prefix=prefix, use_api_v1=True):
                        print("object_name:", f.object_name)
                        if f.is_dir:
                            list_objects(f.object_name)
                        else:
                            f = Config().client.stat_object(Config().BUCKET_NAME, f.object_name)
                            # todo 暂时没有元数据
                            _data = {
                                'size': f.metadata['x-amz-meta-size'],
                                'sha1': f.metadata['x-amz-meta-sha1']
                            }
                            p1 = f.object_name.split(minio_path)[1]
                            # print('wenjian', p1)
                            file_path = p.joinpath(p1)
                            # print(file_path)
                            if file_path.exists():
                                f_date = {
                                    'size': get_size(file_path),
                                    'sha1': get_sha1(file_path)
                                }
                                if f_date == _data:
                                    continue
                            Config().client.fget_object(Config().BUCKET_NAME, f.object_name, str(file_path))

                list_objects()
            except Exception as e:
                print(e)
            finally:
                print('走到这里了')
                self.plugins_task_status[obj.name] = True

        thr = Thread(target=innerFunc)
        thr.start()

