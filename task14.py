import requests
import sqlite3

otvet = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
slovar = otvet.json()

conn = sqlite3.connect("kursy.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS kursy (id INTEGER PRIMARY KEY AUTOINCREMENT, kod TEXT, name TEXT, kurs REAL)")
conn.commit()

spisok = ["USD", "EUR", "CNY"]

for kod in spisok:
    name = slovar["Valute"][kod]["Name"]
    kurs = slovar["Valute"][kod]["Value"]
    cur.execute("INSERT INTO kursy (kod, name, kurs) VALUES (?, ?, ?)", (kod, name, kurs))
    conn.commit()
    print(f"{kod} ({name}) - записал")

print(f"\n")

for row in cur.execute("SELECT * FROM kursy"):
    print(f"{row[0]}. {row[1]} - {row[2]} - {row[3]:.2f} ₽")