cart = []
prices = []


tovar = input("Товар: ")
while tovar != "стоп":                    
    price = float(input("Цена: "))        
    cart.append(tovar)                   
    prices.append(price)
    tovar = input("Товар: ")              
    
print("=== ЧЕК ===")

for i in range(len(cart)):
    print(f"{i + 1}. {cart[i]} — {prices[i]:.2f} ₽")

if len(cart) == 0:
    print("Чек пустой")
else:
    summa = sum(prices)

    print(f"В корзине {len(cart)} шт. На сумму {summa:.2f} ₽")
