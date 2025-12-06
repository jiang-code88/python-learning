"""
    python 抽象类

    - python 实现抽象类需要导入 ABC 模块 from abc import ABC
      然后让普通类继承 ABC 成为抽象类，使用 @abstractmethod 声明抽象方法。
    - 抽象类不可以被实例化，并且需要至少一个抽象方法，抽象类的子类必须实现父类的所有抽象方法。
    - 抽象类可以有普通方法，如果子类没有实现父类的所有抽象方法，子类依旧是抽象类。
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    name = None

    def __init__(self, name):
        self.name = name

    # 定义抽象类中的抽象方法
    @abstractmethod
    def cry(self):
        pass


class Tiger(Animal):
    def cry(self):
        print(f'Tiger {self.name} is crying')

    def hi(self):
        print(f'Tiger {self.name} is hiding')


if __name__ == '__main__':
    # 抽象类不可以被实例话，抽象类必须作为父类被继承，然后子类实现父类的方法
    # 如果实例化抽象类将报错 TypeError: Can't instantiate abstract class Animal without an implementation for abstract method 'cry'
    # animal = Animal('Tiger')
    # animal.cry()

    # 实例化抽象类的子类使用
    tiger = Tiger('Tiger')
    tiger.cry()
