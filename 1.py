passw = input("Введите пароль: ")
repass = input("Подтвердите пароль: ")

if passw != repass:
    print("Пароли не совпадают")
if len(passw) <= 6:
    print("Пароль короткий")

elif (
    passw == repass and
    any(c.isdigit() for c in passw) and
    any(c.islower() for c in passw) and
    any(c.isupper() for c in passw) and
    any(c in "!@#$%^&*()_+-={}[]|\:;'<>?,./" for c in passw)
):
    print("Пароль принят")
else:
    print("Пароль не принят")