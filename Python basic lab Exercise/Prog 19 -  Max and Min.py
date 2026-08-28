# (19) Write a Python Program to enter 10 nos. and find max1,max2,max3 and min1,min2 and min3 

num = []

for i in range(10):
    n = int(input("Enter Number : "))
    num.append(n)

num.sort()

print(num)

print("Min 1 : ", num[0])
print("Min 1 : ", num[1])
print("Min 3 : ", num[2])
print("Max 1 : ", num[9])
print("Max 2 : ", num[8])
print("Max 3 : ", num[7])