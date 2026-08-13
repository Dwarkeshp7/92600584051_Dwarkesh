"""9. Write a program to define and use user-defined functions with different types of arguments."""

def add_numbers(a, b):
  return a + b

def greet(name, message="Hello"):
  return message,name

def describe_pet(pet_name, animal_type):
  return "I have a " ,animal_type, "named", pet_name

def print_scores(student_name, *scores):
  total = sum(scores)
  return student_name ,"got a total score of" ,total

if __name__ == "__main__":
  
  sum_result = add_numbers(5, 10)
  print("Positional Sum:", sum_result)

  print(greet("Dwarkesh"))
  print(greet("Dwarkesh", "Good morning"))

  print(describe_pet(animal_type="dog", pet_name="Buddy"))

  print(print_scores("Dwarkesh", 85, 90, 95))
