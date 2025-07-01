column = 5
row = 5
value = 5

for i in range(column):
    for j in range(row):
        print(f'{value}',end=" ")
        value-=1
    print()
    row -=1
    value = 5
