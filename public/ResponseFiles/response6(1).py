.

def palindrome(string):
  # Reverse the string
  reverse_string = string[::-1] 
  
  # Check if the string is equal to its reverse
  if string == reverse_string:
    return True
  else:
    return False