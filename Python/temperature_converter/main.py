print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Which conversion? (1 or 2): ")

if choice == '1':
    c = float(input("Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c}°C = {f}°F")
elif choice == '2':
    f = float(input("Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f}°F = {c}°C")
else:
    print("Invalid choice!")