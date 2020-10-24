#Count all lowercase,uppercase,digits and special symbols from a given string.

def count(str):
    lower,upper,digit,special=0,0,0,0
    for i in range(len(str)):
        if str[i]>="a" and str[i]<="z" : lower+=1
        elif str[i]>="A" and str[i]<="Z" : upper+=1
        elif str[i]>="0" and str[i]<="9" : digit+=1
        else: special+=1
    return lower,upper,digit,special

str=input("Enter a string:")
l,u,d,s=count(str)
print("\nLower case characters:",l)
print("Upper case characters:",u)
print("No. of digits:",d)
print("Special case characters:",s)