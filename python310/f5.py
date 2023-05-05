# str1 = "admin"
# print(str1.replace("ad", "baidu"))  # 替换
# print(str1.find("d"))  # 查看索引
# print(str1.startswith("d"))  # 以什么什么开头,返回布尔类型
# print(str1.endswith("n"))  # 以什么什么结尾,返回布尔类型
# print(str1.isdigit())  # 判断字符串内容是否为数字,返回布尔类型

# list1 = [11, 22, 33, 44, 55, 66, 22]
#
# list1.append(77)  # 结尾添加
# list1.insert(0, 99)
# print(list1)
#
# list2 = list1.copy()  # 复制内容
# print(list2)
#
# print(list1.count(22))  # 统计出现次数
# print(list1.index(33))  # 查看索引
#
# list1.remove(22)  # 删除固定
# print(list1)
#
# print(list1.pop())  # 默认删除最后一位并打印出来
# print(list1)
#
# list1.extend(list2)  # 将列表2的对象增加至列表1的结尾
# print(list1)
#
# list1.reverse()  # 将内容反转
# print(list1)
#
# list1.sort()  # 从小到大排序
# print(list1)

# list1 = [11, 22, 33, 44, 55, 66, 22]
# # for i in list1:
# #     if i > 55:
# #         print(i)
#
# print([x + 1 for x in list1])  # 其中x+1为最终要输出的内容  ---- 列表推导式
#
# print([x for x in list1 if x > 33])
#
# tuple1 = (1, 2, 3, 4)
# print(dir(tuple1))

# 元组不可变,但其中的对象可变
# tuple2 = (1, 2, 3, {'name': '李华', 'age': 12}, [22, 33, 44])
#
# tuple2[4][0] = 11
# print(tuple2)
#
# tuple2[3]['name'] = '小明'
# print(tuple2)

# dict1 = {'name': '李华', 'age': 12}
# dict2 = dict1.copy()  # 复制对象
# print(dict2)
#
# # dict1.clear()
# # print(dict1) # 清除对象
# print(dict1.get('age'))  # 输出对应键的值
# for key in dict1.keys():
#     print(key)
#
# for value in dict1.values():
#     print(value)

# for key, value in dict1.items():  # 输出kv值
#     print(key, ' :', value)

# dict2 = {'city': 'beijing'}
# dict1.update(dict2)  # 将字典2的对象增加到字典1
# print(dict1)

# 字典本身是无序的数据类型
# dict1 = {'name': '李华', 'age': 12, 'city': 'beijing'}
# dict2 = {'num1': 10, 'num2': 12, 'num3': 0}
# 在 lambda 表达式中，冒号也用于分隔参数列表和函数体
# print(sorted(dict1.items(), key=lambda item: item[0]))  # 根据字典的键排序
# print(sorted(dict1.items()))  # 根据字典的键排序
# print(sorted(dict2.items(), key=lambda item: item[1]))
