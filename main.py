import os, time, numpy as np
import random as rd

boardL1 =np.array([[" ", " "," "],
[" ", " "," "],
[" ", " "," "]])
gamerun=True
def draw(x,y,mark):
    key= True
    while key:
        if boardL1[x][y]!= " ":
            if mark == 'x':
                x,y=map(int, input("Chosen position has already been occuped, input again another position: ").split(","))
            else:
                x,y= rd.randint(0,2),rd.randint(0,2)
        else:
            boardL1[x][y]=mark
            key=False
    return boardL1
def verify():
    i,j=0,0
    while j<=2:
        if boardL1[i][j]=="x" and boardL1[i+1][j]=="x" and boardL1[i+2][j]=="x":
            return True
        elif boardL1[i][j]=="o" and boardL1[i+1][j]=="o" and boardL1[i+2][j]=="o":
            return False
        else:
            i=0
            j+=1
    j=0
    while i<=2:
        if boardL1[i][j]=="x" and boardL1[i][j+1]=="x" and boardL1[i][j+2]=="x":
            return True
        elif boardL1[i][j]=="o" and boardL1[i][j+1]=="o" and boardL1[i][j+2]=="o":
            return False
        i+=1
    if boardL1[0][0]=="x" and boardL1[1][1]=="x" and boardL1[2][2]=="x":
        return True
    elif boardL1[0][0]=="o" and boardL1[1][1]=="o" and boardL1[2][2]=="o":
        return False
    elif boardL1[0][2]=="x" and boardL1[1][1]=="x" and boardL1[2][0]=="x":
        return True
    elif boardL1[0][2]=="o" and boardL1[1][1]=="o" and boardL1[2][0]=="o":
        return False

#to make the competitive game(npc and p2)
os.system('cls')
while gamerun:
    print(boardL1)
    c='x'
    row,colum= map(int, input().split(","))
    draw(row,colum,c)
    
    time.sleep(.7)
    os.system('cls')
    c='o'
    draw(rd.randint(0,2),rd.randint(0,2),c)
    if verify()== True:
        gamerun=False
        print(boardL1)
        print("you won")
    elif verify()== False:
        gamerun=False
        print(boardL1)
        print(" u lose ")
    if " " not in boardL1 and gamerun==True:
        print(boardL1)
        print("Draw")
        break


