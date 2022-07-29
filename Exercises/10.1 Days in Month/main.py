def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    # Docstring (Shows up as info when the function is written)
    """Returns the number of days in a year, leap years are included."""

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Removes 1 from user's month input in order to change from human counting to programming counting
    month -= 1

    if is_leap(year) and month == 1:
        return 29
    else:
        return month_days[month]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
