"""
    01 列表
     - 列表的定义
     - 列表的使用
     - 列表的遍历

     - 定义空列表
     - 列表元素数据类型无限制，允许有重复元素，存取元素有序
     - 列表索引可以从尾部开始，最后一个元素索引是 -1, 倒数第二个元素索引是 -2 ...
       其实就是计算 len(列表) -1 作为索引访问列表
     - 列表元素增、删、改操作

     - 数据容器类型变量的赋值传递是：地址传递
     - 数据容器类型变量的函数参数传递是：地址传递
"""
# 列表的定义
list1 = [1, 2, 3, 4, 5]
list2 = ["red", "green", "blue", "yellow", "white", "black"]
print(f"list1: {list1}")
print(f"list1 type: {type(list1)}")
print(f"list2: {list2}")
print("================================")

# 列表的使用
# 列表名[索引]
# 列表项索引是从 0 开始计算时
print(f"list2 的第一个元素 list[0]: {list2[0]}")
print("================================")

# 列表的遍历
for item in list2:
    print(item)

i = 0
while i < len(list1):
    print(f"list1 第 {i} 个元素：{list1[i]}")
    i += 1
print("================================")

# 空列表
list_0 = []
list_1 = list()
print(f"list_0: {list_0}, list_0 type: {type(list_0)}")
print(f"list_1: {list_1}, list_1 type: {type(list_1)}")
print("================================")

# 列表元素数据类型无限制（允许嵌套列表），允许有重复元素，元素有序
list_2 = [100, "jackson", 4.5, True, "jackson", 4.5, ["yeezy", 300]]
print(f"list_2: {list_2}, list_2 type: {type(list_2)}")
print("================================")

# 列表索引从尾部开始
list_3 = [1, 2, 3, 4, 5]
print(f"list_3 倒数第一个元素：{list_3[-1]}")
print(f"list_3 倒数第二个元素：{list_3[-2]}")
print("================================")

# 列表元素增、删、改
list_4 = [1, 2, 3, 4, 5]
list_4.append(100)
del list_4[1]
list_4[0] = "jackson"
print(f"list_4: {list_4}")
print("================================")

# 列表的元素被修改后，列表变量指向的内存地址不变，只是列表的数据内容变了
list_5 = [1, 2, 3, 4, 5]
print(f"list_5: {list_5}, 地址：{id(list_5)}, "
      f"list_5[1] 元素值：{list_5[1]}, 地址：{id(list_5[1])}")
list_5[1] = 10
print(f"list_5: {list_5}, 地址：{id(list_5)}, "
      f"list_5[1] 元素值：{list_5[1]}, 地址：{id(list_5[1])}")
print("================================")

a = 10
b = a  # 基本数据类型变量的传递是：值传递
b = 20
# 修改 b 变量的值，不会影响 a 变量的值
print(f"a: {a} 地址：{id(a)}, b: {b} 地址：{id(b)}")

list_6 = [1, 2.1, "name"]
list_7 = list_6  # 数据容器类型变量的传递是：地址传递
list_7[1] = 100
# 修改 list_7 容器变量元素的值，会影响 list_6 容器变量元素的值
print(f"list_6: {list_6} 地址：{id(list_6)}")
print(f"list_7: {list_7} 地址：{id(list_7)}")
print("================================")


# 数据容器类型变量的函数参数传递是：地址传递
list_8 = [1, 2, 3, 4, 5]
print(f"list_8: {list_8} 地址：{id(list_8)}")


def function(l):
    l[1] = 100
    print(f"function arg l: {l} 地址：{id(l)}")
    return l


list_9 = function(list_8)
print(f"list_8: {list_8} 地址：{id(list_8)}")
print(f"list_9: {list_9} 地址：{id(list_9)}")
