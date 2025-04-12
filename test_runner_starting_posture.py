import config
import numpy as np
import print_test_results as ps
import geometry

PI = np.pi

current_test = 1
algorithm = ["runner_naive.py", "runner_a_star.py", "runner_a_star_elbow.py", "runner_a_star_starting_posture.py", 
             "runner_a_star_tang.py", "runner_potential_fields.py", "runner_pf_linkage.py", "runner_pf_starting_posture.py",
             "runner_pf_linkage_sp.py"]

""" config.runner_mode: (in config)
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
mode = 0
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
# TODO Starting position
config.target_x = -12
config.target_y = 0
config.center = (-6, 0)
config.radius = 2
alpha_offset = PI
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
print(f"alpha = {alpha}")
alpha = (alpha + alpha_offset) % (2*np.pi)
print(f"theta_coxa = {alpha}")
config.theta_coxa = alpha
config.theta_femur = 0
config.theta_tibia = 0
with open("testresults.txt", "a") as file:
    file.write(f"First Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-9, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-9, -1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, -1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, -1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, 0)
config.radius = 4
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

# Other 12 tests
config.target_x = -10
config.target_y = 0

config.center = (-6, 0)
config.radius = 2
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-7, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-7, -1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, -1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, -1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-6, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.target_x = -6
config.target_y = 1

config.center = (-3, -1)
config.radius = 1
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-3, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-4, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-2, 0)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

with open("testresults.txt", "a") as file:
    file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
current_test = current_test + 1
exec(open(algorithm[mode]).read())

config.center = (-4, 1)
alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
alpha = (alpha + alpha_offset) % (2*np.pi)
config.theta_coxa = alpha

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