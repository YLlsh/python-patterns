column = 5
row = 1
space =4

for i in range(column):

    for k in range(space):
        print(" ",end="")
    for j in range(row):
        print(i+1,end="")

    print()
    space -= 1
    row +=1