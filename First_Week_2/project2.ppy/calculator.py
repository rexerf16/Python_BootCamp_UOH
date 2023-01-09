# *5 Building a Complex Calculator

op = """
1)+
2)-
3)*
4)/
choose one of the opreations : """


def plus():
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the secand number : "))
    pr = num1+num2
    print(str(num1)+" + "+str(num2)+" = "+str(pr))


def sub():
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the secand number : "))
    sr = num1-num2
    print(str(num1)+" - "+str(num2)+" = "+str(sr))


def mult():
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the secand number : "))
    mr = num1*num2
    print(str(num1)+" * "+str(num2)+" = "+str(mr))


def div():
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the secand number : "))
    dr = num1/num2
    print(str(num1)+" / "+str(num2)+" = "+str(dr))


ans = input(op)
if ans == '1':
    plus()
elif ans == '2':
    sub()
elif ans == '3':
    mult()
elif ans == '4':
    div()
