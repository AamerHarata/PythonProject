import matplotlib.pyplot as plt
import Functions as f
import pandas as pd



data = pd.read_csv('litenvinkel.csv', delimiter='\t')

data_t_init = data['t'].values
data_x_init = data['x'].values

data_x = f.fill_array(data_x_init)
data_t = f.fill_array(data_t_init)
data_angle = f.calculate_angle_deg(data_x)

# ax = plt.axes()
# plt.axhline(-2, color='black')
# plt.axvline(0, color='black')
# plt.text(0, max(data_angle) + 5, 'Θ / deg', rotation=0)
# plt.text(8.5, -32.5, 't / sec', rotation=0)
# ax.set_xlim((0, max(data_t)))
# ax.set_ylim(-(max(data_angle) + 3), max(data_angle) + 3)

# plt.plot(data_t, data_x)
# plt.show()
def get_data_t():
    return data_t


def get_data_x():
    return data_x