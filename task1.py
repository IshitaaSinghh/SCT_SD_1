def celsius_to_fahrenheit (c):
    return (c * 9/5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k): 
    return k - 273.15
def kelvin_to_fahrenheit (k):
    return (k - 273.15) * 9/5 + 32
print("Temperature Converter") 
print("1. Celsius to Fahrenheit") 
print("2. Celsius to Kelvin") 
print("3. Fahrenheit to Celsius") 
print("4. Fahrenheit to Kelvin") 
print("5. Kelvin to Celsius") 
print("6. Kelvin to Fahrenheit")
choice = int(input("Choose an option: "))
if choice == 1:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit (c))
elif choice == 2:
    c = float(input("Enter Celsius: ")) 
    print("Kelvin:", celsius_to_kelvin(c))
elif choice == 3:
    f = float(input("Enter Fahrenheit: ")) 
    print("Celsius:", fahrenheit_to_celsius (f)) 
elif choice == 4:
    f = float(input("Enter Fahrenheit: ")) 
    print("Kelvin:", fahrenheit_to_kelvin(f))
elif choice == 5:
    k = float(input("Enter Kelvin: ")) 
    print("Celsius:", kelvin_to_celsius(k))
elif choice == 6:
    k = float(input("Enter Kelvin: ")) 
    print("Fahrenheit:", kelvin_to_fahrenheit (k))
else:
    print("Invalid choice!")