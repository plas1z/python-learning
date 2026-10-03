import requests
import sqlite3

conn = sqlite3.connect("kursy.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS kursy (id INTEGER PRIMARY KEY AUTOINCREMENT, kod TEXT, name TEXT, kurs REAL)")
conn.commit()

spisok = ["USD", "EUR", "CNY"]

while True:
    polzotvet = input("Пункт (1-снимок, 2-история, 3-последний, 4-отчёт, 0-выход):")
    if polzotvet == "1":
        try:
            otvet = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
            slovar = otvet.json()
            for kod in spisok:
                name = slovar["Valute"][kod]["Name"]
                kurs = slovar["Valute"][kod]["Value"]
                cur.execute("INSERT INTO kursy (kod, name, kurs) VALUES (?, ?, ?)", (kod, name, kurs))
                conn.commit()
                print(f"{kod} ({name}) - записал")
        except requests.exceptions.ConnectionError:
            print("Нет интернета, снимок не сделан")
            continue
    elif polzotvet == "2":
        for row in cur.execute("SELECT * FROM kursy"):
            print(f"{row[0]}. {row[1]} - {row[2]} - {row[3]:.2f} ₽")

    elif polzotvet == "3":
        for row in cur.execute("SELECT * FROM kursy ORDER BY id DESC LIMIT 3"):
            print(f"{row[0]}. {row[1]} - {row[2]} - {row[3]:.2f} ₽")
    elif polzotvet == "0":
        print("Пока")
        break
    elif polzotvet == "4":
        kod = input("Какой код?: ").strip().upper()
        cur.execute("SELECT COUNT(*) FROM kursy WHERE kod = ?", (kod,))
        otvet1 = cur.fetchone() 
        skolko = otvet1[0]
        if skolko == 0:
            print("Такой валюты нет в истории")
        else:
            cur.execute("SELECT AVG(kurs) FROM kursy WHERE kod = ?", (kod,))
            otvet2 = cur.fetchone()

            cur.execute("SELECT MAX(kurs) FROM kursy WHERE kod = ?", (kod,))
            otvet3 = cur.fetchone()

            cur.execute("SELECT MIN(kurs) FROM kursy WHERE kod = ?", (kod,))
            otvet4 = cur.fetchone()
            print(f"Снимков: {otvet1[0]}")
            print(f"Средний курс: {otvet2[0]:.2f} ₽")
            print(f"Максимум: {otvet3[0]:.2f} ₽")
            print(f"Минимум: {otvet4[0]:.2f} ₽")
    else:
        print("Нет такого пункта")







