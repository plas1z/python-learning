from fastapi import FastAPI
app = FastAPI()
from fastapi.responses import HTMLResponse

import sqlite3

conn = sqlite3.connect("kursy.db", check_same_thread=False)
cur = conn.cursor()


@app.get("/")
def func1():
    cur.execute("SELECT COUNT(*) FROM kursy")
    row = cur.fetchone()
    skolko = row[0]
    return {"имя сервера —": "«Пульс валют»", "снимков": skolko}

@app.get("/poslednij")
def func2():
    kopilka = []
    for row in cur.execute("SELECT * FROM kursy ORDER BY id DESC LIMIT 3"):
        kod = row[1]
        kurs = row[3]
        kopilka.append({"kod": kod, "kurs": kurs})
    return kopilka

@app.get("/valuta/{kod}")
def valuta(kod: str):
    kod = kod.upper()
    cur.execute("SELECT COUNT(*) FROM kursy WHERE kod = ?", (kod,))
    otvet = cur.fetchone()
    skolko = otvet[0]
    if skolko == 0:
        return("Такой валюты нет в истории")
    else:
        cur.execute("SELECT AVG(kurs) FROM kursy WHERE kod = ?", (kod,))
        otvet1 = cur.fetchone()
        cur.execute("SELECT MAX(kurs) FROM kursy WHERE kod = ?", (kod,))
        otvet2 = cur.fetchone()
        cur.execute("SELECT MIN(kurs) FROM kursy WHERE kod = ?", (kod,))
        otvet3 = cur.fetchone()
    return {"kod": kod, "снимков -": skolko, "средний": otvet1[0], "Максимум": otvet2[0], "Минимум": otvet3[0]}
    

@app.get("/stranica")
def func3():
    kopilka2 = []
    for row in cur.execute("SELECT * FROM kursy ORDER BY id DESC LIMIT 3"):
        kod = row[1]
        name = row[2]
        kurs = row[3]
        x = f"<tr><td>{kod}</td><td>{name}</td><td>{kurs:.2f} ₽</td></tr>"
        kopilka2.append(x)
    stroki = "".join(kopilka2)

    shapka = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Курсы валют</title>
        <style>
            body {
                background-color: #f0f4f8;
                font-family: Arial, Helvetica, sans-serif;
                color: #333333;
            }
            h1 {
                color: #1a5fb4;
            }
            h2 {
                color: #1a5fb4;
            }
            table {
                border-collapse: collapse;
            }
            td {
                border: 1px solid #999999;
                padding: 8px 16px;
                font-size: small;
            }
            .shapka {
                font-weight: bold;
                background-color: #e8f0fe;
                text-align: center;

            }

        </style>
    </head>"""

    body = f"""
    <body>
        <h1>Курсы валют</h1>
        <p>Источник — <strong>Банк России</strong> снимок от 4 октября</p>

        <h2>Сегодняшний снимок</h2>
        <table>
            <tr class="shapka"><td>Код</td><td>Имя</td><td>Курс</td></tr>
            {stroki}
        </table>
        <p>Факты</p>
        <ul>
            <li>Доллар стабилен</li>
            <li>Евро стабилен</li>
        </ul>
        <p><a href="https://www.cbr-xml-daily.ru/daily_json.js">Данные ЦБ (JSON)</a></p>

</body>


</html>"""

    stranica = shapka + body
    return HTMLResponse(stranica)





        