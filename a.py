import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

v0 = 10
a = 24

t = np.linspace(0, 10, 100)
v = v0 + a * t

plt.plot(t, v, label=f'v = {v0} + {a}t')
plt.scatter(0, v0, color='red', label='Initial velocity')
plt.title('Constant Acceleration Velocity-Time Graph')
plt.xlabel('Time (seconds)')
plt.ylabel('Velocity (m/s)')
plt.grid(True)
plt.legend()

# y축 눈금을 10 단위로 지정
plt.gca().yaxis.set_major_locator(MultipleLocator(10))

plt.show()
