c1 = input("Введите первый цвет (красный, синий, желтый): ").lower()
c2 = input("Введите второй цвет (красный, синий, желтый): ").lower()

if (c1 != "красный" and c1 != "синий" and c1 != "желтый") or \
   (c2 != "красный" and c2 != "синий" and c2 != "желтый"):
    print("Ошибка: введен неверный цвет")
elif c1 == c2:
    print(f"Получился тот же цвет: {c1}")
elif (c1 == "красный" and c2 == "синий") or (c1 == "синий" and c2 == "красный"):
    print("Фиолетовый")
elif (c1 == "красный" and c2 == "желтый") or (c1 == "желтый" and c2 == "красный"):
    print("Оранжевый")
elif (c1 == "синий" and c2 == "желтый") or (c1 == "желтый" and c2 == "синий"):
    print("Зеленый")