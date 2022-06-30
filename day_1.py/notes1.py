import random

greeting = "Hello everyone!"

print(greeting)
print("This is a string for displaying characters")
print("1234") #string
print(1234+1) #integer/whole number
print(12.34) #float
print(True) #boolean
print(False) #boolean
print(None) #none - no data

print(len(greeting))
print(greeting[-1])

print(greeting.upper())
print(greeting)
print("HELLO".lower())
print("hellO eveRyonE. ".capitalize())
print("This quick brown fox fox fox".count("fox"))
print("The quick brown fox".find("r"))
print("The quick brown fox".replace("fox","leopard"))
print(("The quick brown fox").strip("brown"))

print(random.random())
print(random.uniform(1,10))

print(random.randint(1,10))
my_name="Chantelle"
my_age=37
student=True

print(my_name,my_age,student)
print("Hello my name is", my_name)
print("I am", my_age)

print("Hello my name is " + my_name)
# print("I am" + my_age)   #debug
print("Hello my name is and I am years old")

print(f"Hello my name is (my_name) and i'm (my_age) years old")

print(1+5)
print(10-5)
print(3*3)
print(5*+5)
print(8/4)
print(20%6)

balance=100
amount=20

balance=amount+balance
balance+=amount
print(balance)

#   variable
user=input("What's your name?\n")
print(user)

#   if/else statements
music = "rock"

if music == "rock":
    print("Oh no its rock!")
elif music == "no music":
    print("put the radio on")
else:
    print("crank that volume")

num=10
num2=20

# if num>num2:                       
#     print(f"{num} is bigger")
# elif num2 > (f"{num} is bigger")      #DEBUG
# else:
#     print("both are equal")

place = "mcr"
weather = "cloudy"

if place == "mcr" and weather== "sunny":
    print("check again")
elif place=="mcr" and weather =="cloudy":
    print("standard")
else:
    print("obviously")

day = "sat"
bank_holiday = True

if day == "sat" or day== "sun" or bank_holiday:
    print("chill its a free day")
else:
    print("get studying!")

#       Functions

def light_switch():
    print("who turned out the lights?\nits dark i cant see")

light_switch()

def withdrawal(amount, accnum):
    print (f"you have withdrawn {amount} from {accnum}")

withdrawal(500, 10000000)

#       Lists

genre = [
    "R&B"
    "Afrobeats"
    "Dancehall"
]
print(genre)
print(len(genre)) #len prints length of characters

genre.append("Soul") #appends list
print(genre)

#      For Loops

for i in genre:
    print(i)

for i in range(10): #prints 0-9
    print(i)

for i in range (100):
    print(i)

for i in range(2,10,2): #counting up in 2
    print(i)

for i in range(10,-1,-1): #counting backwards, start,stop,step
    print(i)

#      While Loops

num = 0
while num < 10:
    num +=1
    print(num)

my_num = 16
comp_num = random.randint(1,50)

while my_num != comp_num:
    print(f"the numbers {my_num} and {comp_num} do not match")
    comp_num = random.randint(1.50)

print(f"the numbers {my_num} and {comp_num} do not match")









