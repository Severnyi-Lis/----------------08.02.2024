#Упрощенный вариант задачи 1
#Вводится количество и стоимость товара.
#Посчитать сумму за товар.#Вводится количество и стоимость товара.
#Посчитать сумму за товар.
cena=int(input('Введите цену товара'))
kolichestvo=int(input('Введите количество товара'))
summa = cena*kolichestvo
print('Сумма покупки',summa,'рублей') 




#Упрощенный вариант задачи 2
#Вводится количество минут до урока и расстояние в километрах.
#Какая должна быть средняя скорость,чтобы успеть на урок?
minuts=int(input('Время  до академии без пробок '))
minuts_prob= int(input('Время до академии с пробками'))
road= int(input('Расстояние от дома до академии'))
skorost_1=road/minuts
skorost_2 = road/minuts_prob
sr_skorost=(skorost_1+skorost_2)/2
print('Ваша средняя скорость',sr_skorost,'км/мин')




#Упрощенный вариант задачи 3
#Вводится ширина, длина и высота комнаты.
#Рулон обоев 10 метров при ширине 0.5
#Сколько рулонов надо купить?
shirina=int(input('Ширина комнаты'))
dlina = int(input('Длина комнаты'))
visota = float(input('Высота комнаты'))
dlina_rulona = int(input('Длина рулона обоев'))
shirina_rulona = float(input('Ширина рулона обоев'))

perimetr_komnaty=(shirina + dlina)*2
ploshad_sten = perimetr_komnaty*visota
ploshad_rulona = dlina_rulona*shirina_rulona
kolichestvo_rulonov = ploshad_sten/ploshad_rulona
print('количество рулонов',kolichestvo_rulonov,'штук')

