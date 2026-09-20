summa = 0
count = 0
add1 = []
print("=== КОШЕЛЕК ===")

with open("add.txt", "w", encoding="utf-8") as f:
    pass

with open("total.txt", "a", encoding="utf-8") as f:
    pass

with open("promej.txt", "w", encoding="utf-8") as f:
    pass

with open("max.txt", "a", encoding="utf-8") as f:
    pass

with open("start.txt", "w", encoding="utf-8") as f:
    f.write("1 — добавить трату\n2 — показать все\n3 — статистика\n4 — найти по категории\n5 — сохранить в файл\n6 — загрузить из файла\n0 — выход")

with open("start.txt", "r", encoding="utf-8") as f:
    text = f.read().strip()
    print(text)

exit1 = "0"
answer = input("Выберите пункт: ")
while answer != exit1:
    if answer == "1":
        kategoria = input("Категория: ")
        while kategoria != "стоп":
            try:
                summa1 = float(input("Сумма: "))
                with open("total.txt", "a", encoding="utf-8") as f:
                    f.write(f"{summa1}\n")
                with open("add.txt", "a", encoding="utf-8") as f:
                    f.write(f"{kategoria} - {summa1} руб\n")
                with open("max.txt", "a", encoding="utf-8") as f:
                    f.write(f"{kategoria} - {summa1} руб\n")
                    add1.append(f"{kategoria} - {summa1} руб")
            except ValueError:
                print("Это не число, пропускаю")



            kategoria = input("Категория: ")

    elif answer == "2":
        count1 = count + len(add1)
        print(f"За сегодня - {count1} покупоки")
        with open("promej.txt", "a", encoding="utf-8") as f:
            for number in add1:
                f.write(f"{number}\n")
        add1.clear()

        with open("promej.txt", "r", encoding="utf-8") as f:
            lines2 = f.readlines()
            if len(lines2) != 0:
                print("\n".join(f"{i}. {line.strip()}" for i, line in enumerate(lines2, start=1)))
            else:
                pass
    elif answer == "3":
        with open("total.txt", "r", encoding="utf-8") as f:
            lines3 = f.readlines()
        clean_lines = [line for line in lines3 if line.strip()]
        if len(clean_lines) == 0:
            print("История покупок пуста.")
        else:
            amounts = [float(line.strip()) for line in clean_lines]
            totalsum = sum(amounts)
            total_count = len(amounts)
            srednee = totalsum / total_count
        print(f"За всё время {total_count} покупок на сумму {totalsum} руб\nсредняя цена : {srednee:.2f} руб")
        with open("max.txt", "r", encoding="utf-8") as f:
            lines4 = f.readlines()
            maximum = max(lines4)
            print(f"Самая дорогая покупка:\n{maximum}")
    elif answer == "4":
        answer2 = input("Категория для поиска:")
        if answer2 != "стоп":
            with open("max.txt", "r", encoding="utf-8") as f:
                lines5 = f.readlines()
                found_lines = []
                for line in lines5:
                    if answer2 in line:
                        found_lines.append(line.strip())

                if len(found_lines) > 0:
                    print(f"Вот что найдено по запросу '{answer2}':")
                    print("\n".join(f"- {line}" for line in found_lines))
                else:
                    print(f"Категория '{search_word}' не найдена.")


        








    answer = input("Выберите пункт: ")
            

        
        
else:
    print("Спасибо, что воспользовались.")