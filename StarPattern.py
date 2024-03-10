import matplotlib.pyplot as plt

def draw_star(ax, x, y, size):
    ax.plot(x, y, marker='*', markersize=size, linestyle='None', color='blue')

# Create a figure and axis
fig, ax = plt.subplots()

# Define star positions and sizes
star_data = [
    (1, 1, 100),
    (2, 3, 80),
    (4, 5, 120),
    (5, 2, 90),
    (3, 4, 110)
]

# Draw stars
for x, y, size in star_data:
    draw_star(ax, x, y, size)

# Set limits
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)

# Add labels and title
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_title('Star Pattern')

# Show plot
plt.grid(True)
plt.show()
