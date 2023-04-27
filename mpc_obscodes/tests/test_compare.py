import os

import pytest

from ..compare import calculate_md5, compare_md5


@pytest.fixture
def test_file1():
    """
    Generate a simple test file which has the following
    md5 checksum:

    md5sum test.txt
    e23f81dccb6fabea176468dec8b493bb  test.txt
    """
    with open("test.txt", "w") as f:
        f.write("md5 test 123")

    yield "test.txt"

    os.remove("test.txt")


@pytest.fixture
def test_file2():
    """
    Generate a simple test file which has the following
    md5 checksum:

    md5sum test2.txt
    4e934a3798b6f06f8d826325c00eaa09  test2.txt
    """
    with open("test2.txt", "w") as f:
        f.write("md5 test 1234")

    yield "test2.txt"

    os.remove("test2.txt")


def test_compare_md5(test_file1, test_file2):
    assert not compare_md5(test_file1, test_file2)
    assert compare_md5(test_file1, test_file1)
    assert compare_md5(test_file2, test_file2)


def test_calculate_md5(test_file1, test_file2):
    assert calculate_md5(test_file1) == "e23f81dccb6fabea176468dec8b493bb"
    assert calculate_md5(test_file2) == "4e934a3798b6f06f8d826325c00eaa09"
    assert calculate_md5(test_file1) != calculate_md5(test_file2)
