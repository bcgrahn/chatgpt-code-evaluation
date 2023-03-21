

import re 

def is_valid_regex(s): 
    try: 
        re.compile(s) 
        return True 
    except re.error: 
        return False

# Driver code 
s = '^[a-z0-9]+$'

if is_valid_regex(s): 
    print("Valid Regex") 
else: 
    print("Invalid Regex")