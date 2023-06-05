#This program functions as a price calculator for holidays, based on hotel, flight and car hire costs.
#It utilises dictionaries and multiple functions to perform its actions, and could be adapted to work with .csv files for larger datasets.

#Dictionaries for the cities and their corresponding flight and hotel costs.
#These get pulled for the plane cost and hotel cost calculations
# and can be added to easily to put more holiday options in for the user, without having to create new IF statements.
flight_prices = {"paris": 150, "belgium": 215, "london": 175}
hotel_prices = {"paris": 90, "belgium": 85, "london": 120}

# FUNCTIONS - placed at the top as 

#Calculate the hotel cost by using the city_flight input as a key in the hotel prices dictionary
#then multiply the value found in the dictionary by the number of nights staying
def hotel_cost():
    total = num_nights*hotel_prices[city_flight]
    return total

#Calculate the plane cost by using the city flight input as a key for the flight prices dictionary
# then multiplies it by 2 (one flight each way!) and returns the total.
def plane_cost():
    total = flight_prices[city_flight]*2
    return total
    
#Multiples the chosen rental days by 60 and returns the total
def car_rental():
    total = rental_days*60
    return total

#Adds the returned values of hotel cost, plane cost and car rental together.
def holiday_cost():
    total = hotel_cost() + plane_cost() + car_rental()
    return total

# USER CODE

#Ask for a city choice by pulling available options from the flight dictionary
# then checks if the inputted string exists in the dictionary
# accepts it and moves on if it is, or restarts the loop if it isn't
while True:
    print("Available destinations are: ")
    for keys in flight_prices:
        print(keys.capitalize())
    city_flight = input("Please type your choice: ")
    city_flight = city_flight.lower()       #Converts their input to lower case for future checks
    if city_flight in flight_prices:
        break
    else:
        print("Please try again.")
        continue
    
#Asks for number of nights to stay as an integer.
while True:
    try:
        num_nights = int(input("Enter the number of nights you wish to stay: "))
        break
    except ValueError:
        print("Enter a whole number only.")

#Asks for number of car rental days as an integer.
while True:
    try:
        rental_days = int(input("Enter the number of days you will be hiring a car for: "))
        break
    except ValueError:
        print("Enter a whole number only.")

#Prints a reminder of the user's holiday choices:
print(f"\nYour holiday details for a {num_nights} nights trip to {city_flight.capitalize()}, with {rental_days} days of car hire:")

#Calls each function from above to calculate the relevant costs based on the user's input.
#Prints out each of the calculated costs to the user that have now been saved using the return function
print(f"Your hotel will cost £{hotel_cost()}")
print(f"Your flights will cost £{plane_cost()}")
print(f"Your car will cost £{car_rental()}")
print(f"Your total holiday cost will be £{holiday_cost()}.")
