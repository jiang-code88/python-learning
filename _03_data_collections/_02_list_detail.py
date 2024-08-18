"""
    02 数据容器-列表-常用操作
     - count(x) 元素 x 在列表中的出现次数
     - extend(xx) 向列表中追加列表中的所有元素
     - index(x)  查找列表中元素 x 所在的索引
     - reverse() 翻转列表中的所有元素
     - insert(x, y) 在列表索引 x 处，插入元素 y

    列表生成式（生成列表的公式）
     - 基本语法：[列表元素的表达式 for 自定义变量 in 可迭代对象]
"""
list_a = [100, 200, 300, 400, 500]
print("100 出现的次数是：", list_a.count(200))
print("==========================")

list_b = [600, 700, 800]
print("list_a：", list_a)
print("list_b：", list_b)
list_a.extend(list_b)
print("list_a 追加 list_b 后的内容：", list_a)
print("==========================")

print("list_a 中 500 元素所在的索引：", list_a.index(500))
print("==========================")

list_a.reverse()
print("list_a 翻转后的结果：", list_a)
print("==========================")

list_a.insert(0, 10000)
print("list_a 在索引 0 处插入元素 10000 后的结果：", list_a)
print("==========================")

list_c = [ele for ele in range(1, 5)]
print("list_c 列表内容：", list_c)
print("==========================")

list_d = [ele * 2 for ele in range(1, 5)]
print("list_d 列表内容：", list_d)
print("==========================")

list_e = [ele + ele for ele in "hello"]
print("list_e 列表内容：", list_e)
print("==========================")


