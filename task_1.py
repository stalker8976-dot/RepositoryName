money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0 # Месяц
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    pacxod = spend - salary
    if pacxod > money_capital:
        break
    months += 1
    money_capital -= pacxod
    spend *= 1 + increase
print("Количество месяцев, которое можно протянуть без долгов:", months)
