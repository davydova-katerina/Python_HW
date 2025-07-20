def is_year_leap(number):
    return "True" if number % 4 == 0 else "False"


year = int(input("Год: "))
result = is_year_leap(year)
print(f"Год {year}: {result}")