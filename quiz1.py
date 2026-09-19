stock = {"кофе": 350.0, "чай": 120.0, "мате": 480.0}

def apply_discount(amount, percent):
    return amount * (1 - percent / 100)

names = []
qtys = []
sums = []

answer = input("Товар: ")
while answer != "стоп":
    if answer in stock:
        qty = int(input("Сколько: "))
        if qty > 0:
            names.append(answer)
            qtys.append(qty)
            sums.append(stock[answer] * qty)
        else:
            print("Пропускаю: неверное количество")
    else:
        print("Нет такого:", answer)
    answer = input("Товар: ")

total = 0
for i in range(len(names)):
    total = total + sums[i]
    print(f"{i + 1}. {names[i]} × {qtys[i]} = {sums[i]:.2f} ₽")

if total > 1000:
    final = apply_discount(total, 5)
    print(f"Итого со скидкой в 5%: {final:.2f} ₽")
else:
    final = total
    print(f"Итого: {final:.2f} ₽")

