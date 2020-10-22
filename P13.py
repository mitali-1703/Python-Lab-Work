#Reverse a given number and return true if it is same as the original number.

num=int(input("Enter a number:"))
r=0
temp=num
while(num!=0):
    a=num%10
    r=r*10+a
    num=num//10
print("Reverse:",r)
if(r==temp):
    print("True as reversed no. is same as the original no.")
else:
    print("False as reversed no. is not same as the original no.")