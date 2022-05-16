import math
import matplotlib.pyplot as plt
import Functions as f
import pandas as pd



data = pd.read_csv('litenvinkel.csv', delimiter='\t')

data_t_init = data['t'].values
data_x_init = data['x'].values

data_x = f.fill_array(data_x_init)
data_t = f.fill_array(data_t_init)
data_angle = f.calculate_angle_deg(data_x)

ax = plt.axes()
plt.axhline(0, color='black')
plt.axvline(0, color='red')

plt.text(0, max(data_angle) + 5, 'Θ / deg', rotation=0)
plt.text(8.2, -17.5, 't / sec', rotation=0)


ax.set_xlim((0, max(data_t)))
ax.set_ylim((-15, 15))

data_v = []
for i in range(len(data_x)):
    data_v.append(data_x[i]*data_t[i])

plt.plot(data_t, data_v)
plt.show()

sum = 0
for x in data_x:
    sum += x
print(sum)