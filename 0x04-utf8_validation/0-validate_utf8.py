#!/usr/bin/python3
""" UTF-8 encoding validator """
from typing import List


def validUTF8(data: List[int]):
    """
    determines if a given data set represents a valid UTF-8 encoding

    Argument:
    data: list of integers
    """
    count = 0

    for bit in data:
        # Array element must be an integer
        if not isinstance(bit, int):
            return False
        # When integer is not in the range of valid integers
        if bit < -255 or bit >= 255:
            return False
        # Convert each integer to its binary format
        bin_num = format(bit, "b").zfill(8)
        if bin_num[0] == '1' and bin_num[1] == '0':
            return False
        # Get the first leading 1's
        byte_len = (bin_num.split('0', 1))[0]
        if byte_len:
            # Getting the length of the total bytes for the character
            byte_len = len(byte_len)
            if byte_len > 4:
                return False
            # If we have a length of byte beyond the length of the array
            if count + byte_len > len(data):
                return False
            # Getting the bytes/integers from the data array
            next_array = data[count + 1: byte_len + count]
            # Iterate through the new array representing the character
            for j in next_array:
                ch_bin = format(j, "b").zfill(8)
                if ch_bin[0] != "1" or ch_bin[1] != "0":
                    return False
            count += byte_len
        else:
            count += 1
    return True
