import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)

# Create empty line
line, = ax.plot([], [], lw=2)

# Generate x values
x = np.linspace(0, 10, 500)

# Create zig-zag function
def zigzag(x, shift):
    return np.sign(np.sin(5 * (x + shift)))

# Update function
def update(frame):
    y = zigzag(x, frame)
    line.set_data(x, y)
    return line,

# Animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 100),
                    interval=50, blit=True)

plt.title("Animated Zig-Zag Line")
plt.show()
