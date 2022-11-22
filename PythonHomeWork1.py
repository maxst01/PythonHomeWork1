num = int(input("Введите день недели числом: "))
if 6 <= num <= 7:
    print("ДА")
elif 0 < num < 6:
    print("Нет")
else:
    print("Число не равно дням недели")
