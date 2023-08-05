# BlaCal Version 2.0.0
# Programmer BlackIQ

# Library
import math

# Functions
def sum():
    sum_1 = float(input("what is first number ? "))
    sum_2 = float(input("what is second number ? "))
    print(sum_1, " + ", sum_2, " = ", sum_1+sum_2)

def min():
    min_1 = float(input("what is first number ? "))
    min_2 = float(input("what is second number ? "))
    print(min_1, " - ", min_2, " = ", min_1-min_2)

def mul():
    mul_1 = float(input("what is first number ? "))
    mul_2 = float(input("what is second number ? "))
    print(mul_1, " * ", mul_2, " = ", mul_1*mul_2)

def div():
    div_1 = float(input("what is first number ? "))
    div_2 = float(input("what is second number ? "))
    print(div_1, " / ", div_2, " = ", div_1/div_2)

def sqrt():
    sqrt_number = float(input("witch number ? "))
    sqrt = math.sqrt(sqrt_number)
    print("√", sqrt_number, "=", sqrt)

def sin():
    sin_number = float(input("witch number ? "))
    sin = math.sin(sin_number)
    print("sin", sin_number, "=", sin)

def cos():
    cos_number = float(input("witch number ? "))
    cos = math.cos(cos_number)
    print("cos", cos_number, "=", cos)

def tan():
    tan_number = float(input("witch number ? "))
    tan = math.tan(tan_number)
    print("tan", tan_number, "=", tan)

# Describtion
print("welcome to BlaCal calculator !")
print("these are the jobs that this program can do !")
print("sum , min , mul , div , sqrt , sin , cos , tan")

# Input
doing = str(input("What do you want to do ? "))

# conditional
if doing == "sum":
    sum()

if doing == "min":
    min()

if doing == "mul":
    mul()

if doing == "div":
    div()

if doing == "sqrt":
    sqrt()

if doing == "sin":
    sin()

if doing == "cos":
    cos()

if doing == "tan":
    tan()

# End
print ("Programmer : BlackIQ")