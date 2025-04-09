import numpy as np
import matplotlib.pyplot as plt
from autograd import grad
import autograd.numpy as anp  # autograd-kompatibles numpy
import PotentialFields as pf
import config
import matplotlib.patches as patches

config.center = (0, 0)
config.radius = 2

# ---- PLOTTING ----
# Gitterpunkte für das Feld
x = np.linspace(-10, 10, 40)
y = np.linspace(-10, 10, 40)
X, Y = np.meshgrid(x, y)

# Initialisiere Arrays für die Vektoren
U = np.zeros_like(X)  # x-Komponente des Vektors
V = np.zeros_like(Y)  # y-Komponente des Vektors

# Zielposition und Stärke der Attraktion
pos_target = (0, 0)  # Ziel in der Mitte
zeta = 1  # Attraktive Potenzialstärke

# Berechnung der Vektorfeld-Werte
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        pos_ee = (X[i, j], Y[i, j])
        # v = pf.v_att_function(pos_ee, pos_target, zeta)
        v = pf.v_rep_function(pos_ee, config.rho_0, config.k)
        U[i, j], V[i, j] = v  # x- und y-Komponenten speichern

# Quiver-Plot für das Vektorfeld
plt.figure(figsize=(6, 6))
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=10, color='b')

# Adding a yellow circle to the plot
circle = patches.Circle(config.center, radius=config.radius, color='yellow', alpha=1)
plt.gca().add_patch(circle)  # Add the circle to the current axis

# Optional: Ziel markieren
# plt.plot(pos_target[0], pos_target[1], 'ro', markersize=8, label="Target")  # Ziel markieren
# plt.xlabel("X-Position")
# plt.ylabel("Y-Position")
# plt.title("Repulsive Vector Field with Yellow Circle")
# plt.legend()
# plt.grid()

#plt.show()
plt.savefig("./PDF_Figures/RepVectorFieldWithObstacle.pdf", bbox_inches='tight')
