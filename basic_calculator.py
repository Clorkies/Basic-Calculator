print("HEllo, this is a Basic Calculator!\n---------------------")


def opmult():
    while ValueError:
        try:
            v1 = input(">> ")
            print("///// to be multiplied by /////")
            v2 = input(">> ")
            product = int(v1)*int(v2)
            return print(str(product) + " is the product")
        except ValueError:
            print("Please input a number")

def opdiv():
    while ValueError or ZeroDivisionError:
        try:
            v1 = int(input(">> "))
            print("///// to be divided by /////")
            v2 = int(input(">> "))
            quotient = v1 / v2
            return print(str(quotient) + " is the product")
        except ValueError:
            print("Please input a number")
        except ZeroDivisionError:
            print("Cannot be divided by zero")

def opadd():
    while ValueError:
        try:
            v1 = int(input(">> "))
            print("///// to be added by /////")
            v2 = int(input(">> "))
            summ = v1 + v2
            return print(str(summ) + " is the product")
        except ValueError:
            print("Please input a number")


def opsub():
    while ValueError:
        try:
            v1 = input(">> ")
            print("///// to be subtracted by /////")
            v2 = input(">> ")
            difference = int(v1) - int(v2)
            return print(str(difference) + " is the product")
        except ValueError:
            print("Please input a number")

new_Task = True
while new_Task:
    u_input = input("Choose operation (Multiply, Addition, Subtraction, Division):\n ")
    if u_input.strip().lower() == "multiply":
        opmult()
        new_Task = False
    elif u_input.strip().lower() == "addition":
        opadd()
        new_Task = False
    elif u_input.strip().lower() == "subtraction":
        opsub()
        new_Task = False
    elif u_input.strip().lower() == "division":
        opdiv()
        new_Task = False
    else:
        print("Please Specify Operation,")
    if not new_Task:
        new_Task1 = input("Start another Calculation? (Yes/No): ")
        if new_Task1.strip().lower() == "yes":
            new_Task = True
        elif new_Task1.strip().lower() == "no":
            new_Task = False
            print("Thank You!\n----------------")


# Good Job
