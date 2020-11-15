from homework4.task03.get_print_output import my_precious_logger


def test_my_precious_logger_writes_to_stdout(capfd):
    my_precious_logger("OK")
    out, err = capfd.readouterr()
    assert out == "OK"


def test_my_precious_logger_writes_to_stderr(capfd):
    my_precious_logger("error: file not found")
    out, err = capfd.readouterr()
    assert err == "error: file not found"
