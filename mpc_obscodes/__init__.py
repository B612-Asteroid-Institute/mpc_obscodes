from importlib.resources import files

mpc_obscodes = files("mpc_obscodes").joinpath("obscodes_extended.json")
_mpc_obscodes_md5 = files("mpc_obscodes").joinpath("obscodes_extended.md5")
