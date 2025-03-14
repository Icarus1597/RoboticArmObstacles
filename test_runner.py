import config
import numpy as np
import PrintStatistics as ps


PI = np.pi

current_test = 1
algorithm = ["WrapperNaive.py", "WrapperAStar.py", "WrapperAStarElbow.py", "WrapperAStarStartPosition.py", 
             "WrapperAStarTang.py", "WrapperPF.py", "WrapperPFLinkage.py", "WrapperPFStartingPosition.py",
             "WrapperPFStartingPosition.py"]

""" config.wrapper_mode: (in config)
0 : Naive Approach
1 : A*
2 : A* algorithm with own approach to avoid obstacle with whole linkage reflecting elbows
3 : A* with adjusting starting position
4 : A* inspired by Tang with PF for linkage
5 : PF
6 : PF Linkage
7 : PF Starting Position
8 : PF Starting Position and Linkage
"""

# Open/Make new file in "write"-config.wrapper_mode
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
    file.write(f"Minimum distance to obstacle: min_distance_to_obstacle = {config.min_distance_to_obstacle}\n \n")

# 1. Spalte: Ausgestreckt nach rechts
print("Erste Spalte 0, 0, 0")
config.theta_coxa = 0.01
config.theta_femur = 0.01
config.theta_tibia = 0.01

with open("testresults.txt", "a") as file:
    file.write(f"First Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 2. Spalte: Ausgestreckt nach oben
print("Zweite Spalte PI/2, 0, 0")
config.theta_coxa = PI/2
config.theta_femur = 0
config.theta_tibia = 0
with open("testresults.txt", "a") as file:
    file.write(f"Second Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 3. Spalte: Ausgestreckt nach schräg rechts oben
print("Dritte Spalte PI/4, 0, 0")
config.theta_coxa = PI/4
config.theta_femur = 0.0001
config.theta_tibia = 0.0001

with open("testresults.txt", "a") as file:
    file.write(f"Third Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 4. Spalte: Ausgestreckt nach unten
print("Vierte Spalte 3/2*PI, 0, 0")
config.theta_coxa = PI/2*3
config.theta_femur = 0
config.theta_tibia = 0

with open("testresults.txt", "a") as file:
    file.write(f"Fourth Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 5. Spalte: Eingeklappt nach rechts
print("5. Spalte 0, PI, PI")
config.theta_coxa = 0
config.theta_femur = PI
config.theta_tibia = PI

with open("testresults.txt", "a") as file:
    file.write(f"Fifth Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 6. Spalte: Eingeklappt nach oben
print("6. Spalte PI/2, PI, PI")
config.theta_coxa = PI/2
config.theta_femur = PI
config.theta_tibia = PI

with open("testresults.txt", "a") as file:
    file.write(f"Sixth Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

# 7. Spalte: Eingeklappt nach schräg rechts oben
print("7. Spalte PI/4, PI, PI")
config.theta_coxa = PI/4
config.theta_femur = PI
config.theta_tibia = PI

with open("testresults.txt", "a") as file:
    file.write(f"Seventh Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 8. Spalte: Eingeklappt nach unten
print("8. Spalte 3/2*PI, PI, PI")
config.theta_coxa = PI/2*3
config.theta_femur = PI
config.theta_tibia = PI

with open("testresults.txt", "a") as file:
    file.write(f"8th Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

# Rechter Winkel
# 9. Spalte rechter Winkel, rechts
print("9. Spalte 0, PI/2, PI/2")
config.theta_coxa = 0
config.theta_femur = PI/2
config.theta_tibia = PI/2

with open("testresults.txt", "a") as file:
    file.write(f"Ninth Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())


# 10. Spalte: Rechter Winkel nach oben
print("10. Spalte PI/2, PI/2, PI/2")
config.theta_coxa = PI/2
config.theta_femur = PI/2
config.theta_tibia = PI/2

with open("testresults.txt", "a") as file:
    file.write(f"Tenth Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

# 11. Spalte: Rechter Winkel nach schräg rechts oben
print("11. Spalte PI/4, PI/2, PI/2")
config.theta_coxa = PI/4
config.theta_femur = PI/2
config.theta_tibia = PI/2

with open("testresults.txt", "a") as file:
    file.write(f"Eleventh Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

# 12. Spalte: Rechter Winkel nach unten
print("12. Spalte 3/2*PI, PI/2, PI/2")
config.theta_coxa = PI/2*3
config.theta_femur = PI/2
config.theta_tibia = PI/2

with open("testresults.txt", "a") as file:
    file.write(f"12th Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

# Position and radius of the obstacle (circle)
config.center = (-6, 0)
config.radius = 2
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, 0)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-9, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-3, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, -1)
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

config.center = (-6, 0)
config.radius = 4
with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[config.wrapper_mode]).read())

ps.statistics_a_star()
ps.statistics_a_star_elbow()
ps.statistics_a_star_start_position()
ps.statistics_astar_tang
ps.statistics_naive()
ps.statistics_pf()
ps.statistics_pf_linkage()
ps.statistics_pf_sp()
ps.statistics_pf_linkage_sp()