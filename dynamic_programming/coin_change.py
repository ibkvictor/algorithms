#[1, 2, 5, 10]

#least number of coins
#input = int, 10 ^ 4
#output = number of coins , int

#                11 amount
#             1, 6,      9, 10 while i< amount
#            0  1, 4, 5  4, 7, 8

#Naive: subproblem of with a remainder find min return value of all recursive possible remainder  O(k ^ n) - exponential, space O(1)
#possible remainder = n - i if i in coins is <= prev_remainder
#return 1 + max up to root call.

#Optimzed: store up subproblems O(k * n) - polynomial or linear in the sense that k = 4

import math
def solution(array, ammount):
    table = {k:1 for k in array}
    table[0] = 0
    def recur(ammount):
        if ammount in table:
            return table[ammount]
        v = math.inf
        for i in range(coins):
            if coins[i] <= ammount:
               v = min(v, recur(ammount - coins[i])) + 1
        table[ammount] = v
        return v
    return recur(ammount)

print(solution([1,2,5,10], 10))
