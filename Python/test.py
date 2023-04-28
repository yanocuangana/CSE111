city_name = "Accra"
elevation = 61
population = 4200000

# Open a text file named cities.txt in append mode.
with open("cities.txt", "at") as cities_file:

    # Print a city's name and information to the file.
    print(city_name, file=cities_file)
    print(f"{elevation}, {population}", file=cities_file)