"""
    python 一切皆为对象，每个对象都有一个布尔值，可以通过内置 bool() 获取
"""

if __name__ == '__main__':
    # 内置布尔值为 False 的对象
    print(bool(False))  # False
    print(bool(0))      # 数值 0
    print(bool(None))   # None
    print(bool(""))     # 空字符串
    print(bool([]))     # 空列表
    print(bool(()))     # 空元组
    print(bool({}))     # 空字典
    print(bool(set()))  # 空集合

    # 因为所有对象都有一个布尔值，所以代码中可以使用对象进行布尔值判断
    content = "hello"
    if content:
        print(f"has content: {content}")
    else:
        print(f"has no content")

    lst = [1, 2, 3]
    if lst:
        print(f"lst content: {lst}")
    else:
        print(f"lst has no content")
