print("Требования к паролю: хотя бы 1 заглавная, 1 строчная, 1 цифра, 1 спецсимвол(_ ! @ ( ) ")
password1=input("Введите пароль: ")
if (any(ch.isdigit() for ch in password1) == True) and (any(ch.islower() for ch in password1)==True) and (any(ch.isupper() for ch in password1)==True) and (any(ch in "_!@()" for ch in password1)==True):
    password2=input("Подтвердите пароль: ")
    if password1 != password2:
        print("Пароли не совпадают")
    else:
        print("Пароль введен успешно")
else:
    print("Пароль не подходит к требованиям")