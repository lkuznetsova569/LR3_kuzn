# #Общая часть ЛР3
# #Первое задание
# import os
# Secret_1=os.environ['Secret_1']  #Вопрос в рамках 4 задания "что происходит при обращении к os.environ и откуда берётся значение?" 
                                   # Ответ: при обращении к os.environ происходит обращение к переменным окружения, которые хранятся в системе. Значение переменной Secret_1 берется из переменных окружения системы. (Иманбаева)
# print(Secret_1)

# Оставила код Иманбаева для Кузнецовой в рамках выполнения первого задания ЛР3
import os
S1_Imanbaeva=os.environ['S1_Imanbaeva']
print(S1_Imanbaeva)
import os
S2_Imanbaeva=os.environ['S2_Imanbaeva']
print(S2_Imanbaeva)
import os
S3_Imanbaeva=os.environ['S3_Imanbaeva']
print(S3_Imanbaeva)

#Второе задание ЛР3(6 вариант). Делала в команде с Иманбаевой
from sympy import *
k, T, C, L = symbols('k T C L')
Cost = 15000
Amort_lst = []
Cost_lst = []
for i in range(8):
    Am = (C - L) / T #Вопрос в рамках 4 задания "какую формулу реализует эта строка и что означают переменные" 
                    # Ответ: cтрока Am = (C - L) / T реализует формулу линейной амортизации, где C — начальная стоимость, L — ликвидационная стоимость, T — срок полезного использования. (Иманбаева)
    Cost -= Am.subs({C: 15000, L: 0, T: 8})
    Amort_lst.append(round(Am.subs({C: 15000, L: 0, T: 8}), 2))
    Cost_lst.append(round(Cost, 2))
print('Amort_lst:', Amort_lst)
print('Cost_lst:', Cost_lst)

Aj = 0
Cost = 15000
Amort_lst2 = []
Cost_lst2 = []
for i in range(8):
    Am = k * 1 / T * (C - Aj) #Вопрос в рамках 4 задания "почему в цикле для метода уменьшаемого остатка используется переменная Aj и зачем она обновляется?" 
                            # Ответ: Aj накапливает сумму уже начисленной амортизации, чтобы в формуле k * 1/T * (C - Aj) амортизация рассчитывалась от остаточной стоимости (начальная стоимость минус накопленная амортизация). (Иманбаева)
    Cost -= Am.subs({C: 15000, k: 2, T: 8})
    Amort_lst2.append(round(Am.subs({C: 15000, k: 2, T: 8}),2))
    Aj += Am
    Cost_lst2.append(round(Cost, 2))
print('Amort_lst2:', Amort_lst2)
print('Cost_lst2:', Cost_lst2)

#контейнер таблиц
import pandas as pd
Y = range(1, 9)
table1 = list(zip(Y, Amort_lst, Cost_lst))
table2 = list(zip(Y, Amort_lst2, Cost_lst2))
tframe = pd.DataFrame(table1, columns=['Year', 'Amortization', 'Cost'])
tframe2 = pd.DataFrame(table2, columns=['Year', 'Amortization2', 'Cost2'])
print(tframe)
print(tframe2)

#Контейнер графиков
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
plt.plot(tframe['Year'], tframe['Cost'], label='Amortization')
plt.savefig('indiv_chart1.png')
plt.close()
plt.figure()
plt.plot(tframe2['Year'], tframe2['Cost2'], label='Amortization2')
plt.savefig('indiv_chart2.png')
plt.close()

plt.figure()
vals = Amort_lst
labels = [str(i) for i in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       explode=explode,
       autopct='%1.1f%%',
       shadow=True,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },    #Вопрос в рамках 4 задания "что обозначают параметры и что показывает диаграмма?" 
             # Ответ: параметры wedgeprops задают стиль границ секторов (толщина линии, тип штриха, цвет), а круговая диаграмма показывает распределение годовых амортизационных отчислений в процентах. (Иманбаева)
       rotatelabels=True)
ax.axis("equal")
plt.savefig('indiv_piechart1.png')
plt.close()

plt.figure()
vals = Amort_lst2
labels = [str(i) for i in range(1, 9)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       explode=explode,
       autopct='%1.1f%%',
       shadow=True,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': "k"
       },
       rotatelabels=True)
ax.axis("equal")
plt.savefig('indiv_piechart2.png')
plt.close()


table1 = list(zip(Y, Amort_lst))
table2 = list(zip(Y, Amort_lst2))
tfame = pd.DataFrame(table1, columns=['Year', 'Amort_lst'])
tfame2 = pd.DataFrame(table2, columns=['Year', 'Amort_lst2'])
plt.figure()
plt.bar(tfame['Year'], tfame['Amort_lst'])
plt.savefig('indiv_gist1.png')
plt.close()
plt.figure()
plt.bar(tfame['Year'], tfame2['Amort_lst2'])
plt.savefig('indiv_gist2.png')
plt.close()

#Оценка Проверяющего Дубенко С.А.: Расчеты верны, графики и таблицы построены корректно. 5. 

