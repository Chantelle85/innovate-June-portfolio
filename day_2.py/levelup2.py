#level up

import random

#   global and local scopes
light = False #global variable

def light_switch(): 
    global light #add a global to allow the program to see it
    if light:
        print("Wow Its bright in here")
        light = False #local variable
    else:
        print("who turned out the light")
        light = True #local variable

light_switch()
light_switch()

#   Tuples (tuples are immutable/cant be changed once made)

evens_nums = [2,4,6,8,10] #lists square brackets
odd_nums = (1,3,5,7,9) #tuples curly brackets

evens_nums.append(12) 
evens_nums.insert(0,0)
print(evens_nums)

#   Slice Notation
genre = [
    "R&B",
    "Afrobeats",
    "Dancehall"
]
print(genre[1]) #this is an index postion [the starting value]
print(genre[1:2:1]) #[start:stop:step]

#   make a string variable
# if it reads forward as the same backwards
# if it does say yes if it doesnt say no

test ="madam"
if test == test[::-1]:
    print(f"yes {test} is a palindrome")
else:
    print("its not a palindrome")

#    While True Loop

num = random.randint(1,50)

while num%2==0: #compares variable and runs under condition
    print("we like even numbers")
    num=random.randint(1,50)
#   if number is odd while loop wont ever run
print("oh no an odd number")

while True: #this loop will always run
    num=random.randint(1,50)
    print(num)
    if num%2==0:
        print("we like even numbers")
        continue
    else:
        print("an odd number")
        break



