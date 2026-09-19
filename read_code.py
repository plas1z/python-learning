stock = {"молоко": 80.0, "сыр": 550.0}

def delivery_cost(total):
    if total >= 5000:
        return 0
    elif total >= 2000:
        return 150
    return 300

names = ["кефир", "хлеб"]
price = stock["сыр"]
d = delivery_cost(3150)

print(names[0])
print(names[:1])
print(len(names))
print(f"{names[1]}: {price:.2f} ₽, доставка {d} ₽")
