"""
    12 字典的常用操作
    - len(dict) 返回字典 dict 中的键值对项数
    - dict[key] 返回字典 dict 中的以 key 为键的值
    - del dict[key] 把键值对从字典中删除
    - dict.keys() 返回字典中所有的 key
    - key in dict 判断 key 是否存在字典中
    - clear() 移除字典中所有的键值对

    - 字典生成式
      - 语法：{字典 key 表达式:字典 value 表达式 for key 变量, value 变量 in zip(key 可迭代对象, value 可迭代对象)}

"""
dict_a = {"name": "Tom", "age": 23, "address": "JD"}
dict_a_keys = dict_a.keys()
print(f"dict_a 字典中的 key 有：{dict_a_keys}, 类型为：{type(dict_a_keys)}")

# 字典生成式
books = ["《红楼梦》", "《三国演义》", "《西游记》", "《水浒传》"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
dict_book_author = {book: author for book, author in zip(books, authors)}
print(dict_book_author)

color_name_en = ["red", "green", "blue"]
color_name_zh = ["红色", "绿色", "蓝色"]
dict_color = {color_zh: color_en.upper() for color_zh, color_en in zip(color_name_zh, color_name_en)}
print(dict_color)