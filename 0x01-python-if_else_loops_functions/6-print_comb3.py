#!/usr/bin/python3


for a in range(0, 10):
    for b in range(a, 10):
        if a != b:
            if a < 8:
                print("{:d}{:d}".format(a, b), end='\n')
            else:
                print("{:d}{:d}".format(a, b), end='\n')

