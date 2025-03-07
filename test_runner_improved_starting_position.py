import config
import numpy as np
import PrintStatistics as ps
import Geometrie

PI = np.pi

current_test = 1
algorithm = ["AStarWrapper.py", "Visuals.py", "OwnElbowWrapper.py", "NaiveWrapper.py", "PFLinkageWrapper.py", "StartPositionWrapper.py"]

""" mode: 
0 : A* algorithm
1 : Potential Fields Method without considering the whole linkage
2 : A* algorithm with own approach to avoid obstacle with whole linkage
3 : Naive Approach
4 : Potential Fields Method with considering whole linkage
5 : A* algorithm but moves to specific start position first
"""
mode = 1

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
    file.write(f"Minimum distance to obstacle: min_distance_to_obstacle = {config.min_distance_to_obstacle}\n \n")

PI = np.pi
# Starting position
config.target_x = -12
config.target_y = 0
config.center = (-6, 1)
config.radius = 2

alpha_offset = PI*5/4

def calculate_theta_coxa():
    side = Geometrie.side_point_to_line2((config.target_x, config.target_y), (0, 0), config.center)
    alpha = Geometrie.angle_vector_point((0,0), (1,0), config.center)
    print(f"side = {side}, alpha = {alpha}")
    alpha = (alpha + side*alpha_offset) % (2*PI)
    config.theta_femur = PI/4 * side % (2*PI)
    config.theta_tibia = PI/4 * side % (2*PI)
    return alpha

config.theta_coxa = calculate_theta_coxa()
print(f"theta_coxa = {config.theta_coxa}")

with open("testresults.txt", "a") as file:
    file.write(f"First Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-9, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-9, -1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, -1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, -1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, 0)
config.radius = 4
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

# Other 12 tests
config.target_x = -10
config.target_y = 0

config.center = (-6, 0)
config.radius = 2
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-7, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-7, -1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, -1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, -1)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.target_x = -6
config.target_y = 1

config.center = (-3, -1)
config.radius = 1
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, -1)
config.radius = 1
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-4, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-2, 0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, -0)
config.theta_coxa = calculate_theta_coxa()

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())


# Print Statistics
ps.statistics_a_star()
ps.statistics_a_star_elbow()
ps.statistics_a_star_start_position()
ps.statistics_naive()
ps.statistics_pf()
ps.statistics_pf_linkage()