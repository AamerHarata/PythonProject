import math
import matplotlib.pyplot as plt
import numpy as np
import Functions as f
import pandas as pd


g = 9.81

data = pd.read_csv('storvinkel.csv', delimiter='\t')

data_t_init = data['t'].values
data_x_init = data['x'].values

data_x = f.fill_array(data_x_init)
data_t = f.fill_array(data_t_init)
data_angle = f.calculate_angle_deg(data_x)

v0 = 0
x0 = data_x[0]
a0 = g*math.sin(data_angle[0])

a1 = g*math.sin(data_angle[1])

v1 = v0 + a1*(data_t[1] - data_t[0])
x1 = x0 + v1*(data_t[1] - data_t[0])
#a = np.zeros(len(data_angle))
a = [g*math.sin(math.radians(data_angle[0]))]
v = [0]
x = [data_x[0]]
k = 0.005
m = 0.034
l = 0.825

for i in range(1, len(data_angle)):
    d_time = data_t[i] - data_t[i-1]
    #a_n = g * math.sin(math.radians(data_angle[i]))
    a_n = -g/l * x[i-1] - k / m * v[i-1]
    a.append(a_n)

    v_n = v[i-1] + a[i]*d_time
    v.append(v_n)

    x_n = x[i-1] + v[i] * d_time
    x.append(x_n)


# for i in range(len(v)):
#     print(f"angle: {data_angle[i]}, x: {x[i]}")
    #print(v[i])


ax = plt.axes()
plt.axhline(0, color='black')
plt.axvline(0, color='red')

# plt.text(0, max(data_angle) + 5, 'Θ / deg', rotation=0)
# plt.text(8.2, -17.5, 't / sec', rotation=0)


ax.set_xlim((0, max(data_t)))
ax.set_ylim((-1, 1))

# Euler method plot
plt.plot(data_t, x)
data_x -= np.average(data_x)
# Analytisk method plot

plt.show()