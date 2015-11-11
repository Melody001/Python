#!/usr/bin/python


try:
    f = open('E:\shared\program\python\IO_test.txt', 'r')
    print(str(f.read()))
finally:
    if f:
        f.close()