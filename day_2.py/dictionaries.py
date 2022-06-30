#Dictionary notes

#use {} to define dictionaires

my_cat = { 
        "name":"tilly", 
        "colour": "black",
        "mood": "shy"
    }
print(my_cat["mood"])
print(f'My cat {my_cat["name"]} is a bit {my_cat["mood"]} today.') #use ' instead of " inside string when already used "

my_cat["mood"] = "sleepy" # method to update a value
print(my_cat["mood"])

x=my_cat.keys() #update keys
my_cat["age"]=6

print(my_cat.get("colour"))
print(my_cat.items())
print(my_cat.values())
print(x)

for i in my_cat.keys():
    print(i)

my_cat.update({"legs":"3"}) #to update dictionary
my_cat.update({"name":"mia"})
print(my_cat)



