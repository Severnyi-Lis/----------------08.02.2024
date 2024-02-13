#Задача 1.
#Вводится количество и стоимость товара.
#Посчитать сумму за товар.
tovar= input('Введите количство товара')
cost = input('Введите стоимость товара')
print(tovar)
print(type(tovar))
kolichestvo= int(tovar)
print(cost)
print(type(cost))
cena= int(cost)
total = kolichestvo*cena
print('Сумма покупки',total,'рублей')





#Задача 2.
#Вводится количество минут до урока и расстояние в километрах.
#Какая должна быть средняя скорость,чтобы успеть на урок?
minuts = input('Время до начала урока без пробок')
minuts_prob = input('Время до начала урока если есть пробки')
road = input('Расстояние до академии')
print(minuts,'минут')
print(type(minuts))
time = int(minuts)

print(minuts_prob,'минут')
print(type(minuts_prob))
zaderzhka = int(minuts_prob)

print(road,'километров')
print(type(road))
doroga = int(road)

skorost_1=doroga/time
skorost_2 = doroga/zaderzhka
sr_skorost=(skorost_1+skorost_2)/2

print('Ваша средняя скорость',sr_skorost,'км/мин')




#Задача 3. Вводится ширина, длина и высота комнаты.
#Рулон обоев 10 метров при ширине 0.5
#Сколько рулонов надо купить?
shirina=input('Ширина комнаты')
dlina = input('Длина комнаты')
visota = input('Высота комнаты')
dlina_rulona = input('Длина рулона обоев')
shirina_rulona = input('Ширина рулона обоев')

print(shirina)
print(type(shirina))
shirina=int(shirina)

print(dlina)
print(type(dlina))
dlina=int(dlina)

print(visota)
print(type(visota))
visota=float(visota)# float как я понял используется для чисел с десятичной точкой

print(dlina_rulona)
print(type(dlina_rulona))
dlina_rulona=int(dlina_rulona)

print(shirina_rulona)
print(type(shirina_rulona))
shirina_rulona=float(shirina_rulona)

perimetr_komnaty=(shirina + dlina)*2
ploshad_sten = perimetr_komnaty*visota
ploshad_rulona = dlina_rulona*shirina_rulona
kolichestvo_rulonov = ploshad_sten/ploshad_rulona
print('количество рулонов',kolichestvo_rulonov,'штук')




#Упрощенный вариант задачи 1 
cena=int(input('Введите цену товара'))
kolichestvo=int(input('Введите количество товара'))
summa = cena*kolichestvo
print('Сумма покупки',summa,'рублей')        