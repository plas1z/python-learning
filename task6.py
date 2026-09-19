summa = []


def discount_percent(amount):
    if amount >= 10000:
        return 15
    elif amount >= 5000:
        return 10
    elif amount >= 2000:
        return 5
    else:
        return 0

def final_price(amount):
    p = discount_percent(amount)
    return amount * (1 - p / 100)

answer = input("Сумма заказа: ")    
while answer != "стоп":                  
    total = float(answer)                
    if total <= 0:
        print("Пропускаю: неверная сумма")
    else:
        summa.append(total)
    answer = input("Сумма заказа: ")     # результат — ОБЯЗАТЕЛЬНО в переменную

if len(summa) == 0:
    print("Заказов не было")
else:
    print("=== РАСЧЁТ ===")

    viruchka = 0

    for i in range(len(summa)):
        viruchka = viruchka + final_price(summa[i])
        print(f"{i + 1}. {summa[i]:.2f} ₽ → скидка {discount_percent(summa[i])}% → к оплате {final_price(summa[i]):.2f} ₽")

    print(f"Итого выручка: {viruchka:.2f} ₽")

        


    