#!/usr/bin/python3
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only
    need to handle the 8 least significant bits of each integer
    """
    # Variable for counting number of bytes in UTF-8 Character
    number_bytes = 0

    # Masks for checking if byte is valid (Starts with 10)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if number_bytes == 0:
            # Count number of bytes the UTF-8 Character will have
            while mask & byte:
                number_bytes += 1
                mask = mask >> 1

            # If number of bytes did not increase then it has 1 byte
            # which is the same we are counting so no need to check next bytes
            # for current character
            if number_bytes == 0:
                continue

            # A character in UTF-8 can be 1 to 4 bytes long
            # But 1 byte characters start in 0 so number_bytes should never
            # be 1
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Every byte that is not the first byte of a character should start
            # with 10, otherwise is not valid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # If bytes of character are valid, then the count will decrease with
        # each byte until a new character starts
        number_bytes -= 1

    # All characters were verified correctly with their proper byte count
    return number_bytes == 0
