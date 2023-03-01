
mesto = int(input("Введите номер места: "))


if mesto % 2 == 0:
    if mesto <= 36:
        print("Верхнее место в купе")
    else:
        print("Верхнее место на боковой полке")
else:
    if mesto <= 36:
        print("Нижнее место в купе")
    else:
        print("Нижнее место на боковой полке")