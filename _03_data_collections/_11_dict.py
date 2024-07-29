"""
    11 python 字典
    字典是一种映射类型，非常适合处理通过 key（键/关键字）来查询对应 value（值）的需求。

    - 字典的定义
    - 访问字典的元素

    - 字典的 key 通常为字符串或数字，value 可以是任意类型（甚至可以是列表，元组，集合）。
    - 对字典进行遍历（遍历 key，遍历 value，遍历 <key,value>）
    - 创建空字典
    - 字典的 key 必须是唯一的，如果指定了多个相同的 key，后续 key 的值将会覆盖前面 key 所指定的值。
"""
# 字典的定义
dict_a = {"name": "Tom", "age": 23, "address": "JD"}
print(f"字典 dict_a 的内容：{dict_a} 字典的类型：{type(dict_a)}")
print("="*30)

# 访问字典元素
print(dict_a["age"])
print("="*30)

# 字典的复合数据类型
dict_multi = {
    "jack": [100, 200, 300],
    "mary": (100, 20, "hello"),
    "none": {'apple', "pear"},
    "smith": "computer",
    "tom": {
        "性别": "男",
        "age": 18,
        "地址": "香港",
        19: 20,
        20: 'yes'
    }
}
print(dict_multi)
print(dict_multi["tom"])
print(dict_multi["tom"][20])
print("="*30)

# 遍历字典所有 key
for k in dict_multi:
    print(f"{k}: {dict_multi[k]}")
print("-"*30)

# 遍历字典所有 value
for v in dict_multi.values():
    print(f"{v}: {type(v)}")
print("-"*30)

# 遍历字典所有 key，value
for k, v in dict_multi.items():
    print(f"{k}: {v}")
print("="*30)

# 创建空字典
dict_empty = {}
dict_empty_a = dict()
print(f"空字典 dict_empty 的内容：{dict_empty} 字典的类型：{type(dict_empty)}")

