import sqlite3
import time
from fastapi import FastAPI
app = FastAPI()
jurnal = []
from fastapi.responses import JSONResponse
code429 = JSONResponse(status_code=429, content={"otvet": "slishkom chasto, podozhdi"})


conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, passwrd TEXT)")
conn.commit()

@app.post("/register")
def reg(dannye: dict):
    global jurnal
    email = dannye["email"]
    passwrd = dannye["passwrd"]
    now = time.time()
    new = []
    for otmetka in jurnal:
        if now - otmetka < 10:
            new.append(otmetka)
    jurnal = new
        

    if len(jurnal) >= 3:
        return(code429)

    jurnal.append(now)


    cur.execute("INSERT INTO users (email, passwrd) VALUES (?, ?)", (email, passwrd))
    conn.commit()
    return {"зарегистрирован": email}

@app.get("/")
def func1():
    cur.execute("SELECT COUNT(*) FROM users")
    row = cur.fetchone()
    skolko = row[0]
    return{"Юзеров -": skolko}