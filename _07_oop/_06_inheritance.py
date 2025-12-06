"""
    python 面向对象 - 继承

    语法：
    class DerivedClassName(BaseClassName):
        ...

    - python 语言中，Object 类是所有类的父类
    - python 支持多重继承
      语法：
      class DerivedClassName(BaseClassName1, BaseClassName2, BaseClassName3):
        ...
    - 在多重继承中，如果有同名的成员变量或方法，遵循从左到右的继承优先级，即左边写的类的优先级大于右边写的类
      例如 BaseClassName1 和 BaseClassName2 中同名方法，只会继承 BaseClassName1 的。
    - 子类和父类中的都有的同名成员变量或成员方法，子类可以使用 super() 来指定调用的是父类的成员变量或成员方法
"""


class Student:
    name = None
    age = None
    __score = None

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score

    def set_score(self, score):
        self.__score = score

    def show_info(self):
        return f"name={self.name}, age={self.age}, score={self.__score}"

    def get_score(self):
        return self.__score


# 小学生
class Pupil(Student):
    __status = None

    def __init__(self, name, age, score, status):
        # 通过 super() 调用父类的构造函数，对子类从父类继承下来的成员变量进行初始化
        super().__init__(name, age, score)
        self.__status = status

    # python 子类会继承父类的所有成员变量和成员方法
    # 子类可以通过直接访问父类的非私有成员变量和成员方法
    # 子类不可以直接访问私有的成员变量和方法，必须通过父类的提供的公共方法访问。
    def testing(self):
        print(f"小学生 {self.name} 考小学数学... 预期成绩 {self.get_score()}")

    # 子类重写的父类 show_info 方法
    def show_info(self):
        # 使用 super() 指定调用的是父类方法，而 self 调用的是子类的成员变量
        return f"{super().show_info()}, status={self.__status}"

        # 除了 super() 还可以使用 父类名.成员方法(self) 和 父类名.成员变量 方式等效使用。
        # return f"{Student.show_info(self)} status={self.__status}"


# 大学生
class Granter(Student):

    def testing(self):
        print(f"大学生 {self.name} 考高等数学... 预期成绩 {self.get_score()}")


if __name__ == '__main__':
    student1 = Pupil("paul", 5, 100, 1)
    student1.testing()
    student1.set_score(99)
    print(student1.show_info())
    print("-" * 30)

    student2 = Granter("jackson", 26, 80)
    student2.testing()
    student2.set_score(60)
    print(student2.show_info())
