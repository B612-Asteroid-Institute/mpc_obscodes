import argparse
import hashlib
import sys


def calculate_md5(file):
    """
    Calculates the MD5 hash of the given file.

    Parameters
    ----------
    file : str
        The path to the file.

    Returns
    -------
    str
        The MD5 hash of the file.
    """
    with open(file, "rb") as f:
        contents = f.read()
        return hashlib.md5(contents).hexdigest()


def compare_md5(file1, file2):
    """
    Calculate and compare the MD5 hashes of the given files.

    Parameters
    ----------
    file1 : str
        The path to the first file.
    file2 : str
        The path to the second file.

    Returns
    -------
    bool
        True if the MD5 hashes match, False otherwise.
    """
    md5_hash1 = calculate_md5(file1)
    md5_hash2 = calculate_md5(file2)

    return md5_hash1 == md5_hash2


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Compares the MD5 hash of the given file to the given MD5 hash."
    )
    parser.add_argument("file1", help="The path to the first file.")
    parser.add_argument("file2", help="The path to the second file.")
    args = parser.parse_args()

    if compare_md5(args.file1, args.file2):
        print("MD5 hashes match.")
        sys.exit(0)
    else:
        print("MD5 hashes do not match.")
        sys.exit(1)
