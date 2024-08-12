"""
    02 捕获处理异常
"""

# 捕获处理异常的语法
"""
try:
    可能出现异常的代码
except [异常 as 别名]:
    发生异常时，处理异常的代码
[else:]
    没有发生异常时，执行的代码
[finally:]
    不管有没有异常，都要执行的代码
"""

# 1 保证程序可以持续的运行下去，并不关心到底出现什么异常
# 没有 [异常 as 别名] 时代表捕获所有的异常并执行处理代码
try:
    num1 = 10
    num2 = 0
    res = num1 / num2
except:
    print(f"捕获到异常")
print("程序继续执行...")

# 2 保证程序可以持续的运行下去，并不关心到底出现什么异常
# 捕获处理 Exception 类型以及其子类型的异常
try:
    num1 = 10
    num2 = 0
    res = num1 / num2
except Exception as e:
    print(f"捕获到异常，异常是 {e} 类型是 {type(e)}")
print("程序继续执行...")

# 3 只处理某些异常（业务处理），其他异常不管出现他们时就中止程序吧
try:
    num1 = 10
    num2 = 0
    res = num1 / num2
except ZeroDivisionError as ze:
    print(f"捕获到异常，异常是 {ze} 类型是 {type(ze)}")
print("程序继续执行...")
