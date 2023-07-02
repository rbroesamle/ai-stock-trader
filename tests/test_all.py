import sys
from io import StringIO


def test():
    print("HALLO")
    sys.path.append(".")
    exec(open("./main.py").read())
