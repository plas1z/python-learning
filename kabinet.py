import sqlite3
from fastapi import FastAPI
app = FastAPI()


conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, passwrd TEXT)")
conn.commit()

@app.post("/register")
def reg(dannye: dict):
    email = dannye["email"]
    passwrd = dannye["passwrd"]

    cur.execute("INSERT INTO users (email, passwrd) VALUES (?, ?)", (email, passwrd))
    conn.commit()
    return {"зарегистрирован": email}

@app.get("/")
def func1():
    cur.execute("SELECT COUNT(*) FROM users")
    row = cur.fetchone()
    skolko = row[0]
    return{"Юзеров -": skolko}