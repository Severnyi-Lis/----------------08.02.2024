# Получить с клавиатуры год, месяц и день рождения
# посчитать возраст
# Получить с клавиатуры год, месяц и день рождения
# посчитать возраст
# Получить с клавиатуры год, месяц и день рождения
# посчитать возраст
year= input ("введите год рождения")
month=input ("введите месяц рождения")
day=input("введите день рождения")
print (year) #ответ пользователя
print (type(year))#тип ответа-строка! А надо - число!
year_of_birth=int(year)
month_of_birth=int(month)
day_of_birth=int(day)
current_year=2024
current_month= 4
current_day= 9 
age = current_year-year_of_birth
if month_of_birth > current_month:
    age = age - 1
if month_of_birth == current_month:
    if day_of_birth < current_day:
        age = age - 1
        if day_of_birth >= current_day:
            age=age

print("Вам", age, "лет")