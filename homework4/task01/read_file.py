"""
Write a function that gets file path as an argument.
Read the first line of the file.
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.
Write a test for that function using pytest library.
Definition of done:
 - function is created
 - function is properly formatted
 - function has positive and negative tests
 - all temporary files are removed after test run
You will learn:
 - how to test Exceptional cases
 - how to clean up after tests
 - how to check if file exists**
 - how to handle*** and raise**** exceptions in test. Use sample from the documentation.
* https://en.wikipedia.org/wiki/Interval_(mathematics)#Terminology
** https://docs.python.org/3/library/os.path.html
*** https://docs.python.org/3/tutorial/errors.html#handling-exceptions
**** https://docs.python.org/3/tutorial/errors.html#raising-exceptions
"""
import os


def read_magic_number(path: str) -> bool:
    if os.path.exists(path):
        with open(path, "r") as fi:
            first_line = fi.readline()
            try:
                digit = float(first_line)
            except Exception as exc:
                raise ValueError(
                    f"line can't be transformed to float. line: '{first_line}'"
                )
            else:
                return 1 <= digit < 3
    else:
        raise FileNotFoundError(f"No such file or directory: {path}")
