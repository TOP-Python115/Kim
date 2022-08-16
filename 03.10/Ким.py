
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


'''
Задание 2
Пользователь вводит с клавиатуры три числа. 
Первое число — зарплата за месяц, второе число — сумма месячного платежа по кредиту в банке, 
третье число — задолженность за коммунальные услуги. 
Необходимо вывести на экран сумму, которая останется у пользователя после всех выплат.
'''



salary = float(input('Enter month salary: '))
credit_pay = float(input('Enter month credit pay: '))
utility_bill = float(input('Enter month utility bill: '))

balance = salary - (credit_pay + utility_bill)

print('Your balance after all payments is ', format(balance, ',.2f'))



'''
Задание 3
Напишите программу, вычисляющую площадь ромба. 
Пользователь с клавиатуры вводит длину двух его диагоналей.
'''



a = float(input('Enter the lentgth of the diagonal A: '))
b = float(input('Enter the lentgth of the diagonal B: '))

square = (a * b) / 2

print('Square of the rhombus is ', format(square, '.2f'))



'''
Задание 4
Выведите на экран надпись To be or not to be на разных строках. 
Пример вывода:To be or not to be
'''


from colorama import init

init()

print('\t\t\t\t\t\t\t\033[3mTo be') #  cmd не поддерживает italic или я что-то делаю не так
print('\t\t\t\t\t\t\tor not')
print('\t\t\t\t\t\t\tto be')



'''
Задание 5
Выведите на экран надпись «Life is what happens 
when you're busy making other plans» John Lennon на разных строках. 
'''
    
print('"Life is what happens')
print('\twhen')
print('\t    you\'re busy making other plans"')
print('\t\t\t\t\tJohn Lennon.')



