# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
first = ticket % 10
ticket //= 10
second = ticket % 10
ticket //= 10
third = ticket % 10
ticket //= 10

half1 = first + second + third

first = ticket % 10
ticket //= 10
second = ticket % 10
ticket //= 10
third = ticket % 10

half2 = first + second + third

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
