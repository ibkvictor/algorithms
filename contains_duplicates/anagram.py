def anagram(s, t):
	if len(s) != len(t):
        	return False
        table1 = {}
        for ch in t:
                if ch not in table1:
                    table1[ch] = 1
                else:
                    table1[ch] += 1
        table2 = {}
        for ch in s:
                if ch not in table2:
                    table2[ch] = 1
                else:
                    table2[ch] += 1
        if table1 == table2:
            return True
        return False

s = "rat"
t = "car"
print(anagram(s,t))

