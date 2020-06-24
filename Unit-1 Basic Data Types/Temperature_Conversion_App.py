#Python Challenge 3	Temperature Conversion App

print("Welcome to the Temperature Conversion Program")

#Get User Input
temperature_f = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))

#Convert temps
Celsius = (temperature_f - 32) * 5/9
Kelvin = (temperature_f -32) * 5/9 + 273.15

#Round temps
temperature_f = round(temperature_f, 4)
Celsius = round(Celsius, 4)
Kelvin = round(Kelvin, 4)

#Summary tables
print("\nDegrees Fahrenheit:	", temperature_f)
print("Degrees Celsius:	", Celsius)
print("Degrees Kelvin:		", Kelvin)