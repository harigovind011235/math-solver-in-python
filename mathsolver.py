import math

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))


z= math.sqrt((b**2)-(4 * a * c))

print(z)

result = lambda a , b, c ,z  : (-b+z)/(2*a)
result1 = lambda a , b, c, z : (-b-z)/(2*a)

print(result(a,b,c,z))
print(result1(a,b,c,z))
