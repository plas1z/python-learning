stock = {"молоко": 80.0, "хлеб": 55.0, "сыр": 550.0, "кефир": 95.0}
names = []    
qtys = []
sums = []


tovar = input("Товар: ")

while tovar != "стоп": 
    if tovar in stock:
        price = stock[tovar]
        qty = int(input("Сколько: "))
        if qty <= 0:
            print("Пропускаю: неверное количество")
        else:
            names.append(tovar)
            qtys.append(qty)
            sums.append(price * qty) 
    else:
        print(f"У нас нет в наличии {tovar}")

    tovar = input("Товар: ")

if (len(names)) == 0:
    print("Чек пустой")

else:

    print("=== ПОКУПКИ ===")

    for i in range(len(names)):
        print(f"{i + 1}. {names[i]} — {qtys[i]} шт — {sums[i]:.2f} ₽")

    summa = sum(sums)
    print(f"Итого: {summa:.2f} ₽")

    best = None
    best_sum = 0 
    for i in range(len(sums)):
        if sums[i] > best_sum:
            best = names[i]
            best_sum = sums[i]
            print(f"Самая дорогая покупка: {best} на {best_sum:.2f} ₽")