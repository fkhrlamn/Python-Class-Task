#  ECIE 3101 Semester 1 Session 23/24
#  Group member:

#Mohammad Fakhrul Amin Bin Zainor 1911309
#Khaled Emad Khaled AlBawaliz 1828405
#Ridhwan Syaafi bin Ma’ahad 1917147
#Muhammad Harith Danial bin Bazli 1923499


#calculates the length of hypotenuse of a right-angled triangle

import math

#Pythagorean theorem
def get_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

print("The program is designed to calculate the length of hypotenuse of a right-angled triangle ")

#ask user to input their desired length of right-angled triangle
a = float(input("Enter the length of first side: "))
b = float(input("Enter the length of second side: "))

print(f"\nThe length of the hypotenuse is: {get_hypotenuse(a, b) :.2f}")