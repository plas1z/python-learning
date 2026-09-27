


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


knight = Fighter("Рыцарь", 100, 30)
dragon = Fighter("Дракон", 120, 25)
fighters = [knight, dragon]
        
def print_all(fighters):
    n = 0
    for f in fighters:
        n = n + 1
        print(f"{n}. {f.name}: {f.hp} hp, атака {f.power}")


print("=== БИТВА ===")
print_all(fighters)
print("---")


while knight.hp > 0 and dragon.hp > 0:
    knight.attack(dragon)
    if dragon.hp > 0:
        dragon.attack(knight)
    else:
        print(f"{dragon.name} повержен!")
print("---")
print("ИТОГ")
print_all(fighters)
for f in fighters:
    if f.hp > 0:
        print(f"{f.name} - победил")
    else:
        pass





