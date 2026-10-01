import sqlite3
conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, category  TEXT, amount  REAL)")
conn.commit()

def ask_amount(prompt):
    ok = False
    while not ok:
        text = input(prompt).strip()
        try:
            textfloat = float(text)
            if textfloat > 0:
                ok = True
            else:
                print("Должно быть больше 0")
        except ValueError:
            print("Это не число")
    return textfloat

vibor = input("Пункт (1-трата, 2-все, 0-выход): ")
while vibor != "0":
    if vibor == "1":
        kategoria = input("Категория: ")
        while kategoria != "стоп":
                summa = ask_amount("Сумма: ")
                cur.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (kategoria, summa))
                conn.commit()
                kategoria = input("Категория: ")
    elif vibor == "2":
        for row in cur.execute("SELECT * FROM expenses"):
            print(f"{row[0]}. {row[1]} — {row[2]:.2f} ₽")
    else:
        print("Нет такого пункта")
    vibor = input("Пункт (1-трата, 2-все, 0-выход): ")
print("Пока")

