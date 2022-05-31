#memoized solution = table[(i, j)]
#subproblem = L(i,j) for all possible i and j
#relate = L(i, j) = 1 or 0 + max(L(n, m)) for n and m in range (0, 1)
#original = L(0,0)
#time = O(n*n)
#space = O(n*n)

import math
def solution(word1, word2):
    table = {}
    def recur(i, j):
        if (i, j) in table:
            return table[(i,j)]
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
        table[(i,j)] = v
        return v
    print(table)
    return recur(0, 0)

print(solution("horse", "ros"))
