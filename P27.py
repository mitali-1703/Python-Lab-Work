#Write a function func1() which accepts a variable length of arguments and print all
#argument values.

def func1(*args):
    for item in args:
        print(item)
list=["Kartikey",5,"Google"]
func1(*list)