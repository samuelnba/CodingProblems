def judgeCircle(moves):
    move = [0, 0, 0, 0]
    for i in moves: 
        if i == "U":
            move[0] += 1
        elif i == "D":
            move[1] += 1
        elif i == "L":
            move[2] += 1
        else: 
            move[3] += 1
    if move[0] - move[1] == 0 and move[2] - move[3] == 0:
        return True
    else: 
        return False
    
print(judgeCircle("LL"))