age = int(input('Age: '))

if age >= 1 and age <= 13:
    print('Детство')
elif age <= 24 and age != 0:
    print('Молодость')
elif age <= 59 and age != 0:
    print('Зрелость')
elif age >= 60:
    print('Старость')
else:
    print('Ошибка')