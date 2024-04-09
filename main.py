# Check if Python is running as 32-bit or 64-bit

import sys

is_64bits = sys.maxsize > 2**32
print(is_64bits)

if is_64bits:
    print('Python is running as 64-bit application')
else:
    print('Python is running as 32-bit application')