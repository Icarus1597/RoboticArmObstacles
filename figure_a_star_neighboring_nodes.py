import matplotlib.pyplot as plt
import numpy as np
import time

# Define the center point
center = (0, 0)

# Define the eight directions (N, S, E, W, NE, NW, SE, SW)
directions = [
    (0, 1),    # North
    (0, -1),   # South
    (1, 0),    # East
    (-1, 0),   # West
    (1, 1),    # North-East
    (-1, 1),   # North-West
    (1, -1),   # South-East
    (-1, -1)   # South-West
]

# Normalize the diagonal directions to ensure they have a length of 1
directions = [(dx / np.linalg.norm([dx, dy]), dy / np.linalg.norm([dx, dy])) if dx != 0 and dy != 0 else (dx, dy) for dx, dy in directions]

# Create the plot
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Plot the center point
ax.plot(center[0], center[1], 'go', markersize=10)  # Green dot for the center

# Plot arrows from the center to the eight neighboring nodes
for direction in directions:
    ax.plot(direction[0], direction[1], 'go', markersize=10)
    ax.arrow(center[0], center[1], direction[0], direction[1], head_width=0.1, head_length=0.15, fc='blue', ec='blue')

# Set grid and labels
#ax.grid(True)
#ax.set_xticks(np.arange(-2, 2, 1))
#ax.set_yticks(np.arange(-2, 2, 1))

# Add labels
#ax.text(center[0] + 0.15, center[1] + 0.15, 'Center', fontsize=12)

# Show the plot
#plt.title('A* Algorithm Visualization - Center Point with 8 Directions')
plt.show()
#plt.savefig("AStarVis.pdf", )
timestamp = time.strftime("%Y%m%d_%H%M%S")
filename = f"./PDF_Figures/AStarNeighbours_{timestamp}.pdf"
#fig.savefig(filename, bbox_inches='tight')
