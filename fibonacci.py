#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def user_Input(terms): 
    if(input_user1 > 0): 
        return True 
    else: 
        print("Please enter a positive integer.")

def gen_Fibonacci(terms):
    forL = terms 
    x1 = 0 
    x2 = 1 
    count = 0
    for count in range(forL): 
        print_Fibonacci(x1,x2,count) 
        if(count%2 == 0):
            x1+= x2 
        else:
            x2+= x1 
        count += 1
def print_Fibonacci(termA, termB,cycle): 
    if(cycle%2 == 0): 
        print(termA,end = " ") 
    else: 
        print(termB,end = " ") 
input_user1 = 0 
input_user = input("User input: ") 
input_user1 = int(input_user) 
x = user_Input(input_user1) 
if(x == True): 
    gen_Fibonacci(input_user1)
