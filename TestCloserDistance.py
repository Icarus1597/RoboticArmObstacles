import config
import numpy as np


PI = np.pi

current_test = 1

config.target_x = -6
config.target_y = 0

# Open/Make new file in "write"-mode
with open("testresults.txt", "w") as file:
    file.write("Test results\n\n")
    file.write("Current Parameters:\n")
    file.write(f"delta_t = {config.delta_t}\n")
    file.write(f"max_velocity = {config.max_velocity}\n")
    file.write(f"link lengths: coxa = {config.coxa_length}, femur = {config.femur_length}, tibia = {config.tibia_length}\n")
    file.write(f"max offset needed for success = {config.delta_success_distance}\n")
    file.write(f"damping_factor = {config.damping_factor}\n")
    file.write(f"Parameters repulsive field: rho_0 = {config.rho_0}, k = {config.k}\n")
    file.write(f"Parameter attractive field zeta = {config.zeta}\n")
    file.write(f"Maximum time for a test: timeout = {config.timeout}\n")
    file.write(f"Minimum distnace to obstacle: min_distance_to_obstacle = {config.min_distance_to_obstacle}\n")
    file.write(f"Target = {config.target_x}, {config.target_y}\n \n")


# 1. Spalte: Ausgestreckt nach rechts
print("Erste Spalte 0, 0, 0")
config.theta_coxa = 0
config.theta_femur = 0
config.theta_tibia = 0

with open("testresults.txt", "a") as file:
    file.write(f"First Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-2, 0)
config.radius = 1
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-1, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-3, 1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-3, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-3, 1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open("Visuals.py").read())