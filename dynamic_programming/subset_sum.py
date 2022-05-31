#use visited as set
#use table to memoized


def solution(array, ammount):
    table = {0: True}
    def recur(ammount, visited):
        if ammount in table:
            return table[ammount]
        v = False
        for i in range(len(array)):
            if array[i] not in visited and array[i] <= ammount:
                new_visited = visited.copy()
                new_visited.add(array[i])
                v = recur(ammount - array[i], new_visited)
                print(v)
                if v:
                    print(table)
                    table[ammount] = v
                    return v
        table[ammount] = v
        return v
    return recur(ammount, set())
        
print(solution([2,5,7,8,9],21))                   

