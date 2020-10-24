#Write a program to multiply all items in a list.

list=[]
num=int(input("Enter no. of elements in list:"))
for i in range(1,num+1):
    ele=int(input("Enter the element of list:"))
    list.append(ele)

mul=1
for i in range(1,len(list)+1):
    mul=mul*i

print("Product of all elements of list is",mul)
