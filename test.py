def get_valid_age():
    while True:
        try:
            birth_year = int(input("Введите свой год рождения: \n"))
            if birth_year < 1900 or birth_year > 2026:
                print("Некорректный год!")
                continue
            print(f"Год принят: {birth_year}")
            break
        except ValueError:
            print("Введите цифры!")


get_valid_age()
