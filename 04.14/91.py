def ordinalDate(day, month, year):
        ordinalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        res = 0
        i = 0
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            for i in range(month):
                res += leapYear[i]
            res = res-(leapYear[i] - day) 
        else:
            for i in range(month):
                res += ordinalYear[i]
            res = res-(ordinalYear[i] - day)  
         
        return res
 
def main():
    day = int(input("Enter day (1-31): "))
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    if month == 2 and day == 29:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(ordinalDate(day, month, year))
        else:
            print('ordinal year you have entered does not have febuary 29')
    else:
        print(ordinalDate(day, month, year))

main()

# Enter day (1-31): 2
# Enter month (1-12): 7
# Enter year: 2022
# 183
