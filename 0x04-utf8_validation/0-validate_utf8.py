#!/usr/bin/python3

def validUTF8(data):
    """ Method to validate UTF-8 encoding
    based on a given data set """
    for byte in data:
        num = []
        exp = 1
        while exp:
            exp >>= 1
            num.append(bool(data & exp))
        return num
