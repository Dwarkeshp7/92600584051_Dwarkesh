"""5. Write a program to demonstrate the use of break continue and pass statements."""

for i in range(1,6):
    if i == 4:
        break
    print(i)

print("------------------------------")

for num in range(1,6):
    if num % 2 == 0:
        #print(num,"is even so skip this")
        continue
    print(num)

print("------------------------------")

for number in range(1,6):
    if number == 3:
        pass
        #print("This Line Still Print")
    print(number)