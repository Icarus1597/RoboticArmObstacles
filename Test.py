import config
import numpy as np


PI = np.pi

# 1. Spalte: Ausgestreckt nach rechts
print("Erste Spalte 0, 0, 0")
config.theta_coxa = 0
config.theta_femur = 0
config.theta_tibia = 0

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())


# 2. Spalte: Ausgestreckt nach oben
print("Zweite Spalte PI/2, 0, 0")
config.theta_coxa = PI/2
config.theta_femur = 0
config.theta_tibia = 0

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 3. Spalte: Ausgestreckt nach schräg rechts oben
print("Dritte Spalte PI/4, 0, 0")
config.theta_coxa = PI/4
config.theta_femur = 0
config.theta_tibia = 0

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 4. Spalte: Ausgestreckt nach unten
print("Vierte Spalte 3/2*PI, 0, 0")
config.theta_coxa = PI/2
config.theta_femur = 0
config.theta_tibia = 0

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 5. Spalte: Eingeklappt nach rechts
print("5. Spalte 0, 0, 0")
config.theta_coxa = 0
config.theta_femur = PI
config.theta_tibia = PI

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())


# 6. Spalte: Eingeklappt nach oben
print("6. Spalte PI/2, 0, 0")
config.theta_coxa = PI/2
config.theta_femur = PI
config.theta_tibia = PI

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 7. Spalte: Eingeklappt nach schräg rechts oben
print("7. Spalte PI/4, 0, 0")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 8. Spalte: Eingeklappt nach unten
print("8. Spalte 3/2*PI, PI/2, PI/2")
config.theta_coxa = PI/2*3
config.theta_femur = PI
config.theta_tibia = PI

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# Rechter Winkel
# 9. Spalte rechter Winkel, rechts
print("9. Spalte 0, PI/2, PI/2")
config.theta_coxa = 0
config.theta_femur = PI/2
config.theta_tibia = PI/2

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())


# 10. Spalte: Rechter Winkel nach oben
print("10. Spalte PI/2, PI/2, PI/2")
config.theta_coxa = PI/2
config.theta_femur = PI/2
config.theta_tibia = PI/2

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 11. Spalte: Rechter Winkel nach schräg rechts oben
print("11. Spalte PI/4, PI/2, PI/2")
config.theta_coxa = PI/4
config.theta_femur = PI/2
config.theta_tibia = PI/2

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())

# 12. Spalte: Rechter Winkel nach unten
print("12. Spalte 3/2*PI, PI/2, PI/2")
config.theta_coxa = PI/2*3
config.theta_femur = PI/2
config.theta_tibia = PI/2

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
exec(open("Visuals.py").read())

config.center = (-3, 0)
exec(open("Visuals.py").read())

config.center = (-9, 0)
exec(open("Visuals.py").read())

config.center = (-9, -1)
exec(open("Visuals.py").read())

config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())