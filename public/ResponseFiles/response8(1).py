

def check_duplicate_letters(sentence): 
  words = sentence.split() 
  for word in words: 
    if len(word) > 1: 
      for i in range(len(word) - 1): 
        if word[i] == word[i+1]: 
          return True 
  return False