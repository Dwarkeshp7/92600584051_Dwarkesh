# Write python programs to Print following Loops :

# A. 1 2 3 4 …… 10

for i in range(1,11):
    print(i)

print("--------------------")

# B. 2 4 6 ……. 20

num = 2

while(num <=20 ):
    print(num)
    num = num + 2
    
print("--------------------")

# C. 1 3 5 7 …… 19

num = 1

while(num <= 19):
    print(num)
    num = num + 2

print("--------------------")

# D. 100 99 98…… 90

for i in range(100,89,-1):
    print(i)

print("--------------------")

# E. 200 198 196 …. 180

for i in range(200,179,-2):
    print(i)

print("--------------------") 

# F. 0 1 1 2 3 5 8 ….. n

n = int(input("Enter n : "))

a,b = 0,1

for i in range(n):
    print(a)
    a,b = b,a+b
    
print("--------------------")

# G. 1 + 2 + …… + 10 = ans

ans = sum(range(1,11))
 
print(ans)

print("--------------------")

# H. ½ + 2/3 + ¾ …… + 9/10 = ans

ans = 0

for i in range (1,10):
    ans = ans + i / (i+1)

print(ans)

print("--------------------")

# I. 1/10 + 2/20 ….. 10/100 = ans

ans = 0

for i in range(1,11):
    ans = ans + i / (i * 10)

print(ans)

print("--------------------") 
