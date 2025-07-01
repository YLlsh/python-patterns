column = 6
row = 1
space = 4

for i in range(column):

    for k in range(space):
        print(" ",end="")

    for j in range(row):
        print("*",end=" ")

    print()
    row += 1
    space -= 1