"""
    python Class 对象
    - 所有类实际上都是 Class 类的对象
"""


class Monster:
    name = '石头怪'

    def hi(self):
        print(f'hi {self.name}')

    # 定义类的静态方法，静态方法不需要接受 self 参数
    @staticmethod
    def hi_static():
        print(f'hi Monster static')


if __name__ == '__main__':
    # Monster 这个类，实际上是 Class 类的一个对象
    print(Monster)

    # 通过类名调用类的对象方法，对象方法需要手动传入一个该类的对象作为 self 参数
    monster = Monster()
    Monster.hi(monster)

    # 通过类名可以直接调用类的静态方法
    Monster.hi_static()
    # 类的对象也可以调用类的静态方法
    monster.hi_static()
