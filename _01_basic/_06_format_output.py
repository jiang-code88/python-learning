"""
    06 python 格式化输出
     - 常规打印
     - % 操作符的格式化输出
     - format() 函数的格式化输出
     - f-string 字符串的格式化输出
"""
name = "john"
age = 23
gender = "male"
score = 120.45

# 常规打印输出
print("个人信息：", name, age, gender, score)

# % 操作符的格式化输出
print("个人信息：%s-%d-%s-%0.3f" % (name, age, gender, score))

# format() 函数的格式化输出
print("个人信息：{}, {}, {}, {}".format(name, age, gender, score))

# f-strings 字符串的格式化输出（简洁明了，推荐使用）
print(f"个人信息：{name}, {age}, {gender}, {score}")
