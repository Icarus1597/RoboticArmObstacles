import config
import numpy as np
import random
import RoboterArm
import PrintStatistics as ps


PI = np.pi

current_test = 1
algorithm = ["WrapperNaive.py", "WrapperAStar.py", "WrapperAStarElbow.py", "WrapperAStarStartPosition.py", 
             "WrapperAStarTang.py", "WrapperPF.py", "WrapperPFLinkage.py", "WrapperPFStartingPosition.py"]

""" mode: 
0 : Naive Approach
1 : A*
2 : A* algorithm with own approach to avoid obstacle with whole linkage reflecting elbows
3 : A* with adjusting starting position
4 : A* inspired by Tang with PF for linkage
5 : PF
6 : PF Linkage
7 : PF Starting Position
"""

# Open/Make new file in "write"-mode
with open("testresults.txt", "w") as file:
    file.write("Test results\n\n")

config.theta_coxa = random.random()*PI
config.theta_femur = random.random()*PI
config.theta_tibia = random.random()*PI

while (current_test <= 5):
    config.theta_coxa = random.random()*PI
    config.theta_femur = random.random()*PI
    config.theta_tibia = random.random()*PI

    arm_length = config.coxa_length + config.femur_length + config.tibia_length

    config.radius = np.maximum(random.random()*arm_length/4, 1)

    # target position
    config.target_x = np.minimum(random.random()*2/3*arm_length, 5*config.radius)
    config.target_y = 0

    # center Obstacle
    center_y = random.random()*arm_length - 1/2*arm_length
    center_x = random.random()*(config.target_x-3*config.radius)+3/2*config.radius
    config.center = (center_x, center_y)

    # Test if in start position the arm is already too close to the obstacle
    arm = RoboterArm.RoboticArm(config.coxa_length, config.femur_length, config.tibia_length)
    arm.update_joints(config.theta_coxa, config.theta_femur, config.theta_tibia)
    distance = arm.distance_arm_obstacle(config.center, config.radius)

    if(distance < 1.5*config.min_distance_to_obstacle):
        continue

    with open("testresults.txt", "a") as file:
        file.write(f"Test no. {current_test} Parameters obstacle: center = {config.center}, radius = {config.radius}\n")
        file.write(f"Start posture: coxa={config.theta_coxa}, femur = {config.theta_femur}, tibia = {config.theta_tibia}\n")
        file.write(f"target position: x={config.target_x}, y={config.target_y}\n")

    mode = 0

    while (mode < len(algorithm)):
        with open("testresults.txt", "a") as file:
            file.write(f"Mode:{algorithm[mode]}\n")
        exec(open(algorithm[mode]).read())
        mode += 1

    current_test = current_test + 1



ps.statistics_a_star()
ps.statistics_a_star_elbow()
ps.statistics_a_star_start_position()
ps.statistics_naive()
ps.statistics_pf()
ps.statistics_pf_linkage()