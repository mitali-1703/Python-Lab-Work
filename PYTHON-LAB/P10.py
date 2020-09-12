#Write a program to calculate average of two numbers and also print their deviation.

num1=int(input("Enter first no.\n"))
num2=int(input("Enter second no.\n"))
avg=int((num1+num2)/2)
print("The average of these 2 nos. is",avg)
d1=(avg-num1)
print("The deviation of num1 from average is",d1)
d2=(avg-num2)
print("The deviation of num2 from average is",d2)
