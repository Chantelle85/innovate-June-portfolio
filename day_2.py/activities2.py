# #Activity 1

# activity 1 using if else
variable_1 = input("Enter a number:")
if variable_1.isnumeric():
    print("This is a number!")
else:
    print("This is not a number!")

#activity 1 using try except
def user_input():
    input_1 = input("Enter a number:\n")

    try:
        print(f"{int(input_1)} is a number!")
    except:
        print("Please use numbers only")
        user_input() #needs to be called here to keep running
user_input() #call input here

#Activity 2
capitals = {  
        "United Kingdom":"London",  #key:value
        "France":"Paris",
        "Germany":"Berlin",
        "Spain":"Madrid",
        "italy":"Rome"
}
capitals.setdefault("Portugal","Lisbon")    #dot notation 
capitals.setdefault("Poland","Warsaw")
print(capitals)

for i in capitals.items():
    print(i)

languages = {
        "United Kingdom":"English",            
        "France":"French",
        "Germany":"German",
        "Spain":"Spanish",
        "italy":"Italian"
}

languages.setdefault("Portugal","Portuguese")
languages.setdefault("Poland","Polish")
capitals.update(languages)
print (capitals ["Poland"]) #check if key has been changed to update capitals to languages

#Activity 3
fav_songs=[     #dictionaries{} in a list[]
    {"Artist":"Lauryn Hill", "Song_name":"Ex-factor", "Genre":"R&B/Soul", "Release_year":"1999"}, 
    {"Artist":"Hybrid Minds", "Song_name":"Touch", "Genre":"Drum & Bass", "Release_year":"2016"}, 
    {"Artist":"Commodores", "Song_name":"Nightshift", "Genre":"Funk/Soul", "Release_year":"1985"}, 
    {"Artist":"Joeboy", "Song_name":"Baby", "Genre":"Afrobeats", "Release_year":"2021"}, 
    {"Artist":"Gregory Abbott", "Song_name":"Shake you down", "Genre":"R&B/Soul", "Release_year":"1986"}
]
print()

for song in fav_songs:
    print(song)

print(f'Replace - {fav_songs[4]} with')

fav_songs[1]={"Artist":"Latto", "Song_name":"Big Energy Remix", "Genre":"Pop/Rap", "Release_year":"2022"}
print(f"New song - {fav_songs[1]}")

print("New Playlist:")
for song in fav_songs:
        print(song)