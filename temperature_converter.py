# Temperature Conversion Program
temperature = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F/K): ").upper()
if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Kelvin: {kelvin:.2f} K")
elif unit == "F":
    celsius = (temperature - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"Celsius: {celsius:.2f} °C")
    print(f"Kelvin: {kelvin:.2f} K")
elif unit == "K":
    celsius = temperature - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"Celsius: {celsius:.2f} °C")
    print(f"Fahrenheit: {fahrenheit:.2f} °F")
else:
    print("Invalid unit! Please enter C, F, or K.")
