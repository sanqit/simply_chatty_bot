# put your python code here
hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())

hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())

total_seconds_1 = seconds_1 + minutes_1 * 60 + hours_1 * 60 * 60
total_seconds_2 = seconds_2 + minutes_2 * 60 + hours_2 * 60 * 60

print(total_seconds_2 - total_seconds_1)
