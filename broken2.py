

class Expense:
    def __init__(self, category, summa):
        self.category = category
        self.summa = summa

    def describe(self):
        print(f"{self.category} — {self.summa:.2f} ₽")


e = Expense("чай", 120)
e.describe()
print(e.summa)