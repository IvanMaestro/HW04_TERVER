# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
a = 'больше 182 см'
b = 'больше 190 см'
c = 'от 166 см до 190 см'
d = 'от 166 см до 182 см'
e = 'от 158 см до 190 см'
f = 'не выше 150 см или не ниже 190 см'
g = 'не выше 150 см или не ниже 198 см'
h = 'ниже 166 см.'

mu = 174
std = 8

z_a = (182 - mu) / std
p_a = z_a - 0.84134
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {a}: {round(p_a, 5)}')

z_b = (190 - mu) / std
p_b = z_b - 0.97725
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {b}: {round(p_b,5)}')

z_c1 = (166 - mu) / 8
z_c2 = (190 - mu) / 8
p_c = 0.97725 - 0.1587
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {c}: {round(p_c,5)}')

z_d1 = (166 - 174) / 8
z_d2 = (182 - 174) / 8
p_d = 0.84134 - 0.1587
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {d}: {round(p_d,5)}')

z_e1 = (158 - 174) / 8
z_e2 = (190 - 174) / 8
p_e = 0.97725 - 0.0228
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {e}: {round(p_e,5)}')

z_f1 = (150 - 174) / 8
z_f2 = (190 - 174) / 8
p_f = 0.0014 + (1 - 0.97725)
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {f}: {round(p_f,5)}')

z_g1 = (150 - 174) / 8
z_g2 = (198 - 174) / 8
p_g = 0.0014 + (1 - 0.99865)
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {g}: {round(p_g,5)}')

z_b = (166 - mu) / std
p_h = 0.1587
print(f'Вероятность того, что случайным образом выбранный взрослый человек имеет рост {h}: {round(p_h,5)}')
