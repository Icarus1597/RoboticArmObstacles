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
# TODO Starting position
config.target_x = -12
config.target_y = 0
config.center = (-600, 0)
config.radius = 2

config.theta_coxa = 0
config.theta_femur = PI/2
config.theta_tibia = PI/2

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive

exec(open(algorithm[0]).read()) # A*
exec(open(algorithm[1]).read()) # PF
exec(open(algorithm[3]).read()) # Naive


ps.statistics_a_star()
ps.statistics_pf()
ps.statistics_naive()
