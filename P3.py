#Write a program to calculate area of triangle using Heron's Formula.

print("Enter the 3 sides of a triangle")
a=int(input())
b=int(input())
c=int(input())
s=int((a+b+c)/2)
print("The area of the triangle by Heron's formula is",int((s*(s-a)*(s-b)*(s-c))**0.5))

# OUTPUT
# Enter the 3 sides of a triangle
# 3
# 4
# 5
# The area of the triangle by Heron's formula is 6
