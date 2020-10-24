#Write a recursive function to display Fibonacci series upto N terms.

def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fib(n-2)+fib(n-1)

num=int(input("Enter a number:"))
print("The fibonacci series upto",num,"terms is:")
for i in range(num+1):
    print(fib(i),end=" ")

