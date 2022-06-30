#       LEVEL UP
int(5.4) 

print(int(5.4))#floating point
print(int("54"))#integer

balance = 500
deposit = int(input ("How much would you like to deposit? "))

balance+=deposit

print(f"Your balance is: {balance}")

print ("What is you name?") #examples of truthy/falsy
name = input()

if name:
    print(f"Welcome {name} to innovate")
else: 
    print("You did not enter a name")

allowed = ["alex","brian","carol"]
name = input ("What is your name?")

while name not in allowed: #not operator
    print("Sorry your name isnt on the list")
    print("Try again")
    name=input("What is your name? ")
print("Please come in ")

#   Try/Except

def add_up():
    num1 = input("What is the first number you'd like to add up\n")
    num2 = input("What is the first number you'd like to add up\n")

    try:
        print(int(num1) + int(num2))
    except:
        print("Please use numbers only")
        add_up()
add_up()