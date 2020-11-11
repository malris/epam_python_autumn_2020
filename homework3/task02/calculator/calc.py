import concurrent.futures
import hashlib
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def sum_slow_calculations():
    numbers_to_calculate = [i for i in range(500)]
    with concurrent.futures.ProcessPoolExecutor(max_workers=50) as executor:
        total_sum = sum(
            int(calc_res)
            for calc_res in executor.map(slow_calculate, numbers_to_calculate)
        )
    return total_sum
