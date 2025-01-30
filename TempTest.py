import config
import numpy as np


PI = np.pi

current_test = 1
algorithm = ["AStarWrapper.py", "Visuals.py"]
mode = 1 # 0 : Astar-Algorithm, 1 : Potential Fields Method

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
    file.write(f"Minimum distnace to obstacle: min_distance_to_obstacle = {config.min_distance_to_obstacle}\n \n")



#arm.update_joints(np.pi/4, np.pi/2, np.pi*3/2)
config.theta_coxa = PI/4+PI
config.theta_femur = PI/4
config.theta_tibia = PI/4
config.center = (-1, 5)

with open("testresults.txt", "a") as file:
    file.write(f"First Set of Tests. coxa = {config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")

exec(open(algorithm[mode]).read())