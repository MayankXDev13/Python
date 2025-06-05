year = 2025


if (year % 400) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is NOT a leap year")
    