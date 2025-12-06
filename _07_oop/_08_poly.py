"""
    python 面向对象 - 多态
"""


class Animal:
    def cry(self):
        pass


class Cat(Animal):
    def cry(self):
        print('小猫 喵喵喵的哭...')


class Dog(Animal):
    def cry(self):
        print('小狗 汪汪汪的哭...')


class Bird(Animal):
    def cry(self):
        print('小鸟 叽叽叽的哭...')


# 父类对象可以接受多个子类对象，然后实际调用时更加具体的子类对象去调用具体子类的方法
def animalCry(animal: Animal):
    animal.cry()


if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    bird = Bird()

    # 子类对象均可以传递个父类类型变量，然后运行时父类类型变量是调用具体子类的方法
    animalCry(cat)
    animalCry(dog)
    animalCry(bird)
    print("-" * 30)

    # 判断对象是否为某个类或其子类的对象
    print(isinstance(cat, Cat))
    print(isinstance(dog, Dog))
    print(isinstance(bird, Bird))
    print(isinstance(bird, Animal))
    print("-" * 30)

    # 还可以用于判断的变量类型，因为 python 一切皆为对象
    num = 9
    info = 'abc'
    print(isinstance(num, int))
    print(isinstance(info, str))
    print(isinstance(info, int))

    # 还可以用于判断容器类型
    print(isinstance(info, list))
    print(isinstance(info, tuple))
    print(isinstance(info, set))
    print(isinstance(info, dict))

    # 可以指定多个类型（使用元组），判断变量符合其中任意一种类型
    print(isinstance(info, (int, str)))
    print(isinstance(info, (int, float)))
