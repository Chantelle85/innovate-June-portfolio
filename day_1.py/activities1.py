#Activity 1

header = "Welcome to Code Nation"
headerlen = (len(header))

def odd_even_checker(header):
    if (headerlen % 2) == 0: 
        print(f'"{header}" is {headerlen} characters long and an even number.')
    else:
        print(f'"{header}" is {headerlen} characters long and an odd number.')
odd_even_checker(header)

#Activity 2
alphabet = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u',
    'v','w','x','y','z'
]
alphabet_index = 0
for i in range(len(alphabet)):
    print(alphabet[alphabet_index])
    alphabet_index += 1

def user_input():
    usernum = input("enter a number from 1 to 26 to find the corresponding letter: ")
    if usernum.isnumeric() == True:
        usernum = int(usernum)
        if usernum in range(1,27):
            print(f"you chose {usernum}, which equals to the letter {alphabet[usernum-1].upper()}! Have another go...\n")
            user_input()
        else:
            print("Sorry the alphabet only has 26 letters, TRY AGAIN: ")
            user_input()
    else:
        print("oops!!\nthat's not even a number try again: ".upper())
        user_input()
user_input()