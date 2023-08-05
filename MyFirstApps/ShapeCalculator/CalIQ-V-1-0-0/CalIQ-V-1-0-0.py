# CalIQ Verson 1.0.0
# Programmer BlackIQ

# Libraries
import math

pi = 3.14

print("Square, Rectangle, Triangle, Circle")
shape = str(input("What shape do you want ? "))

if shape == "circle":
    ask_c = str(input("p or s ? "))
    if ask_c == "p":
        r = float(input("Give me r : "))
        p_c = (r+r)*pi
        print("P of this Circle is", p_c)
    if ask_c == "s":
        r = float(input("Give me r : "))
        s_c = (r*r)*pi
        print("S of this Circle is", s_c)
if shape == "rectangle":
    h_r = float(input("Give me height : "))
    w_r = float(input("Give me width : "))
    s_r = h_r*w_r
    p_r = (h_r+w_r)*2
    print("S of this Rectangle is", s_r)
    print("P of this Rectangle is", p_r)

if shape == "square":
    z = float(input("Give me z : "))
    s_s = z*z
    p_s = z*4
    print("S of this Square is", s_s)
    print("P of this Square is", p_s)

if shape == "triangle":
    b_t = float(input("Give me Base : "))
    h_t = float(input("Give me Height : "))
    z_1 = float(input("Give me first side : "))
    z_2 = float(input("Give me second side : "))
    z_3 = float(input("Give me third side : "))
    s_t = (b_t*h_t)/2
    p_t = z_1+z_2+z_3
    print("S of this triangle is", s_t)
    print("S of this triangle is", p_t)

exiting = input()
