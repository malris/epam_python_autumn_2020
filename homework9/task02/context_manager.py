"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with suppressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Suppressor:
    """
    Suppresses passed exception.
    """

    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            is_error_found = issubclass(exc_type, self.exception)
        except TypeError:
            pass
        else:
            return is_error_found


@contextmanager
def suppressor(exception):
    """
    Suppresses passed exception.
    If exception doesn't inherit BaseException, it raises TypeError
    """
    try:
        yield
    except exception:
        pass
