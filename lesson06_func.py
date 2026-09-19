# Урок 6. ОБРАЗЕЦ: функции — свои собственные команды
# Ты уже пользовался чужими: input(), print(), len(), sum().
# def позволяет СДЕЛАТЬ СВОЮ.

def delivery_cost(total):          # def = «определи команду»: имя + входы в скобках
    if total >= 5000:              # тело — с отступом, как у if/while
        return 0                   # return = «вот результат» — и выйти
    elif total >= 2000:
        return 150
    else:
        return 300

def greet(name, hour):             # входов может быть несколько, через запятую
    if hour < 12:
        return f"Доброе утро, {name}!"
    return f"Добрый день, {name}!"

# Вызов: имя + скобки + данные. Пока не вызовешь — код внутри не работает.
print(greet("Саша", 9))
print(greet("Ника", 15))

check = 3150.0
d = delivery_cost(check)           # то, что вернул return, легло в d
print(f"Чек {check:.2f} + доставка {d} = {check + d:.2f} ₽")
