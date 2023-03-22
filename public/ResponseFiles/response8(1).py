

def check_duplicate_letters(sentence):
  words = sentence.split()
  for word in words:
    for letter in word:
      if word.count(letter) > 1:
        return True
  return False