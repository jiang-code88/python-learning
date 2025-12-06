"""
    python 面向对象 - 封装

"""
class Person:
    """
        类中成员变量或成员方法名以 __ 开头，则该变量或方法就是私有的，
        私有变量和方法只允许类内部访问，不允许类外部访问。
    """
    name = None
    __age = None
    __job = "python 工程师"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def hello(self):
        print(f"Hello {self.name}!")

    def __speak(self):
        print(f"Speak my name: {self.name}!")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_job(self):
        return self.__job


if __name__ == '__main__':
    person = Person("paul", 23)

    print(person.name)
    # 私有变量，类外部不可以访问
    # print(person.age)  # 报错 'Person' object has no attribute 'age'

    # 类外部使用 get 方法访问私有变量
    print(person.get_age())
    person.set_age(25)
    print(person.get_age())
    print("-" * 30)

    person.hello()
    # 私有方法，类外部不可访问
    # person.speak()  # 报错 'Person' object has no attribute 'speak'
    print("-" * 30)

    # python 语言具有动态特性，可以动态的创建类中成员变量，
    # 但此时赋值创建的 __job 成员变量和类中私有成员变量 __job 是不同的
    # 第一个是普通的名为 __job 的成员变量，第二个实际上是名称为 _Person__job 的成员变量。
    person.__job = "Java工程师"
    print(person.__job)
    print(person.get_job())




