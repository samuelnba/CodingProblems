def hasAlternatingBits(n):
    n = str(bin(n))
    n = n[2:]
    if n[0] == "0":
        temp = True
    else:
        temp = False
    for i in n:
        if i == "0" and temp == False:
            return False
        elif i == "1" and temp == True:
            return False
        temp = not temp
    return True
print(hasAlternatingBits(7))