n = int(input())

pibonacci = [0, 1]
for i in range(2, n + 1):
    pibonacci.append(pibonacci[i-1] + pibonacci[i-2])
print(pibonacci[n])