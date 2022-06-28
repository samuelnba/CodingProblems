def isSubsequence(s, t):
    for i in s:
        found = False
        for j in range(len(t)):
            if t[j] == i:
                t = t[j+1:]
                found = True
                break
        if found == False:
            return False
    return True
print(isSubsequence(s = "abc", t = "ahbgdc"))