#!/usr/bin/python
import sys

try:
    f = open(str(sys.argv[1]), 'r')
    print(str(f.read()))
finally:
    if f:
        f.close()