#Anonymous Love Letter

#You have written an anonymous love letter and you don’t want your handwriting to be recognized. Since you don’t have a printer within reach, you are trying to write this letter by copying and pasting characters from a newspaper.
#
#Given a string L representing the letter and a string N representing the newspaper, return true if the L can be written entirely from N and false otherwise. The letter includes only ascii characters
#



#newspaper

#love letter
def solution(letter, newspaper):
  table = {}
  for ch in newspaper:
    if ch in newspaper:
      table[ch] = 1
    else:
      table[ch] += 1
      
  for ch in letter:
    if ch in table:
      if table[ch] == 1:
        del table[ch]
      else:
        letter[ch] -= 1
    else:
      return False
  return True

n = "newspaper"
l = "letter"
print(solution(l, n))
