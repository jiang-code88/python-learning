"""
    04 数据容器-元组
    元组可以存放多个不同类型数据，元组是不可变序列

    - 元组的定义
    - 元组的使用
    - 元组的遍历

    - 定义空元组
    - 元组元素可以有多个，数据类型没有限制（允许嵌套元组），允许有重复元素，元素有序。
    - 元组是不可变序列不允许增，删，改操作，但是元组中 list 类型元素的内容可以被增、删改。
    - 元组索引也可以从尾部开始，最后一个元素索引为 -1，倒数第二个元素索引为 -2 以此类推。
    - 只有一个元素的元组，定义时需要带上逗号（,），否则就不是元组了。

    - 元组的意义：
      - 多线程环境下，元组可以充当不可变对象，避开线程不安全问题，节省同步操作的开销。
        所以不需要对元组进行增删改时，优先考虑元组。
      - 元组在创建时间和空间占用上都由于列表。
      - 元组能够对不需要修改的数据写保护（防止误擦写）。
"""
# 1 元组的定义
tuple_a = (100, 200, 300, 400, 500)
tuple_b = ('read', 'green', 'blue', 'yellow', 'white', 'black')
print(f"元组 tuple_a 的内容：{tuple_a} 类型：{type(tuple_a)}")
# 2 元组的使用
print("元组 tuple_b 的第二个元素：", tuple_b[1])  # 索引从 0 开始s
print("=======================")

# 3 元组的遍历
for item in tuple_b:
    print(item)
print("-----------------------")

i = 0
while i < len(tuple_b):
    print(tuple_b[i])
    i += 1
print("=======================")

# 4 定义空元组
tuple_empty_a = ()
tuple_empty_b = tuple()
print(f"元组 tuple_empty_a 的内容：{tuple_empty_a} 类型：{type(tuple_empty_a)}")
print(f"元组 tuple_empty_b 的内容：{tuple_empty_b} 类型：{type(tuple_empty_b)}")
print("=======================")

# 元组元素可以有多个，数据类型没有限制（允许嵌套元组），允许有重复元素，元素有序。
tuple_multi = (100, 'jack', 4.5, True, "jackson")
print(f"元组 tuple_multi 的内容：{tuple_multi}")
tuple_nest = (100, "tom", ("jackson", 300, False))
print(f"元组 tuple_nest 的内容：{tuple_nest}")
print("=======================")

# 元组是不可变序列不允许增，删，改操作，但是元组中 list 类型元素的内容可以被增、删改
tuple_list = (1, 1.2, ["Jack", "Tome", "Jackson"])
print(f"修改前元组 tuple_list 的内容：{tuple_list}")
tuple_list[2][1] = "Lili"
print(f"修改后元组 tuple_list 的内容：{tuple_list}")
print("=======================")

# 只有一个元素的元组，定义时需要带上逗号（,），否则就不是元组了。
no_tuple_single = (100)
print(f"非元组 tuple_single_a 的内容：{no_tuple_single} 类型：{type(no_tuple_single)}")
tuple_single = (100,)
print(f"元组 tuple_single 的内容：{tuple_single} 类型：{type(tuple_single)}")


