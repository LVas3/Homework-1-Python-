agefromuser = input("Введите ваш возраст: ")
if agefromuser.isdigit():
    age=int(agefromuser)
    if age >= 18:
            print("Вы совершеннолетний")
    elif age < 0:
            print("Ошибка: возраст не может быть отрицательным!")
    elif age > 0 & age<18:
            print("Вы несовершеннолетний")
else:
        print("введено не число!")
