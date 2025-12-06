"""
    python 类型注解
    - 类型提示，防止运行时出现参数类型，返回值类型，变量类型不符合异常。
    - 类型注解，不会影响程序的正常运行，只是提示作用，也就是即使提示类型不匹配依旧还是可以运行的
"""
from typing import Union


# 遍历打印字符串中每一个字符
def func(s):
    for ele in s:
        print(ele)


def func_type_hint(s: str):
    for ele in s:
        print(ele)


# 基础数据类型的类型注解
v1: int = 100
v2: float = 1.2
v3: bool = True
v4: str = 'abc'


# 实例的类型注解
class Car:
    pass


cat: Car = Car()
# 需要 Car 类型但是传递的是 str 类型不符合编辑器会提示
# cat: Car = "car"


# 容器类型的类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {'a': 1, 'b': 2}

# 容器类型的详细类型注解
# list[int] 表示有 int 类型元素的列表，某一个元素匹配该类型即可。
my_list_1: list[int] = [1, 2, 3, 'str']
# 元组的每一个元素的类型，都要在类型注解中有标记
my_tuple_1: tuple[int, int, int, str] = (1, 2, 3, 'abc')
# set[int] 表示有 int 类型元素的集合，某一个元素匹配该类型即可。
my_set_1: set[int] = {1, 2, 3, 'str'}
# dict[str, int] 表示 [key的类型, value的类型]
my_dict_1: dict[str, int] = {'a': 1, 'b': 2}


# 方法的形参类型注解和返回值类型注解
# 参数 a 的类型为 int，参数 b 的类型为 str，返回值类型为 str
def method(a: int, b: str) -> str:
    pass


# Union 类型
# 使用前需要导入Union：from typing import Union
# Union[X, Y] 等价于 Union[X｜Y] 表示类型满足 X 或 Y 之一
v10: Union[int, str] = 100

if __name__ == '__main__':
    # 对于函数 func，参数应该传递的字符串
    func('abc')
    # 如果传递 int 类型值，在 python 函数运行时将报错
    # func(123)
    print('-' * 30)

    # 如果不希望这种类型不符合异常，在程序运行期间报错，影响程序运行稳定性，
    # 可以在方法参数上增加类型注解，标记该形参接受的数据类型，
    # 便于编辑器在编辑期间检测提示类型不匹配，预防类型不符合报错
    func_type_hint('abc')
    # func_type_hint(123)
