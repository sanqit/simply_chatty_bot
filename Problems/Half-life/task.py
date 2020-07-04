n = int(input())
r = int(input())

k = 0
while r < n:
    n = n / 2
    k += 1

print(k * 12)
