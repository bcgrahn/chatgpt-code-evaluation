

import re

def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False

# Usage
s = '^[0-9]*$'
print(is_valid_regex(s)) # True