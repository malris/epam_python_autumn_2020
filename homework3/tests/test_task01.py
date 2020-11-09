from typing import Any, Sequence

import pytest
from homework3.task01.cache_wrapper import inp_func, power_func


@pytest.mark.parametrize(["arguments"], [([100, 200],), ((0, 0),), ((-10, 15),)])
def test_power_func_cached_2_times(arguments: Sequence[Any]):
    actual_result1 = power_func(*arguments)
    actual_result2 = power_func(*arguments)
    actual_result3 = power_func(*arguments)
    actual_result4 = power_func(*arguments)

    assert actual_result1 is actual_result2 is actual_result3 is not actual_result4


def test_inp_func_cached_2_times(pytestconfig):
    capture_manager = pytestconfig.pluginmanager.getplugin("capturemanager")
    capture_manager.suspend_global_capture(in_=True)

    actual_result1 = inp_func()
    actual_result2 = inp_func()
    actual_result3 = inp_func()
    actual_result4 = inp_func()

    capture_manager.resume_global_capture()
    assert actual_result1 is actual_result2 is actual_result3 is not actual_result4
