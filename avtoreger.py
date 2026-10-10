import requests




def ask_amount(prompt):
    ok = False
    while not ok:
        text = input(prompt).strip()
        try:
            textfloat = int(text)
            if textfloat > 0:
                ok = True
            else:
                print("Должно быть больше 0")
        except ValueError:
            print("Это не целое число")
    return textfloat

skolko = ask_amount("Сколько: ")

uspex = 0
fail = 0

for n in range(skolko):
    mail = f"bot{n}@test.local"
    passwrd = f"pass{n}!test"
    otvet = requests.post("http://127.0.0.1:8000/register", json={"email": mail, "passwrd": passwrd})
    if otvet.status_code == 200:
        uspex = uspex + 1
    else:
        fail = fail +1
        print(f"Круг номер {n} не прошёл")

print()
print(f"Регистраций прошло - {uspex}")
print(f"Ошибок - {fail}")
    