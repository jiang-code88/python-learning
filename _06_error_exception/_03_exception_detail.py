"""
    03 捕获处理异常细节
"""
# 1 如果异常发生了，则异常后的代码将不会被执行，直接进入 expect 指定代码块中。
# 2 如果异常没有发生，则顺序执行 try 指定代码快代码，不会进入 expect 指定代码块中执行。
# 3 如果希望 try 指定代码块在没有发生异常时，要执行某些代码，则使用 else 指定代码块。
# 4 如果希望不管是否抛出异常，都要执行某些代码（比如关闭连接，释放资源等），则使用 finally 指定代码块。
# 5 可以有多个 expect 语句指定代码块，捕获不同的异常进行不同的业务处理，
#   如果发生异常，只会匹配一个 expect 语句，所以建议把具体异常的捕获写在前面，基类异常写在后面。
#   这样当具体异常捕获不到时，再由基类异常兜底来进行捕获。
# 6 一个 expect 语句可以捕获多个不同异常，语法是 expect(IndexError, ZeroDivisionError) as e:
# 
