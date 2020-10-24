#Write a loop to find factorial of any number.

num=int(input("Enter a number:"))
f=1
for i in range(num,0,-1):
    f=f*i
print("Factorial of the entered no. is",f)