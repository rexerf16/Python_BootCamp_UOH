# *4 If Statements & Comparisons
age = int(input("Enter Your age : "))
salary = int(input("Enter your salary :"))
if age >= 18 and salary >= 8000:  # it will perform the if() statment if the conditions
    print("the employee is 18 or older and his salary is 8000(SR) or more")
elif age >= 18 and salary <= 8000:
    print("the employee is 18 or older and his salary is lower than 8000(SR) ")
elif age < 18 and salary <= 8000:  # eilf() will check a new conditions if the if()
    print("The emplyee is younger than 18 and his salary is lower than 8000(SR)")
elif age < 18 and salary >= 8000:
    print("The emplyee is younger than 18 and his salary is 8000(SR) or more")
else:  # it will print this else condition if its not true or by deafult
    print("Error !!")
