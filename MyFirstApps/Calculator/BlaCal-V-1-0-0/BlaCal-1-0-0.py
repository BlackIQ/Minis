# BlaCal Version 1.0.0
# Programmer BlackIQ

# Library
import math

# Describtion
print("welcome to BlackIQ calculator !")
print("these are the jobs that this program can do !")
print("sum , min , mul , div , sqrt , sin , cos , tan")

# Input
doing = str(input("What do you want to do ? "))

# conditional
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
    sqrt = math.sqrt(sqrt_number)
    print("√", sqrt_number, "=", sqrt)

if doing == "sin":
    sin_number = float(input("witch number ? "))
    sin = math.sin(sin_number)
    print("sin", sin_number, "=", sin)

if doing == "cos":
    cos_number = float(input("witch number ? "))
    cos = math.cos(cos_number)
    print("cos", cos_number, "=", cos)

if doing == "tan":
    tan_number = float(input("witch number ? "))
    tan = math.tan(tan_number)
    print("tan", tan_number, "=", tan)

# End
print ("Programmer : BlackIQ")
exiting = input()
