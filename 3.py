def a(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


year = int(input("Введите год: "))


if a(year):
    print(f"Год {year} - високосный")
else:
    print("Это год не високосный")