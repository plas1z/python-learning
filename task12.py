import requests
otvet = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
slovar = otvet.json()

class Valuta:
    def __init__(self, kod, name, kurs):
        self.kod = kod
        self.name = name
        self.kurs = kurs

    def __str__(self):
        return f"{self.kod} ({self.name}): {self.kurs:.2f} ₽"

    def is_dorogaya(self):
        return self.kurs > 100

def ask_kod(prompt):
    ok = False
    while not ok:
        text = input(prompt).strip()
        if len(text) > 0:
            ok = True
        else:
            print("Пусто, попробуй ещё")
    return text

spisokvalut = []

while True:
    kod = ask_kod("Код валюты (или стоп):")
    if kod.lower() == "стоп":
        break
    otvet = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    slovar = otvet.json()

    if kod not in slovar["Valute"]:
        print("Такой валюты у ЦБ нет")
        continue 

    name = slovar["Valute"][kod]["Name"]
    kurs = slovar["Valute"][kod]["Value"]

    novaya_valuta = Valuta(kod, name, kurs)
    spisokvalut.append(novaya_valuta)

    res = novaya_valuta.is_dorogaya()
    if res:
        txt = "да"
    else:
        txt = "нет"
    print(f"{novaya_valuta} — дороже 100 ₽: {txt}")





print(f"Спрошено валют: {len(spisokvalut)}")


if len(spisokvalut) > 0:
    champion = max(spisokvalut, key=lambda v: v.kurs)
    print(f"Самая дорогая: {champion.kod}")
else:
    print("Вы не спросили ни одной валюты!")