def get_name():
    while True:
        name = input("Как вас зовут? ").strip()

        if name:
            return name

        print("Вы не ввели имя")


def get_age():
    while True:
        age = input("Сколько тебе лет? ").strip()

        if age.isdigit():
            return int(age)

        print("Возраст должен быть числом")


name = get_name()
print(f"Привет, {name}")
age = get_age()
print(f"Тебе {age} лет")
