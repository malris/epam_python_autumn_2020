"""
Write down the function, which generates the filter object for specified keywords.

Function should return a Filter object with the list of single-argument functions
to detect all of entries of input list, that include all of the key-value pairs.

Examples of usage:
positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)))
positive_even.apply(range(100)) should return only even numbers from 0 to 99

sample_data = [
    {'name': 'Bill', 'occupation': 'was there', 'type': 'person'},
    {'name': 'polly', 'type': 'bird'}
]
make_filter(name='polly', type='bird').apply(sample_data) should return only th 2nd entry of sample_data
"""


class Filter(object):
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return (
            [item for item in data if all(i(item) for i in self.functions)]
            if self.functions
            else []
        )


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(lambda d, k=key, v=value: d.get(k) == v)
    return Filter(*filter_funcs)
