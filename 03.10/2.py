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



