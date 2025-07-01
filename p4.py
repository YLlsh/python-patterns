column =5 
row = 1
value = 12

for i in range(column):
    for j in range(row):
        print(f'{value}',end=" ")
        value -= 2

    print()
    row += 1
    value =12