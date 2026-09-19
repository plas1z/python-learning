summa = 0
count = 0
spisok2 = []

print("=== Журнал продаж ===")

with open("sales2.txt", "w", encoding="utf-8") as f:
    pass

with open("sales.txt", "a", encoding="utf-8") as f:
    pass

try:
    with open("sales.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        totalsum = sum(float(line.strip()) for line in lines)
        print(f"За прошлые запуски: {len(lines)} продаж на общую сумму: {totalsum:.2f} ₽.")
except ValueError:
    print("продаж не было")


    

answer = input("Введите сумму: ")        
while answer != "стоп":
    

    try:
        number = float(answer)           
        if number <= 0:
            print("Пропускаю: неверная сумма")
        else:
            summa = summa + number       
            count = count + 1            
            with open("sales2.txt", "a", encoding="utf-8") as f:
                f.write(f"{number}\n")   
                spisok2.append(number)

    except ValueError:                   
        print("Это не число, пропускаю")

    answer = input("Введите сумму: ")    

with open("sales.txt", "a", encoding="utf-8") as f:
    for number in spisok2:
        f.write(f"{number}\n")

with open("sales2.txt", "r", encoding="utf-8") as f:
    lines2 = f.readlines()
    totalsum2 = sum(float(line2.strip()) for line2 in lines2)
print(f"За этот запуск: {len(lines2)} продаж на общую сумму: {totalsum2:.2f} ₽.")

with open("sales.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    totalsum3 = sum(float(line.strip()) for line in lines)
    print(f"За всё время: {len(lines)} продаж на общую сумму: {totalsum3:.2f} ₽.")