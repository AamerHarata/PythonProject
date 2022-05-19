import numpy as np
from matplotlib import pyplot as plt

import Euler_storVinkel as Euler
import Analytisk_storVinkel as Anal
import Observasjon_storVinkel as Observ

euler_t = Euler.get_data_t()
euler_x = Euler.get_data_x()

analytisk_x = Anal.get_data_x()
analytisk_t = Anal.get_data_t()

observ_x = Observ.get_data_x()
observ_t = Observ.get_data_t()

ax = plt.axes()
plt.axhline(0, color='black')
plt.axvline(0, color='red')

ax.set_xlim((0, max(euler_t)))
ax.set_ylim((-1, 1))
ax.set_title("Stor Vinkel")
euler_x -= np.average(euler_x)
analytisk_x -= np.average(analytisk_x)
observ_x -= np.average(observ_x)

plt.plot(euler_t, euler_x, label="Euler")
plt.plot(observ_t, observ_x, label="Observasjon")
plt.plot(analytisk_t, analytisk_x, label="Analytisk")
plt.legend(loc="upper left")
plt.savefig("Storvinkel.png")
plt.show()

