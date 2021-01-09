#Write a program which will ask for two numbers from a user. Then
#offer a menu to the user giving them a choice of operator:
#e.g. – Enter “a” if you want to add
#“b” if you want to subtract
#Include +, -, /, *, **(to the power of) and square. Once the user has
#selected which operator they wish to use, perform the calculation.

print("Hi! I'm here to help you calculate! I want you to give me two numbers!")
first = int(input("What is your first number choice?"))
second = int(input("What is your second number choice?"))
print("Great job!")

print ("""
    A = Add Numbers together.
    B = Subtract the second number from the first.
    C = Divide second number by first number.
    D = Multiply numbers together.
    E = First number to the power of second.
    F = Square the numbers.
    """)
method = str(input("Choose a letter A-F"))

if method == "A" or method =="a":
    print(first+second)

elif method == "B" or method =="b":
    print(first-second)

elif method == "C" or method =="c":
    print(second/first)

elif method == "D" or method =="d":
    print(second*first)

elif method == "E" or method =="e":
    print(first**second)

elif method == "F" or method =="f":
    print(pow(first,2),pow(second,2))
