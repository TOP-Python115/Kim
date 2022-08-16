y = ''
while True:
    s = int(input())
    if s % 7 != 0:
        break
    y += str(s) + ' '
print(y, str(s), sep='')