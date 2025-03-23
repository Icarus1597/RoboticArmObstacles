import numpy as np
import matplotlib.pyplot as plt

# Punkte definieren
blue_point = np.array([4, 0])   # Unten rechts
red_point = np.array([0, 3])    # Oben links
yellow_circle_center = np.array([2, 4])  # Oben mittig

# Vektor von blauem Punkt zum gelben Kreis
vector = yellow_circle_center - blue_point  
unit_vector = vector / np.linalg.norm(vector)  # Normieren für Richtungsvektor

# Orthogonale Linie: 90° Drehung des Vektors
perp_vector = np.array([-unit_vector[1], unit_vector[0]])  
perp_length = 1  # Länge der orthogonalen Linie
perp_end = blue_point + perp_length * perp_vector  # Endpunkt der orthogonalen Linie

# Figur erstellen
fig, ax = plt.subplots(figsize=(6,6))

# Punkte plotten
ax.scatter(*blue_point, color='blue', s=100, label="Blauer Punkt")
ax.scatter(*red_point, color='red', s=100, label="Roter Punkt")
ax.scatter(*yellow_circle_center, color='yellow', s=300, edgecolors='black', label="Gelber Kreis")
ax.scatter(*perp_end, color='blue', s=100, edgecolors='black', label="Orthogonaler Punkt")

# Gelber Kreis zeichnen
circle = plt.Circle(yellow_circle_center, 0.5, color='yellow', alpha=0.5, edgecolor="black")
ax.add_patch(circle)

# Pfeil vom blauen Punkt zum roten Punkt
ax.annotate("", xy=red_point, xytext=blue_point,
            arrowprops=dict(arrowstyle="->", color="black", linewidth=1.5))

# Beschriftungen "Left" und "Right"
mid_arrow = (blue_point + red_point) / 2
ax.text(mid_arrow[0] - 0.2, mid_arrow[1] + 0.2, "Left", fontsize=12, verticalalignment="bottom")
ax.text(mid_arrow[0] + 0.2, mid_arrow[1] - 0.2, "Right", fontsize=12, verticalalignment="top")

# Gerade vom blauen Punkt nach rechts
ax.plot([blue_point[0], blue_point[0] + 2], [blue_point[1], blue_point[1]], 'k-', linewidth=2)

# Gerade vom blauen Punkt zum Mittelpunkt des gelben Kreises
ax.plot([blue_point[0], yellow_circle_center[0]], [blue_point[1], yellow_circle_center[1]], 'k-', linewidth=2)

# Orthogonale blaue Linie
ax.plot([blue_point[0], perp_end[0]], [blue_point[1], perp_end[1]], 'b-', linewidth=2)

# Winkelbogen für Alpha (zwischen den beiden Geraden)
angle_range = np.linspace(0, np.arccos(np.dot(unit_vector, [1, 0])), 30)  
arc_x = blue_point[0] + 0.5 * np.cos(angle_range)
arc_y = blue_point[1] + 0.5 * np.sin(angle_range)
ax.plot(arc_x, arc_y, 'r', linewidth=1.5)

# Winkel-Beschriftung "α"
ax.text(blue_point[0] + 0.6, blue_point[1] + 0.2, r"$\alpha$", fontsize=14, color="red")

# Rechter Winkel markieren mit kleinem Quadrat
offset = 0.3 * perp_vector
square_x = [perp_end[0], perp_end[0] - offset[0], blue_point[0] - offset[0], blue_point[0]]
square_y = [perp_end[1], perp_end[1] - offset[1], blue_point[1] - offset[1], blue_point[1]]
ax.plot(square_x, square_y, 'b-', linewidth=2)

# Achsen ausblenden
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 5)
ax.set_aspect('equal')
ax.axis("off")

# Speichern als Vektorgrafik
#plt.savefig("geometrie_final.svg", format="svg")

# Anzeigen
plt.show()
