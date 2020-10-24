#Write a function calculation() which accepts 2 variables and calculates their sum and
# difference in a single return call.

def calculation(x,y):
    sum=x+y
    diff=x-y
    return(sum,diff)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s,d=calculation(a,b)
print("The sum and difference of the numbers respectively is:",s,d)