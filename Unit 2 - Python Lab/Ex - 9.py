"""9. Write a program to demonstrate iterators and iterables in Python."""

listnum = [10,20,30]

print(hasattr(listnum,"__iter__"))

listnum2 = iter(listnum)

print(next(listnum2))
print(next(listnum2))
print(next(listnum2))