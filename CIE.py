def km_to_miles(km)
return km*1.64

def miles_to_km(miles)
return miles/1.64
print("Choose conversion type:")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
choice = input("Enter 1 or 2: ")

if choice == "1":
    km = float(input("Enter distance in kilometers: "))
    if km >= 0:
        print(f"{km} kilometers is equal to {km_to_miles(km):.2f} miles.")
    else:
        print("Please enter a value that is zero or more.")
elif choice == "2":
miles = float(input("Enter distance in miles: "))
    if miles >= 0:
        print(f"{miles} miles is equal to {miles_to_km(miles):.2f} kilometers.")
    else:
        print("Please enter a value that is zero or more.")
