n = int(input())

result = 1
current = 1
while current <= n:
    result *= current
    current += 1

print(result)
