#Display fibonacci series upto 10 terms using loop.

num=10
a=-1
b=1
c=0
for i in range(0,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
