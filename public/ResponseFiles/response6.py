.

def palindrome(str):
  rev_str = str[::-1]
  if rev_str == str:
    return True
  else:
    return False

print(palindrome('bob')) # True
print(palindrome('abba')) # True
print(palindrome('abcd')) # False