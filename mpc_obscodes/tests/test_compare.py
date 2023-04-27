
import hashlib
import os 

from ..compare import compare_md5

def test_compare_md5():

    with open("test.txt", "w") as f:
        f.write("md5 test 123")

    md5_hash = hashlib.md5("md5 test 123".encode("utf-8")).hexdigest()

    assert compare_md5(md5_hash, "test.txt")

    with open("test2.txt", "w") as f:
        f.write("md5 test 1234")

    assert not compare_md5(md5_hash, "test2.txt")

    os.remove("test.txt")
    os.remove("test2.txt")