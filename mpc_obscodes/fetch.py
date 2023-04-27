import argparse
import gzip
import hashlib
import json
import os
import shutil

import requests

URL = "https://minorplanetcenter.net/Extended_Files/obscodes_extended.json.gz"
FILE_COMPRESSED = os.path.join(os.path.dirname(__file__), "obscodes_extended.json.gz")
FILE_DECOMPRESSED = os.path.join(os.path.dirname(__file__), "obscodes_extended.json")
MD5_FILE = os.path.join(os.path.dirname(__file__), "obscodes_extended.md5")


def fetch_file(url: str, output_file: str):
    """
    Fetches the file from the given URL and saves it to the output file.

    Parameters
    ----------
    url : str
        The URL to fetch the file from.
    output_file : str
        The path to the output file.

    Raises
    ------
    Exception
        If the status code of the response is not 200.
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch file from {url}. Status code: {response.status_code}"
        )
    with open(output_file, "wb") as f:
        f.write(response.content)


def decompress_gz_file(gz_file: str, output_file: str):
    """
    Decompresses a gzipped file and saves it to the output file.

    Parameters
    ----------
    gz_file : str
        The path to the gzipped file.
    output_file : str
        The path to the output file.
    """
    with gzip.open(gz_file, "rb") as f_in:
        with open(output_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def store_md5_hash(file: str, output_file: str):
    """
    Stored the MD5 hash of the given file to the output file.

    Parameters
    ----------
    file : str
        The path to the file.

    Returns
    -------
    str
        The MD5 hash of the file.
    """
    with open(file, "r") as f:
        contents = f.read().encode("utf-8")
        with open(output_file, "w") as f_out:
            f_out.write(
                hashlib.md5(contents).hexdigest() + "  " + os.path.basename(file)
            )


def check_json_loads(file):
    """
    Checks if the JSON file loads.

    Parameters
    ----------
    file : str
        The path to the file.

    Raises
    ------
    Exception
        If the file does not load correctly.
    """
    try:
        with open(file, "r") as f:
            json.load(f)
    except Exception as e:
        raise Exception(f"Failed to load file {file}. Error: {e}") from e


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fetch MPC observatory code file, decompress it and check if it loads."
    )
    parser.add_argument(
        "--url",
        type=str,
        default=URL,
        help="URL to fetch the MPC observatory code file from.",
    )
    parser.add_argument(
        "--compressed_file",
        type=str,
        default=FILE_COMPRESSED,
        help="Path where to save compressed file.",
    )
    parser.add_argument(
        "--decompressed_file",
        type=str,
        default=FILE_DECOMPRESSED,
        help="Path where to save decompressed file.",
    )
    parser.add_argument(
        "--md5_file",
        type=str,
        default=MD5_FILE,
        help="Path where to save MD5 hash file.",
    )
    args = parser.parse_args()

    fetch_file(args.url, args.compressed_file)
    decompress_gz_file(args.compressed_file, args.decompressed_file)
    check_json_loads(args.decompressed_file)
    store_md5_hash(args.decompressed_file, args.md5_file)
