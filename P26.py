#Create a function showEmployee() which accepts employees' name and salary and displays
# both and if salary is missing in function call then it should display it as 9000.

def showEmployee(name,salary=9000):
        print("Employees' name is:",name)
        print("Employees' salary is:",salary)

user_name=input("Enter employees' name:")
user_salary=int(input("Enter employees' salary:"))
print("\nWhen salary is passed as an argument in function call:")
showEmployee(name=user_name,salary=user_salary)
print("\nWhen salary is not passed as an argument in function call:")
showEmployee(name=user_name)
