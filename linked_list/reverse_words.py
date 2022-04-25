#hold the positions of the words
#and recreate the words

def reverse_words(arr):
  res = []
  i = len(arr)
  j = len(arr) - 1
  while j > -1:
    if arr[j] == " ":
      print(j)
      res += arr[j + 1: i]
      if i > 0: 
        res.append(" ")
      i = j - 1
    j -= 1
  print(res)
  res += arr[0:i+1]
  return res

#space = o (1)
#time  = o (n)


def reverse_words(arr):
  res = []
  i = len(arr)
  j = len(arr) - 1
  while j > -1:
    if arr[j] == " ":
      print(j)
      res += arr[j + 1: i]
      res.append(" ")
      i = j
    j -= 1
  if i > 0:
    res += arr[0:i]
  return res


print(reverse_words(['p', 'e', 'r', 'f', 'e', 'c', 't', ' ','m', 'a', 'k', 'e', 's', ' ','p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]))
