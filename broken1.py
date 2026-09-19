prices = [100, 250, 40]

def total_with_discount(prices, percent):
    total = 0
    for p in prices:
        total = total + p
    return total * (1 - percent / 100)

d = {"чай": 120, "кофе": 350}
print(d["чай"])

n = int(input("Число: "))
if n == 10:
    print("десять")

words = ["а", "б", "в"]
print(words[2])
