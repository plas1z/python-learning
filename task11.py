# task11 — Урок 11, Этап 1: прокачка класса
# Твой класс из task10 (копия). Задача: добавить __str__ и is_alive
# (образец — в lesson11_oop2.py), затем создать трёх бойцов и
# напечатать каждого ОДНИМ print(боец) — карточкой.

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

    # ↓↓↓ сюда добавь __str__ (return строки, не print!)
    # ↓↓↓ и is_alive (return self.hp > 0)


# ↓↓↓ сюда — трёх бойцов (Рыцарь 100/30, Дракон 120/25, Гоблин 40/10)
# и печать каждого одним print(имя_переменной)
