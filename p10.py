row = 5
column = 5
space = 1

for i in range(row):
   # print("$\")
    for j in range(space):
        print(" ",end="")
    for j in range(column):
        print("*",end="")
    print() 
    column -=1   
    space += 1    
    