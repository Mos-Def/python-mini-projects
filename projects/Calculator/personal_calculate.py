import time
import random

print("Welcome to your calculator")
print("Pick M for mutiplication, A for addition, S for subtraction, D for division")
while True:
    action = input()
    if action == 'M':
        #Mutiplication
        mutiplication_input = input("Number: ")
        mutiplied_input = input ("Times by: ")
        mutiplication = int(mutiplication_input)
        mutiplied = int(mutiplied_input)
        mutiplication_value = mutiplication * mutiplied
        print(mutiplication_value)
        break
    elif  action == 'A':
        #Addition
        addition_input = input("Number: ")
        added_input = input("Added by: ")
        addition = int(addition_input)
        added = int(addition)
        addition_value = addition + added
        print(addition_value)
        break
    elif action == 'S':
        #Subtraction
        subtraction_input = input("Number: ")
        subtract_input = input("Subtract by: ")
        subtraction = int(subtraction_input)
        subtracted = int(subtract_input)
        subtraction_value = subtraction - subtracted
        print(subtraction_value)
        break
    elif action == 'D':
        #Divison
        div_input = input("Number: ")
        divided_input = input("Divided by: ")
        division = int(div_input)
        divided = int(divided_input)
        division_value = division / divided 
        print(division_value)
        break



