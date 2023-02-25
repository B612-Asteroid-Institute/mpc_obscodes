import importlib.resources

mpc_obscodes = importlib.resources.files("mpc_obscodes").joinpath(
    "obscodes_extended.json"
)
