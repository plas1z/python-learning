# task1.py — калькулятор чека (твоя самостоятельная работа, урок 1)

name = input("Какое название товара? ")


price = float(input("Сколько цена за штуку? "))

value = int(input("Кол-во товара? "))

bill = price * value
sale = bill * 0.9


print(f"Чек: Вы купили {value} {name}, сумма: {bill:.2f} ₽ (со скидкой 10%: {sale} ₽)")
