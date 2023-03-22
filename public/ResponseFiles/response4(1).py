

def isPalindrome(s): 
    # Using slicing to reverse the string 
    rev = s[::-1] 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")