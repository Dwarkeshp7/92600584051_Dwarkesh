# (20) Write a Python Program to perform 3x3 matrix multiplication.

a = []
b = []
c = [[0,0,0],[0,0,0],[0,0,0]]

print("Enter First Matrix:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    a.append(row)

print("Enter Second Matrix:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    b.append(row)

for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j] = c[i][j] + a[i][k] * b[k][j]

print("Result Matrix:")
for i in range(3):
    print(c[i])

""" 
First Matrix

1 2 3
4 5 6
7 8 9

Second Matrix

9 8 7
6 5 4
3 2 1

Output

[30, 24, 18]
[84, 69, 54]
[138, 114, 90]
"""