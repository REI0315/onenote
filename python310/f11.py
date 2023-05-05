import configparser
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import winreg
from CONFIG import CONFIG

from pathlib import Path, WindowsPath
from threading import Thread


def zip_shell(cmds):
    shell = ""
    for cmd in cmds:
        shell += cmd + "&"
    print(shell[:-1])

    return shell[:-1]


def shell(cmds):
    res = subprocess.Popen(
        zip_shell(cmds), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    return res.stdout.read().decode("gbk"), res.stderr.read().decode("gbk")


def check_npm():
    # self.ui.label.setText(self.ui.label.text() + '--------->【正在配置】')

    cmds = ['where npm']
    res = shell(cmds)
    print(res)
    npm_path = res[0].replace('\r', '').split('\n')
    print(npm_path)
    if npm_path[0]:
        # 有npm
        return True
    else:
        raise Exception


def check_tsc():
    # self.ui.label_2.setText(self.ui.label_2.text() + '--------->【正在配置】')
    cmds = ['tsc -v']
    res = shell(cmds)

    tsc_value = res[0]
    if 'Version' in tsc_value:
        return True
    else:
        raise Exception


def excute_js(prject_path):
    # self.ui.label_3.setText(self.ui.label_3.text() + '--------->【正在配置】')
    if isinstance(prject_path, WindowsPath):
        prject_path = str(prject_path)
    puerts_path = Path(prject_path).joinpath('Plugins').joinpath('Puerts')
    cmds = ['cd ' + str(puerts_path), prject_path[0] + ':', 'node enable_puerts_module.js']
    p = Path(prject_path).joinpath('tsconfig.json')
    if p.exists():  # 如果存在， 则只需要执行命令查看文件是否存在即可
        print(shell(cmds))
        print(p)
        if p.exists():
            # 成功了
            return True
        else:
            raise Exception
    else:  # 如果不存在，则需要生成文件后再去修改文件
        print(shell(cmds))
        print(p)
        if p.exists():
            # 成功了
            with open(p, 'r+') as f:
                # print(f.read())
                json_txt = json.loads(f.read())
                # "experimentalDecorators": true, //手动增加
                #  "emitDecoratorMetadata": true, //手动增加
                #
                json_txt['compilerOptions']['experimentalDecorators'] = True
                json_txt['compilerOptions']['emitDecoratorMetadata'] = True
                # f.
            with open(p, 'w') as f:
                f.write(json.dumps(json_txt, indent=4))
            return True
        else:
            raise Exception


def create_package_json(prject_path):
    # self.ui.label_4.setText(self.ui.label_4.text() + '--------->【正在配置】')

    file_text = {
        "dependencies": {
            "react": "^18.2.0"
        },
        "name": prject_path.name,
        "version": "1.0.0",
        "main": "index.js",
        "devDependencies": {},
        "dependencies": {
            "@types/react": "^15.6.6",
            "@types/react-reconciler": "^0.18.0",
            "@types/mocha": "^7.0.1"
        },
        "scripts": {
            "test": "echo \"Error: no test specified\" && exit 1"
        },
        "author": "",
        "license": "ISC",
        "description": ""
    }
    package_json_path = Path(prject_path).joinpath('package.json')
    if package_json_path.exists():
        # 如果存在了,那么我就不管了
        print('存在')
        return True
    else:
        with open(package_json_path, 'w') as f:
            f.write(json.dumps(file_text, indent=4))
        if package_json_path.exists():
            return True
        else:
            # 失败了
            raise Exception


# def select_unreal(project_path):
#     # self.ui.label_5.setText(self.ui.label_5.text() + '--------->【正在配置】')
#
#     # 注册表中 UE引擎的注册位置
#     location = r"Unreal.ProjectFile\DefaultIcon"
#     # 获取注册表该位置的所有键值
#     key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, location)
#     # print(key)
#     default_unreal_path = ''
#     try:
#         for i in range(100):
#             default_unreal_path = winreg.EnumValue(key, i)[1]
#     except Exception as e:
#         print(e)
#     finally:
#         winreg.CloseKey(key)
#     # default_unreal_path =
#
#     if default_unreal_path:
#         cmds = [default_unreal_path+" /switchversion "+str(Path(self.path).joinpath(self.project.name+'.uproject'))]
#         print(cmds)
#         res = shell(cmds)
#
#         time.sleep(1)
#         # while True:
#             # #'UnrealVersionSelector.exe'
#             # #'tasklist'
#             # cmds = ['tasklist']
#             # print(cmds)
#             # res = shell(cmds)
#             # print(res)
#         sln_path = Path(self.path).joinpath(self.project.name+'.sln')
#         print(sln_path)
#         if sln_path.exists():
#             self.ui.label_5.setText(self.ui.label_5.text() + '--------->【完成】')
#             return True
#             # break
#         else:
#             self.ui.label_5.setText(self.ui.label_5.text() + '--------->【失败！】')
#             print('不存在')
#             return False
#
#     else:
#         # 没有找到引擎
#         self.ui.label_5.setText(self.ui.label_5.text() + '--------->【失败！没有找到引擎安装路径】')
#         return False
#         pass

def Generate_Project(select_unreal_path, project_path):
    # search_file = Path(self.path).joinpath('Intermediate').joinpath('ProjectFiles').joinpath(self.project.name+'.vcxproj')
    # select_unreal_path = ''
    # with open(search_file,'r',encoding='utf-8') as f:
    #     txt = f.read()
    #     res = re.findall(r'<NMakeOutput>(.*?)</NMakeOutput>',txt)
    #     for r in res:
    #         if ':' in r and 'UnrealEditor.exe' in r:
    #             print(r)
    #             select_unreal_path = Path(r).parent.parent.parent.parent
    #             self.select_unreal_path = select_unreal_path
    #     print(select_unreal_path)
    # D:/UE5GAI22/UnrealEngine5/Engine/Binaries/DotNET/UnrealBuildTool/UnrealBuildTool.exe  -projectfiles -project="D:/testcommon/DEMOUICommon.uproject" -game -engine -progress
    cmds = [str(select_unreal_path.joinpath('Engine').joinpath('Binaries').joinpath('DotNET').joinpath(
        'UnrealBuildTool').joinpath('UnrealBuildTool.exe')) +
            " -projectfiles -project=" + str(Path(project_path).joinpath(project_path.name + '.uproject')) +
            " -game -engine -progress"]
    print(cmds)
    res = str(shell(cmds)[0])
    for r in res.split('\r\n'):
        print(r)
    if '100%' in res:
        return True
    else:
        raise Exception


def npm_install(project_path):
    # self.ui.label_7.setText(self.ui.label_7.text() + '--------->【正在配置】')

    cmds = ['cd ' + str(project_path), str(project_path)[0] + ':', 'npm install']
    print(cmds)
    res = str(shell(cmds)[0])
    for r in res.split('\r\n'):
        print(r)


# def compail_project(select_unreal_path,project_path):
#     cmd_path = str(Path(shell(['where cmd'])[0].replace('\r', '').replace('\n', '')))
#
#     os.startfile(cmd_path,
#                  arguments=' /K ' + str(Path(select_unreal_path).joinpath(
#                      r'Engine\Binaries\ThirdParty\DotNet\Windows\dotnet.exe')) + ' '
#                            + '"' + str(Path(select_unreal_path).joinpath(
#                      r'Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.dll')) + '" '
#                            + project_path.name + 'Editor Win64 Development -Project="' + str(
#                      Path(project_path).joinpath(project_path.name + '.uproject'))
#                            + '" -WaitMutex -FromMsBuild')


if __name__ == '__main__':
    # BUILD_MSG = {
    #     "project": {
    #         "name": "VKPLiveBroadcast",
    #         "branch": "dev_version_v0.1.0_uicommon",
    #         "url": "http://10.0.110.128/demo/demouicommon.git"
    #     },
    #     "plugins": [
    #         {
    #             "name": "v8",
    #             "branch": "main",
    #             "url": "http://10.0.110.128/tools/v8.git"
    #         },
    #         {
    #             "name": "UEReactUMG",
    #             "branch": "dev",
    #             "url": "http://10.0.110.128/tools/uereactumg.git"
    #         },
    #         {
    #             "name": "UEPuerts",
    #             "branch": "dev",
    #             "url": "http://10.0.110.128/tools/uepuerts.git"
    #         },
    #         {
    #             "name": "VKBUICommon",
    #             "branch": "dev_version_v0.0.2_VKBUICommon",
    #             "url": "http://10.0.110.128/virtualkaka_ue/vkbuicommon.git"
    #         },
    #         {
    #             "name": "VKBCommon",
    #             "branch": "dev_version_v0.0.2_VKBCommon",
    #             "url": "http://10.0.110.128/virtualkaka_ue/vkbcommon.git"
    #         }
    #     ]
    # }
    BUILD_MSG = eval(sys.argv[1])

    PROJECT_PATH = CONFIG['project_abs_path'].joinpath(BUILD_MSG['project']['name'])
    UE_ROOT_PATH = CONFIG['UE_ROOT_PATH']

    # 2023.2.24李臣增加王攀注入环境和版本号的逻辑
    _project_name = BUILD_MSG['project']['name']
    _env = BUILD_MSG['platform']
    _version = BUILD_MSG['version']
    configIni = configparser.ConfigParser(strict=False)
    version_ini_path = rf'D:\projects\{_project_name}\Plugins\VKBCommon\Config\Version.ini'
    if not os.path.exists(version_ini_path):
        if not os.path.exists(rf'D:\projects\{_project_name}\Plugins\VKBCommon\Config'):
            os.mkdir(rf'D:\projects\{_project_name}\Plugins\VKBCommon\Config')
        with open(version_ini_path, 'w') as f:
            f.write('[Env]\nenv=meta\n[Version]\nversion=v0.2.0')
    configIni.read(version_ini_path)
    configIni.set('Env', 'env', _env)
    configIni.set('Version', 'version', _version)
    configIni.write(open(version_ini_path, 'w'))
    # 增加修改项目名称的逻辑2023.3.6
    default_game_ini_path = rf'D:\projects\{_project_name}\Config\DefaultGame.ini'
    project_name = '虚拟咔咔' + _version
    if _env == 'test':
        project_name = '【测试环境】虚拟咔咔' + _version
    elif _env == 'dev':
        project_name = '【开发环境】虚拟咔咔' + _version
    elif _env == 'pre':
        project_name = '【预发环境】虚拟咔咔' + _version
    elif _env == 'online':
        project_name = '虚拟咔咔' + _version
    file_data = ""
    with open(default_game_ini_path, "r", encoding='utf-8') as f:
        for line in f:
            line = line.replace('虚拟咔咔直播工具V1.0.0', project_name)
            file_data += line
    with open(default_game_ini_path, "w", encoding='utf-8') as f:
        f.write(file_data)
    # ----------------------------------------------
    # 任务列表
    try:

        # check_npm()
        # check_tsc()
        excute_js(PROJECT_PATH)
        create_package_json(PROJECT_PATH)
        Generate_Project(UE_ROOT_PATH, PROJECT_PATH)
        npm_install(PROJECT_PATH)
        Generate_Project(UE_ROOT_PATH, PROJECT_PATH)
        # compail_project(UE_ROOT_PATH,PROJECT_PATH)
        # 编译项目交给jenkins

        # 删除两个BAT文件
        if os.path.exists(str(Path(PROJECT_PATH).joinpath('CopyExeAndPdb_VKP.bat'))):
            os.remove(str(Path(PROJECT_PATH).joinpath('CopyExeAndPdb_VKP.bat')))
        if os.path.exists(str(Path(PROJECT_PATH).joinpath('CopyExeAndPdb_VKP-sample.bat'))):
            os.remove(str(Path(PROJECT_PATH).joinpath('CopyExeAndPdb_VKP-sample.bat')))

    except Exception as e:
        print("因为异常触发了退出", str(e))
        exit(1)
