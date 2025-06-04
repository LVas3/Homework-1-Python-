
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
#Можно реализовать через одну строку
#name, surname, age = input("Введите ваше имя, фамилию и возраст через пробел: ").split()

print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age))


print("\nРеализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет")
