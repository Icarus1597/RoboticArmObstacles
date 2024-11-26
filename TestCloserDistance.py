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

# 2. Spalte: Ausgestreckt nach oben
print("Zweite Spalte Pi/2, 0, 0")
config.theta_coxa = PI/2
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

# 3. Spalte: Ausgestreckt schräg
print("Dritte Spalte PI/4, 0, 0")
config.theta_coxa = PI/4
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

# 4. Spalte: Ausgestreckt nach unten
print("Vierte Spalte 3/2*PI, 0, 0")
config.theta_coxa = 3/2*PI
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

# 5. Spalte: Eingeklappt
print("Fuenfte Spalte 0, PI, PI")
config.theta_coxa = 0
config.theta_femur = PI
config.theta_tibia = PI

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

# 6. Spalte: Eingeklappt
print("Sechste Spalte PI/2, PI, PI")
config.theta_coxa = PI/2
config.theta_femur = PI
config.theta_tibia = PI

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

# 7. Spalte: Eingeklappt nach schräg rechts oben
print("7. Spalte PI/4, PI, PI")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI

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

# 8. Spalte: Eingeklappt nach unten
print("8. Spalte 3/2*PI, PI, PI")
config.theta_coxa = PI/2*3
config.theta_femur = PI
config.theta_tibia = PI

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

# Rechter Winkel
# 9. Spalte rechter Winkel, rechts
print("9. Spalte 0, PI/2, PI/2")
config.theta_coxa = 0
config.theta_femur = PI/2
config.theta_tibia = PI/2

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

# 10. Spalte: Rechter Winkel nach oben
print("10. Spalte PI/2, PI/2, PI/2")
config.theta_coxa = PI/2
config.theta_femur = PI/2
config.theta_tibia = PI/2

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

# 11. Spalte: Rechter Winkel nach schräg rechts oben
print("11. Spalte PI/4, PI/2, PI/2")
config.theta_coxa = PI/4
config.theta_femur = PI/2
config.theta_tibia = PI/2

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

# 12. Spalte: Rechter Winkel nach unten
print("12. Spalte 3/2*PI, PI/2, PI/2")
config.theta_coxa = PI/2*3
config.theta_femur = PI/2
config.theta_tibia = PI/2

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

with open("testresults.txt", "a") as file:
    file.write(f"Total number of tests: {current_test-1}, #SUCCESS: {config.number_success}, in percent: {config.number_success/(current_test-1)}\n")
