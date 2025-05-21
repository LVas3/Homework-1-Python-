try:
    num_input = input("Введите число: ")
    num = int(num_input)
    if num >= 0:
        if num % 2 == 0:
            print(f"Число {num} является четным")
        else:
            print(f"Число {num} не является четным")
    else:
        print("Ошибка: число должно быть неотрицательным")
except ValueError:
    print("Ошибка: введено не число")
