fib1 = fib2 = 1

n = int(input())

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib2, end=' ')