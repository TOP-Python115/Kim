a = int(input('enter number 1: '))
b = int(input('enter number 2: '))

if a % b == 0:
    print(f"{a} делится на {b} нацело\n Частное: {a / b}")
else:
    print(f"{a} не делится на {b} нацело\nЧастное: {a // b}\nОстаток: {a % b}")