total = 0
count = 0

print("Вас привествует касса самообслуживания, когда товары закончастя напишите стоп")

tovar = input("Напишите цену товара:")


    

    
    

while tovar != "стоп":
        price = float(tovar)
    
    
    

        if price <= 0:
            print("Пропускаю: некорректная цена")
        else:
            total = total + price
            count = count + 1



        tovar = input("Напишите цену товара:")
    

if count == 0:
    print("Чек пустой!")
else:
    if total >= 5000:
        delivery = 0
    elif total >= 2000:
        delivery = 150
    else:
        delivery = 300

    srednee = total / count
    final = total + delivery

    print(f"Товаров: {count}, к оплате: {final:.2f} ₽, средняя цена:{srednee:.2f} ₽, доставка:{delivery}₽")