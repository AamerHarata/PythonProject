import numpy as np
from matplotlib import pyplot as plt

import Euler_storVinkel as Euler
import Analytisk_storVinkel as Observ

euler_t = Euler.get_data_t()
euler_x = Euler.get_data_x()

observ_x = Observ.get_data_x()
observ_t = Observ.get_data_t()

ax = plt.axes()
plt.axhline(0, color='black')
plt.axvline(0, color='red')

ax.set_xlim((0, max(euler_t)))
ax.set_ylim((-1, 1))

euler_x -= np.average(euler_x)
observ_x -= np.average(observ_x)

plt.plot(euler_t, euler_x)
plt.plot(observ_t, observ_x)
plt.show()
