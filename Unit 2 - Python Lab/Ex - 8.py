"""8. Write a program to illustrate variable scope using local global and nonlocal variables."""

def my_fun1():
    local_var = "This is from Local"
    print(local_var)

my_fun1()

print("----------")

num = 10

def my_fun2():
    print("Global Inside Function :",num)

my_fun2()
print("Global outside Functino :",num)

print("----------")

def my_fun3():
    msg = "Hello From Outer"

    def my_fun4():
        nonlocal msg
        msg = "Hello From Inner"

    my_fun4()
    print(msg)

my_fun3()
