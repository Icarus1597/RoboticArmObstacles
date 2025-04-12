import config
import numpy as np
import print_test_results as ptr

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

config.target_x = -12
config.target_y = 0

config.center = (-600, 0) # Move it far out of the way to not influence the arm
config.radius = 2

config.theta_coxa = 0
config.theta_femur = PI/2
config.theta_tibia = PI/2

for i in range (0, 9): # run multiple times to get average
    exec(open(algorithm[0]).read()) # naive
    exec(open(algorithm[1]).read()) # A*
    exec(open(algorithm[5]).read()) # PF

ptr.statistics_a_star()
ptr.statistics_pf()
ptr.statistics_naive()
