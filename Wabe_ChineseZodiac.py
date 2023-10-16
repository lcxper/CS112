#Chinese zodiac sign
def find_zodiac_sign(year):
    if year < 1900:
        return "Year should be 1900 or later."
    
    zodiac_animal = (year - 1900) % 12
    
    rat = zodiac_animal == 0
    ox = zodiac_animal == 1
    tiger = zodiac_animal == 2
    rabbit = zodiac_animal == 3
    dragon = zodiac_animal == 4
    snake = zodiac_animal == 5
    horse = zodiac_animal == 6
    goat = zodiac_animal == 7
    monkey = zodiac_animal == 8
    rooster = zodiac_animal == 9
    dog = zodiac_animal == 10
    pig = zodiac_animal == 11

    return {
        "Rat": rat, "Ox": ox, "Tiger": tiger, "Rabbit": rabbit,
        "Dragon": dragon, "Snake": snake, "Horse": horse, "Goat": goat,
        "Monkey": monkey, "Rooster": rooster, "Dog": dog, "Pig": pig
    }

# Input year from the user
year = int(input("Enter a year: "))

# Find and display the Chinese zodiac sign
zodiac_signs = find_zodiac_sign(year)
sign = [key for key, value in zodiac_signs.items() if value][0]

print(f"The Chinese zodiac sign for the year {year} is {sign}.")