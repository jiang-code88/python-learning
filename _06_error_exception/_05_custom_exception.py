"""
    自定义异常
    1. 程序可以通过创建新的异常类命名自己的异常。
       不管是以直接还是间接的方式，自定义异常都应从 Exception 类派生出来。
    2. 自定义异常类通常应当保持简单，它往往只提供一些属性，允许相应的异常处理程序提取有关错误的信息。
    3. 自定义异常命名通常都以 Error 结尾。
"""


# 自定义异常-AgeError
class AgeError(Exception):
    pass


# 自定义异常使用
# 如果输入年龄不在 18-29 之间时，抛出 AgeError 异常
while True:
    try:
        input_value = input("请输入年龄（18-29）：")
        if input_value == "quit":
            print("退出程序")
            break
        age = int(input_value)
        if age < 18 or age > 29:
            raise AgeError(f"！！！输入的年龄 {age} 并不在范围（18-29）之内")
        print(f"》》》你输入的年龄为：{age}")
    except ValueError:
        print(f"！！！你输入的年龄不是整数")
    except AgeError as e:
        print(e)
