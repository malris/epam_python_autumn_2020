import pytest
from homework4.task02.mock_input import count_dots_on_i


def mocked_urlopen(*args):
    class MockResponse:
        def __init__(self, text="", status_code=200):
            self.text = text
            self.status_code = status_code

    if args[0] == "https://mock-existing-site.com/":
        html_data = """<html><body><p>This is a paragraph.</p><p>This is a paragraph.</p><p id="p01">I am different.</p></body></html>"""
        return MockResponse(html_data, 200)
    else:
        return MockResponse("", 200)


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("https://mock-existing-site.com/", 6), ("https://mock-existing-site1.com/", 0)],
)
def test_count_dots_on_i_works_properly(value: str, expected_result: int, mocker):
    mocker.patch("homework4.task02.mock_input.requests.get", side_effect=mocked_urlopen)
    assert count_dots_on_i(value) == expected_result


def test_count_dots_on_i_raises_value_error(mocker):
    mocker.patch("homework4.task02.mock_input.requests.get", side_effect=Exception())
    with pytest.raises(ValueError, match="Unreachable"):
        count_dots_on_i("https://example.com/nonexisted-page")


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [("http://ya.ru/", 3686), ("https://example.com/", 59)],
)
def test_count_dots_on_i_real_website(value: str, expected_result: int):
    assert count_dots_on_i(value) == expected_result
