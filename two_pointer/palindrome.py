import time
def isPalindrome(s):
    res = ''
    for ch in s:
        if ch.isalnum():
            print(ch)
            res += ch.lower()

    i = 0
    j = len(res) - 1
    while i <= j:
        if res[i] != res[j]:
            return False
        i += 1
        j -= 1
    print(i, j)
    print(res[i], res[j])
    return True

start = time.time()
s = "race a car" 
print(isPalindrome(s))
print(time.time() - start)