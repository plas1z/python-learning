import sqlite3
import hashlib
from fastapi import FastAPI
app = FastAPI()

conn = sqlite3.connect("sklad.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS rabotniki (id INTEGER PRIMARY KEY AUTOINCREMENT, imya TEXT, kod_hech TEXT)")
conn.commit()

def sdelat_hech(slovo):
    hech = hashlib.sha256(slovo.encode()).hexdigest()
    return hech

@app.post("/zayavka")
def zayavka(dannye: dict):
    imya = dannye["imya"]
    kod = dannye["kod"]
    hech = sdelat_hech(kod)
    cur.execute("INSERT INTO rabotniki (imya, kod_hech) VALUES (?, ?)", (imya, hech))
    conn.commit()
    return {"zapishem": imya}

@app.post("/vhod")
def vhod(dannye: dict):
    imya = dannye["imya"]
    kod = dannye["kod"]
    cur.execute("SELECT kod_hech FROM rabotniki WHERE imya = ?", (imya,))
    row = cur.fetchone()
    if row is None:
        return {"otvet": "net takogo rabotnika"}
    hech_bazy = row[0]
    hech_prishel = sdelat_hech(kod)
    if hech_prishel == hech_bazy:
        return {"otvet": "prohodi"}
    else:
        return {"otvet": "kod nevernyi"}
