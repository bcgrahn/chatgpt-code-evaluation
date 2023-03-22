.

def palindrome(string):
  revStr = string[::-1]
  if string == revStr:
    return True
  else:
    return False