import os

import pytest

from ..fetch import check_json_loads


def test_check_json_loads():
    # Test the check JSON function correcly loads a JSON file.
    with open("test.json", "w") as f:
        json_string = """{\n    "test" : 1\n}"""
        f.write(json_string)

    check_json_loads("test.json")

    # Test the check JSON function correcly loads an invalid JSON file.
    with open("invalid_test.json", "w") as f:
        json_string = """{\n    "test" : 1\n"""
        f.write(json_string)

    with pytest.raises(Exception):
        check_json_loads("invalid_test.json")

    os.remove("test.json")
    os.remove("invalid_test.json")
