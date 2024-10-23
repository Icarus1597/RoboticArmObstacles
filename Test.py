import config
import numpy as np


PI = np.pi

# 1. Spalte: Ausgestreckt nach rechts
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