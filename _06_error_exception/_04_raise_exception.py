"""
    04 python 主动触发(抛出)异常
"""
# raise 语句支持强制触发(抛出)指定异常
try:
    raise ZeroDivisionError("主动触发 ZeroDivisionError 异常")
except Exception as e:
    print(f"捕获到异常，异常是 {e} 类型是 {type(e)}")
