import jdatetime
from math import *
from time import *

def get_name():
    name = str(input("What Is Your Name ? "))
    print("Welcome" , name)

def acts():
    ac1 = str(input("What can I do for you ? "))
    if "date and time" in ac1:
        print(jdatetime.datetime.now())
    elif "date" in ac1:
        print(jdatetime.datetime.now().date())
    elif "time" in ac1:
        print(jdatetime.datetime.now().time())
    elif "calculator" in ac1:
        print("welcome to BlackAI calculator !")
        print("these are the jobs that this program can do !")
        print("sum , min , mul , div , sqrt , sin , cos , tan")
        doing = str(input("What do you want to do ? "))

        if doing == "sum":
            sum_1 = float(input("what is first number ? "))
            sum_2 = float(input("what is second number ? "))
            print(sum_1, " + ", sum_2, " = ", sum_1+sum_2)

        if doing == "min":
            min_1 = float(input("what is first number ? "))
            min_2 = float(input("what is second number ? "))
            print(min_1, " - ", min_2, " = ", min_1-min_2)

        if doing == "mul":
            mul_1 = float(input("what is first number ? "))
            mul_2 = float(input("what is second number ? "))
            print(mul_1, " * ", mul_2, " = ", mul_1*mul_2)

        if doing == "div":
            div_1 = float(input("what is first number ? "))
            div_2 = float(input("what is second number ? "))
            print(div_1, " / ", div_2, " = ", div_1/div_2)

        if doing == "sqrt":
            sqrt_number = float(input("witch number ? "))
            sqrt_n = sqrt(sqrt_number)
            print("√", sqrt_number, "=", sqrt_n)

        if doing == "sin":
            sin_number = float(input("witch number ? "))
            sin_n = sin(sin_number)
            print("sin", sin_number, "=", sin_n)

        if doing == "cos":
            cos_number = float(input("witch number ? "))
            cos_n = cos(cos_number)
            print("cos", cos_number, "=", cos_n)

        if doing == "tan":
            tan_number = float(input("witch number ? "))
            tan_n = tan(tan_number)
            print("tan", tan_number, "=", tan_n)

def AI_end():
    job = str(input("Do you want restart ? "))
    if job == "yes":
        AI()
    elif job == "no":
        print("Bye", "name_of_user")
    else:
        print("Error !")

def AI():
    get_name()
    acts()
    AI_end()
