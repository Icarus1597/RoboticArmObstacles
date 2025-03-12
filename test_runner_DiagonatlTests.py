import config
import numpy as np


PI = np.pi

print("1.,2.: PI/4, PI, PI")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = -12,12
config.center = (-6, 6)
config.radius = 2
exec(open("Visuals.py").read())

config.theta_coxa = 5/4*PI
exec(open("Visuals.py").read())

config.theta_coxa = 7/4*PI
exec(open("Visuals.py").read())

print("3.4.: PI/4, PI, PI")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = 12,-12
config.center = (6, -6)
config.radius = 2
exec(open("Visuals.py").read())

config.theta_coxa = 5/4*PI
exec(open("Visuals.py").read())

config.theta_coxa = 3/4*PI
exec(open("Visuals.py").read())

print("5.6..: PI/4, PI, PI")
config.theta_coxa = 3*PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = 12,12
config.center = (6, 6)
config.radius = 2
exec(open("Visuals.py").read())

config.theta_coxa = 7/4*PI
exec(open("Visuals.py").read())

config.theta_coxa = 5/4*PI
exec(open("Visuals.py").read())

print("7.8.: PI/4, PI, PI")
config.theta_coxa = 3*PI/4
config.theta_femur = PI
config.theta_tibia = PI
config.target_x, config.target_y = -12,-12
config.center = (-6, -6)
config.radius = 2
exec(open("Visuals.py").read())

config.theta_coxa = 7/4*PI
exec(open("Visuals.py").read())

config.theta_coxa = 1/4*PI
exec(open("Visuals.py").read())