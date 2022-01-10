# BlaCal Version 3.0.0
# Programmer BlackIQ

# Library
import math
from termcolor import colored

# Colorising with termcolor
welcome = colored('welcome to BlaCal calculator !', 'blue')
version = colored('verson 3.0.0', 'blue')
jobs = colored('these are the jobs that this program can do !', 'red')
jobs_list = colored('sum , min , mul , div , sqrt , sin , cos , tan', 'yellow')
end_1 = colored("The End", 'red')
end_2 = colored("Programmer : BlackIQ", 'red')

# Functions {
# Describtion function
def start():
    print(welcome)
    print(version)
    print(jobs)
    print(jobs_list)

# End function
def end():
    print(end_1)
    print(end_2)

# Functions Doing
def sum():
    sum_1 = float(input("what is first number ? "))
    sum_2 = float(input("what is second number ? "))
    o_sum = (sum_1+sum_2)
    sum_cololed = colored(o_sum, 'green')
    print(sum_cololed)

def min():
    min_1 = float(input("what is first number ? "))
    min_2 = float(input("what is second number ? "))
    o_min = (min_1-min_2)
    min_cololed = colored(o_min, 'green')
    print(min_cololed)

def mul():
    mul_1 = float(input("what is first number ? "))
    mul_2 = float(input("what is second number ? "))
    o_mul = (mul_1*mul_2)
    mul_cololed = colored(o_mul, 'green')
    print(mul_cololed)

def div():
    div_1 = float(input("what is first number ? "))
    div_2 = float(input("what is second number ? "))
    o_div = (div_1/div_2)
    div_cololed = colored(o_div, 'green')
    print(div_cololed)

def sqrt():
    sqrt_number = float(input("witch number ? "))
    o_sqrt = math.sqrt(sqrt_number)
    sqrt_colored = colored(o_sqrt, 'green')
    print(sqrt_colored)

def sin():
    sin_number = float(input("witch number ? "))
    o_sin = math.sin(sin_number)
    sin_colored = colored(o_sin, 'green')
    print(sin_colored)

def cos():
    cos_number = float(input("witch number ? "))
    o_cos = math.cos(cos_number)
    cos_colored = colored(o_cos, 'green')
    print(cos_colored)

def tan():
    tan_number = float(input("witch number ? "))
    o_tan = math.tan(tan_number)
    tan_colored = colored(o_tan, 'green')
    print(tan_colored)

# Conditional
def doing_me():
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

# Start
start()

# Input
doing = str(input("what do you want to do ? "))

# Main Code
doing_me()

# End
end()