n = int(input())
res = 0
for a in range(1, n+1):
    if n % a == 0:
        res += a
print(res)