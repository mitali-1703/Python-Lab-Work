#Write a python function that accepts a string and calculates the no. of uppercase and
# lowercase letters.

def count(str):
    u,l=0,0
    for i in range(len(str)):
       if str[i]>="A" and str[i]<="Z" : u+=1
       elif str[i]>="a" and str[i]<="z" : l+=1
    return u,l

s=input("Enter a string:")
upper,lower=count(s)
print("\nUppercase characters:",upper)
print("Lowercase characters:",lower)