def check_power_of_2(a: int) -> bool:
    return bool(a) and (not (bool(a & (a - 1))))
