"""10.Write a program to generate a sequence of numbers using generator functions and yield keyword."""

def sequence_generator(start, end, step=1):
    current = start
    while current <= end:
        yield current 
        current = current + step 

numbers_sequence = sequence_generator(start=1, end=10, step=2)

for num in numbers_sequence:
    print(num)

manual_sequence = sequence_generator(start=100, end=105, step=2)
print(next(manual_sequence)) 
print(next(manual_sequence))
print(next(manual_sequence))