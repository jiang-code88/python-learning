"""
    13 数据容器-总结
    - 数据容器的通用转换
      list(容器)  将序列，支持迭代的容器或其他可迭代对象转换为列表
      str(容器)   将指定容器转换为字符串
      tuple(容器) 将序列，支持迭代的容器或其他可迭代对象转换为元组
      set(容器)   将序列，支持迭代的容器或其他可迭代对象转换为集合
    - python 数据类型
      - 可变数据类型：当该数据类型的变量的值发生变化时，它的内存地址不变，那么这个数据类型就是可变数据类型。
        包括 list(列表)、set(集合)、dict(元组)
      - 不可变数据类型：当该数据类型的变量的值发生变化时，他的内存地址改变，那么这个数据类型就是不可变数据类型。
        包括 数值类型(int、float)、bool(布尔)、string(字符串)、tuple(元组)
"""
str_a = "hello"
list_a = ["red", "blue", "white"]
tuple_a = ("red", "blue", "white")
set_a = ("red", "blue", "white")
dict_a = {"red": "红色", "blue": "蓝色", "white": "白色"}

# 1 转换为列表
print(f"字符串 str_a 转换为列表：{list(str_a)}，类型：{type(list(str_a))}")
print(f"元组 tuple_a 转换为列表：{list(tuple_a)}，类型：{type(list(tuple_a))}")
print(f"集合 set_a 转换为列表：{list(set_a)}， 类型：{type(list(set_a))}")
print(f"字典 dict_a 转换为列表：{list(dict_a)}，类型：{type(list(dict_a))}")  # 只取字典项的 key 转换
print("-" * 60)

# 2 转换为字符串
print(f"列表 list_a 转换为字符串：{str(list_a)}，类型：{type(str(list_a))}")
print(f"元组 tuple_a 转换为字符串：{str(tuple_a)}，类型：{type(str(tuple_a))}")
print(f"集合 set_a 转换为字符串：{str(set_a)}，类型：{type(str(set_a))}")
print(f"字典 dict_a 转换为字符串：{str(dict_a)}，类型：{type(str(dict_a))}")
print("-" * 60)

# 3 转换为元组
print(f"字符串 tuple_a 转换为元组：{tuple(str_a)}，类型：{type(tuple(str_a))}")
print(f"列表 list_a 转换为元组：{tuple(list_a)}，类型：{type(tuple(list_a))}")
print(f"集合 set_a 转换为元组：{tuple(set_a)}，类型：{type(tuple(set_a))}")
print(f"字典 dict_a 转换为元组：{tuple(dict_a)}，类型：{type(tuple(dict_a))}")
print("-" * 60)

# 4 转换为集合
print(f"字符串 tuple_a 转换为集合：{set(str_a)}，类型：{type(set(str_a))}")
print(f"列表 list_a 转换为集合：{set(list_a)}，类型：{type(set(list_a))}")
print(f"元组 set_a 转换为集合：{set(tuple_a)}，类型：{type(set(tuple_a))}")
print(f"字典 dict_a 转换为集合：{set(dict_a)}，类型：{type(set(dict_a))}")
print("-" * 60)

