#!/usr/bin/python3
"""Utf8 Validation"""


def validUTF8(data):
    """
        :type data: List[int]
         :rtype: bool
    """
    count = 0
    for num in data:
        if count == 0:
            if num >> 5 == 0b110:
                count = 1
            elif num >> 4 == 0b1110:
                count = 2
            elif num >> 3 == 0b11110:
                count = 3
            elif not num >> 7 == 0b0:
                return False
        else:
            if not num >> 6 == 0b10:
                return False
            count -= 1
    return count == 0
