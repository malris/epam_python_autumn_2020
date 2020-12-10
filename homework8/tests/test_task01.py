import tempfile

import pytest
from homework8.task01.task01 import KeyValueStorage


def with_temp_file(content):
    def create_temp_file(f):
        def wrapped(*args, **kwargs):
            with tempfile.NamedTemporaryFile(mode="w+t") as file:
                file.write(content)
                file.flush()
                return f(file.name, *args, **kwargs)

        return wrapped

    return create_temp_file


@with_temp_file("last_name=top power=9001")
def test_transform_content_to_dict_pair(path_to_file: str):
    kv_storage = KeyValueStorage(path_to_file)
    assert kv_storage.data_dict == {"last_name": "top", "power": 9001}


@with_temp_file("last_name=top power=9001\npower=max")
def test_access_items_as_attributes(path_to_file: str):
    kv_storage = KeyValueStorage(path_to_file)
    assert kv_storage.last_name, kv_storage.power == ("top", 9001)


@with_temp_file("last_name=top power=9001\npower=max")
def test_access_items_as_collection(path_to_file: str):
    kv_storage = KeyValueStorage(path_to_file)
    assert kv_storage["last_name"], kv_storage["power"] == ("top", 9001)


@with_temp_file("1=top power=9001")
def test_invalid_key_raises_value_error(path_to_file: str):
    with pytest.raises(ValueError, match="invalid key to be assigned to an attribute"):
        kv_storage = KeyValueStorage(path_to_file)
