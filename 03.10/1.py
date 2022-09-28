
'''
Задание 1
Пользователь вводит с клавиатуры три числа. 
Необходимо найти сумму чисел, произведение чисел. 
Результат вычислений вывести на экран.
'''



a = float(input('Enter number 01: '))
b = float(input('Enter number 02: '))
c = float(input('Enter number 03: '))

print('Sum of numbers ', a, ', ', b, ', ', c, ' = ', format((a+b+c), ',.2f'))
print('Product of numbers ', a, ', ', b, ', ', c, ' = ', format((a*b*c), ',.2f'))


