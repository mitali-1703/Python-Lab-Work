#Write a python function that checks whether a passed string is palindrome or not.


def check(s):
        if s == s[::-1]:
            print("The passed string is a palindrome")

        else:
            print("The passed string is not a palindrome")

str=input("Enter a string:")
check(str)
