import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
x, y = [], []
line, = ax.plot([], [], lw=2)

def update(frame):
    x.append(frame)
    y.append(np.sin(frame/2))
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return line,

ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 20, 0.5), blit=True)
plt.show()
