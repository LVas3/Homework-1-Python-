while True:
    number = input("Введите число: ")
    if number == "exit" or number == "Exit" or number == "EXIT"  :
        print("Выход из программы...")
        break
    elif number.isdigit():
        print(f"В этом числе {len(number)} цифры.")
    elif number.lstrip('-').isdigit():
        print(f"В этом числе {len(number.lstrip('-'))} цифры.")
    else:
        print("данные не являются числом.")
