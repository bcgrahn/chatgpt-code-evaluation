

def isPalindrome(S): 
    if len(S) == 0: 
        return True
    else: 
        if S[0] == S[-1]: 
            return isPalindrome(S[1:-1]) 
        else: 
            return False
  
# Driver code 
S = "malayalam"
ans = isPalindrome(S) 
  
if ans: 
    print("Yes") 
else: 
    print("No")