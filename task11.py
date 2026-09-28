

class Fighter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def describe(self):
        print(f"{self.name}: {self.hp} hp, атака {self.power}")

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power
        print(f"{self.name} бьет: -{self.power} → {enemy.name} {enemy.hp} hp")

    def __str__(self):
        return f"{self.name} [{self.hp} hp, атака {self.power}]"

    def is_alive(self):
        return self.hp > 0

def ask_count(prompt):
    ok = False
    while not ok:
        text = input(prompt).strip()
        try:
            x = int(text)
            if x >= 2:
                ok = True
            else:
                print("Нужно хотя бы двое бойцов")
        except ValueError:
            print("Это не число")
    return x

def ask_number(prompt):
    ok = False
    while not ok:
        text = input(prompt).strip()
        try:
            x = float(text)
            if x > 0:
                ok = True
            else:
                print("Должно быть больше 0")
        except ValueError:
            print("Это не число")
    return x

listfighters = []
skolko = ask_count("Сколько бойцов: ")
for n in range(skolko):
    name = input("Имя бойца: ").strip()
    hp = ask_number("Сколько здоровья?: ")
    ataka = ask_number("Сколько атака?: ")
    listfighters.append(Fighter(name, hp, ataka))


print("=== ТУРНИР ===")


for i in range(len(listfighters)):
    print(f"{i + 1}. {listfighters[i]}")


print("---")

alive = 0
for f in listfighters:
    if f.is_alive():
        alive = alive + 1
    else:
        pass
        
while alive > 1:
    for i in range(len(listfighters)):
        if listfighters[i].is_alive():
            if i == len(listfighters) - 1:
                sled = 0
            else:
                sled = i + 1

            if listfighters[sled].is_alive():
                listfighters[i].attack(listfighters[sled])
    alive = 0
    for f in listfighters:
        if f.is_alive():
            alive = alive + 1
        else:
            pass

print("---")
print("ИТОГ")

for i in range(len(listfighters)):
    print(f"{i + 1}. {listfighters[i]}")


for f in listfighters:
    if f.is_alive():
        print(f"Победитель: {f.name} ")
    else:
        pass





