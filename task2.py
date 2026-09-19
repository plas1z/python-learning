
order = float(input("Введите сумму заказа:"))
coupon = input("У вас есть купон на бесплатную доствку?")

if order <= 0 or order > 100000:
    print("Ошибка: некорректная сумма")
else:
    if order >= 5000 or coupon == "да":   # купон участвует в лестнице
        delivery = 0
    elif order >= 2000:
        delivery = 150
    else:
        delivery = 300

    final = order + delivery
    print(f"Итого к оплате: {final:.2f} ₽ (доставка {delivery:.2f} ₽)")



