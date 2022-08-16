x1 = str(input('coordinate 1 letter(a - h): '))
y1 = int(input('coordinate 1 number(1 - 8): '))
x2 = str(input('coordinate 2 letter(a - h): '))
y2 = int(input('coordinate 2 number(1 - 8): '))


if (ord(x1) + y1 + ord(x2) + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
