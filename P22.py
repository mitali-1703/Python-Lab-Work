#Write a python script to sort(ascending and descending) a dictionary by value.

a={"1":"12","2":"1","3":"0","4":"23","5":"57"}
print("The sorted values of dictionary in ascending order is:",sorted(a.values()))
print("The sorted values of dictionary in descending order is:",sorted(a.values(),reverse=True))