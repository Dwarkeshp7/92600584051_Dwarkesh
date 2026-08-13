#2. Write a program to illustrate the use of different data types and type casting.
"""
Numeric data types: int, float, complex
String  data types: str
    Sequence types: list, tuple, range
Mapping data  type: dict
      Boolean type: bool
    Set data types: set
"""

a = 26
print("The Type of",a,"is : ",type(a))

b = 26.25
print("The Type of",b,"is : ",type(b))

c = 26+4j
print("The Type of",c,"is : ",type(c))

d = "Dwarkesh"
print("The Type of",d,"is : ",type(d))

e = [1,2,3,4,5]
print("The Type of",e,"is : ",type(e))

f = (1,2,3,4,5)
print("The Type of",f,"is : ",type(f))

g = {1:"Dwarkeh",2:"Parmar","age":20}
print("The Type of",g,"is : ",type(g))

h = range(1,6)
print("The Type of",h,"is : ",type(h))

i = {"Dwarkesh",26,51,"Parmar"}
print("The Type of",i,"is : ",type(i))

j = True
print("The Type of",j,"is : ",type(j))
