from ..compare import calculate_md5


def test_mpc_obscodes():
    from mpc_obscodes import mpc_obscodes

    assert mpc_obscodes.is_file()


def test__mpc_obscodes_md5():
    from mpc_obscodes import _mpc_obscodes_md5

    assert _mpc_obscodes_md5.is_file()


def test__mpc_obscodes_md5_matches():
    from mpc_obscodes import _mpc_obscodes_md5, mpc_obscodes

    # Read the MD5 hash from the file that comes with the
    # package
    with open(_mpc_obscodes_md5.as_posix(), "r") as f:
        md5_hash = f.read().split()[0]

    # Compare to the MD5 calculated from the mpc_obscodes file
    assert calculate_md5(mpc_obscodes.as_posix()) == md5_hash
