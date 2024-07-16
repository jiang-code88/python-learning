"""
    12 数据类型-字符串
     - 单引号、双引号
     - 简单字符串和复杂字符串
     - 非转义字符串
"""
# 1 单引号和双引号的区别
str_1 = 'Tom say "hello"'
str_2 = "Paul say \"hello\""
str_3 = "Bob say 'hello'"
print(str_1, str_2, str_3)
print("====================================")


# 2 python 中不支持单字符类型，单字符在 python 中也是作为一个字符串使用
str_4 = 'A'
print(str_4, type(str_4))
print("====================================")


# 3 python 中使用三个单引号'''或双引号"""，表示复杂的字符串内容
str_5 = """import sys
sys.float_info.dig\n
15

s = '3.14159265358979'    # decimal string with 15 significant digits
format(float(s), '.15g')  # convert to float and back -> same value\n
'3.14159265358979'"""
print(str_5, type(str_5))
print("====================================")


# 4 在字符串前面加上 r 可以使得整个字符串中的转义字符不被转义输出
str_6 = r"""import sys
sys.float_info.dig\n
15

s = '3.14159265358979'    # decimal string with 15 significant digits
format(float(s), '.15g')  # convert to float and back -> same value\n
'3.14159265358979'"""
print(str_6, type(str_6))

# TODO: 字符串驻留机制（待学习补充）
