zodiac_animals = ["monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"]
year = int(input("enter your year of birth: "))
print(year, "is", zodiac_animals[year %12] )
