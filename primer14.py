import requests
import sqlite3

GORODA = {
    "москва": (55.75, 37.62),
    "питер": (59.94, 30.31),
    "сочи": (43.60, 39.73),
}

conn = sqlite3.connect("pogoda.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS zametki (id INTEGER PRIMARY KEY AUTOINCREMENT, gorod TEXT, temp REAL, veter REAL)")
conn.commit()

for gorod in GORODA:
    koord = GORODA[gorod]
    url = f"https://api.open-meteo.com/v1/forecast?latitude={koord[0]}&longitude={koord[1]}&current_weather=true"
    try:
        otvet = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Нет интернета, опрос прерван")
        break
    if otvet.status_code != 200:
        print(f"{gorod}: сайт ответил кодом {otvet.status_code}, пропускаю")
        continue
    slovar = otvet.json()
    temp = slovar["current_weather"]["temperature"]
    veter = slovar["current_weather"]["windspeed"]
    cur.execute("INSERT INTO zametki (gorod, temp, veter) VALUES (?, ?, ?)", (gorod, temp, veter))
    conn.commit()
    print(f"{gorod}: {temp}°C, ветер {veter} км/ч — записал")

print()
for row in cur.execute("SELECT * FROM zametki"):
    print(f"{row[0]}. {row[1]} — {row[2]}°C, ветер {row[3]} км/ч")
