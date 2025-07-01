column = 6
row = 4

for i in range(column):
    for j in range(row):
        if i == 1: 
            print("*", end=" ")
        else:
            print("")

    print()