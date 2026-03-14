
while True:
    name = input("Как вас зовут? ").strip()

    if name:
        print(f"Привет, {name}")
        break
else:
    print("Вы не ввели имя")
