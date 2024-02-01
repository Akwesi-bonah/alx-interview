#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
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
    number_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:

        mask_n_byte = 1 << 7

        if number_bytes == 0:
            while mask_n_byte & i:
                number_bytes += 1
                mask_n_byte = mask_n_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:

            if not (i & mask1 and not (i & mask2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
