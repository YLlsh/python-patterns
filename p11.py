row = 3
colunm = 1
space = 2


for i in range(row):
    for s in range(space):
        print(" ",end="")
    space -=1   
    
    for j in range(colunm):
        if colunm <=5 :
            print("*",end="")
            
    colunm += 2
    print()
    
b = 3
space2 = 1
for i in range(2): 
    for s in range(space2):
        print(" ",end="")
    space2 += 1
    
    for j1 in range(b):
        print("*",end="")
    print()
    b -= 2