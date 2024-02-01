# UTF-8 Validation

This module provides a method for checking whether a given data set represents a valid UTF-8 encoding.

## `validUTF8(data: List[int]) -> bool`

Method that determines if a given data set represents a valid UTF-8 encoding.

### Arguments

- `data` (List[int]): The data set to be checked. Each integer in the list represents 1 byte of data.

### Returns

- `bool`: `True` if the data is a valid UTF-8 encoding, `False` otherwise.

### Description

A character in UTF-8 can be 1 to 4 bytes long. The data set can contain multiple characters. The method checks whether the data set is a valid UTF-8 encoding by performing the following steps:

1. Count the number of bytes in each UTF-8 character.
2. Validate each byte in the data set based on the UTF-8 encoding rules.
3. If all characters are verified correctly with their proper byte count, return `True`. Otherwise, return `False`.

### Example

```python
data = [197, 130, 1]  # Represents the UTF-8 encoding of the character 'Ç'

result = validUTF8(data)
print(result)  # Output: True