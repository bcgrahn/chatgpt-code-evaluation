

import re

def is_valid_regex(S):
    try:
        re.compile(S)
        return True
    except re.error:
        return False

# example
S = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'
print(is_valid_regex(S)) # True