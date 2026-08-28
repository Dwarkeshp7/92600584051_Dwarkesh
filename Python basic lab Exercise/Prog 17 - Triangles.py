# Write Python Programs to print following triangles.
"""
    
1
12
123
1234
12345  

"""
print("-----1-----")

for i in range(1,6):
    print()
    for x in range(1,i+1):
        print(x,end="")
        
"""
1
21
321
4321
54321
"""

print("\n\n-----2-----")

for i in range(1,6):
    print()
    for x in range(i,0,-1):
        print(x,end="")

"""
5
45
345
2345
12345
"""

print("\n\n-----3-----")

for i in range(5,0,-1):
    print()
    for j in range(i,6):
        print(j,end="")

"""
12345
2345
345
45
5
"""

print("\n\n-----4-----")

for i in range(1,6):
    for j in range(i,6):
        print(j,end="")

    print()

"""
5
54
543
5432
54321
"""

print("-----5-----")

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end="")

    print()

"""
12345
1234
123
12
1
"""
print("-----6-----")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")

    print()

"""
54321
5432
543
54
5
"""

print("-----7-----")

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end="")

    print()

"""
54321
4321
321
21
1
"""
print("-----8-----")

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")

    print()

"""
1
23
456
78910
…… n
"""

print("-----9-----")

n = int(input("Enter n : "))
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(num,end="")
        num = num + 1
        
    print()

"""
1
10
101
1010
10101
"""

print("-----10-----")

for i in range(1,6):
    for j in range(1,i+1):
        if j % 2 != 0:
            print(1,end="")
        else:
            print(0,end="")
    print()

"""
1
01
010
1010
10101
"""

print("-----11-----")

temp = 0
for i in range(1,6):
    for j in range(i):
        if temp == 0:
            print("1",end="")
            temp = 1
        else:
            print("0",end="")
            temp = 0
        
    print()

"""
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
"""

print("-----12-----")

n = 5
for i in range(1,n+1):
    print(" " * (2 * (n - i)),end="")

    for j in range(i,0,-1):
        print(j,end=" ")

    for j in range(2,i + 1):
        print(j,end=" ")

    print()

"""
*
**
***
****
*****
"""

print("-----13-----")

for i in range(1,6):
    for j in range(i):
        print("*",end="")

    print()

"""
    *
   **
  ***
 ****
*****

print("-----14-----")

for i in range(1,6):
    for j in range():
        print()

    print()

    """


"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

print("-----15-----")

rows = 5
for i in range(1,rows + 1):

    print(" " * (rows-i) + "* " * i)

