import config
import numpy as np


PI = np.pi

# 5. Spalte: Eingeklappt nach rechts
print("5. Spalte 0, PI, PI")
config.theta_coxa = 0
config.theta_femur = PI
config.theta_tibia = PI

# Position and radius of the obstacle (circle)

config.radius = 2
config.center = (-3, -1)
exec(open("Visuals.py").read())

config.center = (-6, -1)
exec(open("Visuals.py").read())

config.center = (-6, 0)
config.radius = 4
exec(open("Visuals.py").read())


# 6. Spalte: Eingeklappt nach oben
print("6. Spalte PI/2, PI, PI")
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
print("7. Spalte PI/4, PI, PI")
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