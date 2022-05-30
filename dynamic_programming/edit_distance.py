import math
def solution(word1, word2):
    def recur(i, j):
        v = math.inf
        if i < len(word1) and j < len(word2):
            if word1[i] != word2[j]:
                #insert
                v = min(v, recur(i , j + 1)) + 1
                #replace
                v = min(v, recur(i + 1, j + 1)) + 1
                #delete
                v = min(v, recur(i + 1, j)) + 1
            else:
                v = min(v, recur(i + 1, j + 1))
        elif j == len(word2) and i < len(word1):
            v = len(word1) - i + 1
        elif i == len(word1) and j < len(word2):
            v = len(word2) - i + 1
        else:
            v = 0
        return v
    return recur(0, 0)

print(solution("", "ros"))
