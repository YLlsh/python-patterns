row = 7
column = 4

for i in range(row):
    if i == 0 or i == (row-1) :
        print("*" * column)
    else:
        print("*" + "  " + "*")