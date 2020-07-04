# put your python code here
number = int(input())

last_digit = number % 10
number //= 10
middle_digit = number % 10
number //= 10
first_digit = number % 10
print(last_digit + middle_digit + first_digit)
