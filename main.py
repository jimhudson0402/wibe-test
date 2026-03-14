def get_name():
    while True:
        name = input("Как вас зовут? ").strip()

        if name:
            return name

        print("Вы не ввели имя")


name = get_name()
print(f"Привет, {name}")
age = input("Сколько тебе лет? ").strip()
print(f"Тебе {age} лет")

