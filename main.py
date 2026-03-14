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


def main():
    name = get_name()
    age = get_age()
    print(f"Привет, {name}")
    print(f"Тебе {age} лет")
    print(f"Через 10 лет тебе будет {age + 10} лет")


if __name__ == "__main__":
    main()
