# *3 If statments
is_male = True

if is_male:  # it will print this if() statment if the condition is true
    print("You are a male")
else:  # it wwill print this else condition if its not true or by deafult
    print("You are not a male")


is_male2 = True
is_tall = False

if is_male2 or is_tall:  # it will print this if() statment if one of the conditions is true
    print("You are a male or tall or both")
else:  # it will print this else condition if its not true or by deafult
    print("You are neither a male or tall !!")

a = 5
b = 5
if a and b < 1:  # it will print this if() statment if both of the conditions is true
    print("a and b is bigger than one")
else:  # it will print this else condition if its not true or by deafult
    print("one of a and b is not bigger than one")

# if the both conditions are true so it perform the first if statment and so on
# nested if() statments
num1 = 20
num2 = 20
if num1 and num2 > 10:
    print("num1 and num2 is bigger than 10")
    if num1 and num2 >= 20:
        print("num1 and num2 is bigger than 20 or equal to 20")
        if num1 and num2 >= 30:
            print("num1 and num2 is bigger than 30")
        else:
            print("num1 and num2 is not bigger than 30")
