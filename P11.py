#Given 2 integers;return their product and if product is greater than 1000,then return sum.

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if(num1*num2>1000):
    print("Product of the numbers is",num1*num2)
else:
    print("Sum of the numbers is",num1+num2)
