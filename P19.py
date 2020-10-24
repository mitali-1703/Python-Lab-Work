#Given a string of odd length and greater than 7,return a string made of middle 3 chars
#of given string.

def middle_3_chars(s):
    middleIndex=int(len(s)//2)
    return s[middleIndex-1 : middleIndex+2]

str=input("Enter a string of odd length and greater than 7:")
print("String made up of middle 3 chars of the passed string is:",middle_3_chars(str))

