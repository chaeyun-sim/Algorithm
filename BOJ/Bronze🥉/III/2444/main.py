n = int(input())

for i in range(n - 1, 0, -1):
    print((" " * i) + "*" * ((n - i) * 2 - 1))
for i in range(n):
    print((" " * i) + "*" * ((n - i) * 2 - 1))