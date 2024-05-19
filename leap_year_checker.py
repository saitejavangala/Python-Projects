def leap_year(year):
    if (year % 4 == 0 and year % 100!= 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not leap year")
    return

year = int(input("Enter a year: "))
leap_year(year)