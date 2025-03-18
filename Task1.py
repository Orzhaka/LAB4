password = input("Введите пароль: ")
confirm_password = input("Подтвердите пароль: ")

if password == confirm_password:
    print("Пароль принят")
else:
    print("Введенные пароли не совпадают")