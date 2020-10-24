#Write a program to print sum of all numbers in a list.

list=[30,6,14,0,9]
sum=0
for i in range(len(list)):
    sum=sum+list[i]

print("The sum of all numbers in list is:",sum)