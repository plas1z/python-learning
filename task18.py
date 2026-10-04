from fastapi import FastAPI
app = FastAPI()

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
    

