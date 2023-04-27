from ..compare import compare_md5

def test_mpc_obscodes():
    from mpc_obscodes import mpc_obscodes

    assert mpc_obscodes.is_file()

def test__mpc_obscodes_md5():
    from mpc_obscodes import _mpc_obscodes_md5

    assert _mpc_obscodes_md5.is_file()

def test__mpc_obscodes_md5_matches():
    from mpc_obscodes import mpc_obscodes, _mpc_obscodes_md5

    with open(_mpc_obscodes_md5.as_posix(), "r") as f:
        md5_hash = f.read().split()[0]

    assert compare_md5(md5_hash, mpc_obscodes.as_posix())