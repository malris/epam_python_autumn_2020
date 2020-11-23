"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from functools import wraps


def instances_counter(cls):
    """
    A decorator for counting class instances.
    """
    cls.instance_counter = 0

    def counted_init(f):
        """
        A decorator for counting class instances in __init__.
        """

        @wraps(f)
        def wrapper(*args, **kwargs):
            args[0].__class__.instance_counter += 1
            f(*args, **kwargs)

        return wrapper

    def get_created_instances(_cls) -> int:
        """
        Return the number of existed class instances.
        """
        return _cls.instance_counter

    def reset_instances_counter(_cls) -> int:
        """
        Reset counter of existed class instances.
        :return: Value of class instance counter before reset
        """
        old_class_count = _cls.instance_counter
        _cls.instance_counter = 0
        return old_class_count

    cls.__init__ = counted_init(cls.__init__)
    cls.get_created_instances = classmethod(get_created_instances)
    cls.reset_instances_counter = classmethod(reset_instances_counter)
    return cls


@instances_counter
class User:
    def __init__(self):
        print("original class init")


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()

    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())  # 0
    _ = User()
    print(user.reset_instances_counter())  # 1
