        if len(array) < 3:
                return []
        if len(array) == 3:
            if sum(array) != 0:
                return []
        array = sorted(array)
        result = set()
        table = dict()
        for i in range(len(array) - 1):
                for j in range(i+1, len(array)):
                        complement = 0 - array[i] - array[j]
                        if complement in table:
                                table[complement].add(tuple(sorted((i,j))))
                        else:
                                table[complement] = set()
                                table[complement].add(tuple(sorted((i,j))))

        for i in range(len(array)):
                if array[i] in table:
                        for pairs in table[array[i]]:
                                if i not in pairs:
                                        result.add(tuple(sorted((array[pairs[0]], array[pairs[1]], array[i]))))
        return result
