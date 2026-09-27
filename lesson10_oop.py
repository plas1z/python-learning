# Урок 10. ОБРАЗЕЦ: класс — свой тип данных с поведением
# На твоём домене: подписка VPN.

class Subscription:                      # class = ЧЕРТЁЖ нового типа
    def __init__(self, email, price, days):   # конвейер рождения: срабатывает при создании
        self.email = email               # self = «эта конкретная коробка»
        self.price = price
        self.days = days
        self.status = "trial"            # поле с начальным значением

    def activate(self):                  # метод — функция внутри класса
        self.status = "active"           # первый параметр метода — ВСЕГДА self

    def describe(self):
        print(f"{self.email}: {self.status}, {self.days} дн., {self.price:.2f} ₽")


# Класс — чертёж. Объект (экземпляр) — конкретная вещь, сделанная по нему.
# Вызов класса = «сделай мне одну такую» → __init__ заполняет ЕЁ поля.
sub1 = Subscription("vasya@mail.ru", 499.0, 30)
sub2 = Subscription("kate@mail.ru", 2199.0, 90)

sub1.describe()            # у каждого объекта СВОИ поля
sub2.describe()

sub1.activate() 
#sub2.activate()
sub2.describe()           # первая оплатила — статус меняется ТОЛЬКО у неё
sub1.describe()
sub2.describe()            # вторая не тронута

print(sub1.status)         # поле читается снаружи через точку
print(sub1 == sub2)        # два объекта — две разные коробки, даже с одинаковыми полями
