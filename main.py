import os, time, numpy as np
import sys
boardL1 =np.array([[" ", " "," "],
[".", ".","."],
[".", ".","."]])
os.system("cls")
def verify():
    i,j=0,0
    while j<=2:
        if boardL1[i][j]=="." and boardL1[i+1][j]=="." and boardL1[i+2][j]==".":
            print(i,j)
            i,j=0,0
            break
        else:
            i=0
            j+=1
    while j<=2:
        if boardL1[i][j]=="." and boardL1[i][j+1]=="." and boardL1[i][j+2]==".":
            print(i,j)
            i,j=0,0
            break
        if i==2:
            i=0
            j+=1
        i+=1
    
verify()
