money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital + salary >= spend: #While птому что ма не знаем заранее, сколько месяцев будет в итоге
    money_capital += salary - spend
    count += 1
    spend = spend + spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", count )
