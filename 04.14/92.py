ordinalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
period = 14
    
def yearDay_to_dayMonth(year, day):
    res = 0
    month = 0
    if day <= 31:
        res = [day, 1]
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            for m in leapYear:
                day -= m
                month += 1
                if day <= 0:
                    res = [day + m, month]
                    break
        else:
            for m in ordinalYear:
                day -= m
                month += 1
                if day <= 0:
                    res = [day + m, month]
                    break
    res.insert(0, year)
    print(f"year: {res[0]} \n"
          f"month: {res[2]} \n"
          f"day: {res[1]}")
   
            
def ordinalDate(day, month, year):
        # ordinalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        dayNumber = 0
        i = 0
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            for i in range(month):
                dayNumber += leapYear[i]
            dayNumber = dayNumber-(leapYear[i] - day) 
        else:
            for i in range(month):
                dayNumber += ordinalYear[i]
            dayNumber = dayNumber-(ordinalYear[i] - day)  
        
        dayNumber += period
        
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:    
            if dayNumber > 366:
                year += 1
                dayNumber -= 366
        else:
            if dayNumber > 365:
                year += 1
                dayNumber -= 365
        
        yearDay_to_dayMonth(year, dayNumber)   
        
def main():
    day = int(input("Enter day (1-31): "))
    month = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    if month == 2 and day == 29:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            ordinalDate(day, month, year)
        else:
            print('ordinal year you have entered does not have febuary 29')
    else:
        ordinalDate(day, month, year)

main()


# Enter day (1-31): 30
# Enter month (1-12): 12
# Enter year: 2020
# year: 2021
# month: 1
# day: 13


