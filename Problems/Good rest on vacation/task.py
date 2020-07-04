# put your python code here
duration_in_days = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_cost = int(input())

total_cost = food_cost * duration_in_days + hotel_cost * (duration_in_days - 1) + 2 * flight_cost
print(total_cost)
