names = []
amount = []
print("""=== КОШЕЛЕК ===
1 — добавить трату
2 — показать все
3 — статистика
4 — найти по категории
5 — сохранить в файл
6 — загрузить из файла
0 — выход""")

answer = input("Выберите пункт: ")
while answer != "0":
    if answer == "1":
        kategoria = input("Категория: ").strip()   
        while kategoria != "стоп":                  
            summa_text = input("Сумма: ").strip()   

            if summa_text == "стоп":                
                kategoria = "стоп"                  
            else:
                try:
                    summa = float(summa_text)       
                    if summa > 0:
                        names.append(kategoria)     
                        amount.append(summa)
                        kategoria = input("Категория: ").strip()   
                    else:
                        print("Сумма должна быть больше 0")
                except ValueError:
                    print("Это не число, пропускаю")
        
                
    elif answer == "2":
        if len(names) == 0:
            print("Трат пока нет")
        else:
            for i in range(len(names)):
                print(f"{i + 1}. {names[i]} — {amount[i]:.2f} ₽")


            


    elif answer == "3":    
        if len(names) == 0:
            print("Трат пока нет")
        else:
            dlina = len(names)
            summa1 = sum(amount)
            srednee = summa1 / dlina
            biggest = max(amount)
            i = amount.index(biggest)
            name = names[i]
            print(f"Всего трат: {dlina}")
            print(f"Сумма: {summa1:.2f} ₽")
            print(f"Средняя: {srednee:.2f} ₽")
            print(f"Самая крупная: {name} на {biggest:.2f} ₽")

    elif answer == "4":
        target = input("Категория для поиска: ").strip()
        found = False
        for i in range(len(names)):
            if names[i] == target:
                print(f"{names[i]} — {amount[i]:.2f} ₽")
                found = True
        if not found:
            print(f"Трат по категории «{target}» не найдено")

    elif answer == "5":
        with open("wallet.txt", "w", encoding="utf-8") as f:
            skok = len(names)
            for i in range(len(names)):
                f.write(f"{names[i]};{amount[i]}\n")
            print(f"Сохранено: {skok} трат в wallet.txt")


    elif answer == "6":
        names.clear()
        amount.clear()
        try:
            with open("wallet.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split(";")
                    names.append(parts[0])
                    amount.append(float(parts[1]))
            print(f"Загружено: {len(names)} трат")
        except FileNotFoundError:
            print("Файла нет, грузить нечего")
           


    else:
        print("Нет такого пункта")
    answer = input("Выберите пункт: ")
print("Пока")
    

