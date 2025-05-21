while True:
    num_str = input("Введите число: ")
    if num_str.lower() == "exit":
        print("Выход из программы...")
        break

    if num_str.lstrip('-').isdigit():
        length = len(num_str.lstrip('-'))
        print(f"В этом числе {length} цифры.")
    else:
        print("Ошибка: данные не являются числом.")
