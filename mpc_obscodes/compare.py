
import argparse
import hashlib
import sys

def compare_md5(md5_hash, file):
    """
    Compares the MD5 hash of the given file to the given MD5 hash.

    Parameters
    ----------
    md5_hash : str
        The MD5 hash to compare to.
    file : str
        The path to the file.

    Returns
    -------
    bool
        True if the MD5 hashes match, False otherwise.
    """
    with open(file, "rb") as f:
        contents = f.read()
        return md5_hash == hashlib.md5(contents).hexdigest()
    
if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser(
        description="Compares the MD5 hash of the given file to the given MD5 hash."
    )
    parser.add_argument("md5_hash", help="The MD5 hash to compare to.")
    parser.add_argument("file", help="The path to the file.")
    args = parser.parse_args()

    if compare_md5(args.md5_hash, args.file):
        print("MD5 hashes match.")
        sys.exit(0)
    else:
        print("MD5 hashes do not match.")
        sys.exit(1)
