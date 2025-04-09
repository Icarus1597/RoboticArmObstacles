import numpy as np
import matplotlib.pyplot as plt

# Define positions
blue_point = np.array([4, 0])   # Coxa link
red_point = np.array([0, 3])    # Target point
yellow_circle_center = np.array([3, 2])  # Obstacle
blue_point_target_position = np.array([4, -2])

# Vector Coxa link to obstacle
vector = yellow_circle_center - blue_point  
unit_vector = vector / np.linalg.norm(vector)  # Norm

# Orthogonale Linie: 90° Drehung des Vektors
perp_vector = np.array([-unit_vector[1], unit_vector[0]])  
perp_length = 2  # Länge der orthogonalen Linie
perp_end = blue_point + perp_length * perp_vector  # Endpunkt der orthogonalen Linie

# Figur erstellen
fig, ax = plt.subplots(figsize=(6,6))

# Punkte plotten
ax.scatter(*blue_point, color='blue', s=100, label="Blauer Punkt")
ax.scatter(*red_point, color='red', s=100, label="Roter Punkt")
ax.scatter(*perp_end, color='blue', s=100, label="Orthogonaler Punkt")
ax.scatter(*blue_point_target_position, color = 'blue', s=100, label="Femur Link Target", alpha=0.5)


# Gelber Kreis zeichnen
circle = plt.Circle(yellow_circle_center, 0.5, fc='y', alpha=1)
ax.add_patch(circle)

# Pfeil vom blauen Punkt zum roten Punkt
ax.annotate("", xy=red_point, xytext=blue_point,
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.5))

# Gerade vom blauen Punkt zum Mittelpunkt des gelben Kreises
ax.plot([blue_point[0], yellow_circle_center[0]], [blue_point[1], yellow_circle_center[1]], 'k-', linewidth=1)
center_vector = (yellow_circle_center - blue_point)

# Orthogonale blaue Linie
ax.plot([blue_point[0], perp_end[0]], [blue_point[1], perp_end[1]], 'b-', linewidth=2)

# Current Position Coxa Joint 
ax.plot([blue_point[0], blue_point_target_position[0]], [blue_point[1], blue_point_target_position[1]], 'b-', linewidth = 2, alpha=0.5)

# Achsen ausblenden
ax.set_xlim(-3, 6)
ax.set_ylim(-3, 5)
ax.set_aspect('equal')
ax.axis("off")

# Speichern als Vektorgrafik
plt.savefig("./PDF_Figures/sp_geometry_normal_case.pdf")

# Anzeigen
#plt.show()
