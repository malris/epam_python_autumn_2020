"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на место отведенное под него
В конечном варанте кода будет вызываться AttributeError при custom_sum.__original_func
Это корректное поведение
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools

WRAPPER_ASSIGNMENTS = ("__name__", "__doc__")


def my_wraps(func, assigned=WRAPPER_ASSIGNMENTS):
    def wrapper(wrapped_func):
        def wrapped(*args, **kwargs):
            return wrapped_func(*args, **kwargs)

        for attr in assigned:
            try:
                value = getattr(func, attr)
            except AttributeError:
                pass
            else:
                setattr(wrapped, attr, value)
        setattr(wrapped, "__original_func", func)

        return wrapped

    return wrapper


def print_result(func):
    @my_wraps(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
