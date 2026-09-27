# Урок 11. ОБРАЗЕЦ: __str__ — красивая печать объекта, is_alive — вопрос-метод

class Fighter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def __str__(self):                      # МАГИЯ №2: зовётся при print(объект)
        return f"{self.name} [{self.hp} hp, атака {self.power}]"

    def attack(self, enemy):
        enemy.hp = enemy.hp - self.power
        print(f"{self.name} бьёт: -{self.power} → {enemy.name} {enemy.hp} hp")

    def is_alive(self):                     # метод-вопрос: отвечает да/нет
        return self.hp > 0


a = Fighter("Рыцарь", 100, 30)
b = Fighter("Дракон", 120, 25)

# Без __str__ печатались бы адреса (<__main__.Fighter object at 0x...>).
# Теперь print сам зовёт __str__ и печатает то, что он вернул:
print(a)
print(b)

# is_alive возвращает True/False — можно класть прямо в if и в while:
print(a.is_alive())          # True
a.hp = 0                     # рыцаря подкосили
print(a.is_alive())          # False
if a.is_alive():
    print("жив")
else:
    print("мёртв")
