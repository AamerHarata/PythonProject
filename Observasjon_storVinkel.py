import math

import matplotlib.pyplot as plt
import Functions as f
import pandas as pd



data = pd.read_csv('storvinkel.csv', delimiter='\t')

data_t_init = data['t'].values
data_x_init = data['x'].values

data_x = f.fill_array(data_x_init)
data_t = f.fill_array(data_t_init)
data_angle = f.calculate_angle_deg(data_x)


k = 0.399
m = 0.034
b = 0.0042
w_p = math.sqrt(k / m - b ** 2 / (4 * m ** 2))
#w_p = math.sqrt(9.81/0.85)
print(w_p)
A = 0.448+0.039

calc_x = []

for t in data_t:
    x = A * math.exp(-b / (2 * m) * t) * math.cos(w_p * t - 0.76) - 0.022
    calc_x.append(x)

ax = plt.axes()
plt.axhline(0, color='black')
plt.axvline(0, color='red')

plt.text(0, max(data_angle) + 5, 'x', rotation=0)
plt.text(8.2, -17.5, 't / sec', rotation=0)

ax.set_xlim((0, max(data_t)))
ax.set_ylim((-2, 2))

plt.plot(data_t, calc_x)
plt.plot(data_t, data_x)
plt.show()
