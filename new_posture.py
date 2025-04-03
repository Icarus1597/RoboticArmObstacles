import config2
import PotentialFields as pf
import autograd.numpy as anp
import numpy as np
import Geometrie
import AStarAlgorithm
import time
import matplotlib.pyplot as plt

""" config.wrapper_mode: (in config)
0 : Naive Approach
1 : A*
2 : A* Elbows
3 : A* SP
4 : A* Tang
5 : PF
6 : PF L
7 : PF SP
8 : PF SP L
"""

PI = np.pi

def init_test(arm):
    if(config2.wrapper_mode == 1 or config2.wrapper_mode == 2 or config2.wrapper_mode == 4): # A* without SP
        # A-Star Algorithm
        initial_point = AStarAlgorithm.AStarNode(arm.end_effector, config2.target)
        time_start_algorithm = time.time()
        config2.path_node_list = initial_point.iterative_search_wrapper()
        time_end_algorithm = time.time()
        with open("testresults.txt", "w") as file:
            file.write(f"Time needed calculation = {time_end_algorithm - time_start_algorithm}\n\n")

        if(config2.path_node_list == -1):
            with open("testresults.txt", "w") as file:
                file.write(f"Time needed calculation = {time_end_algorithm - time_start_algorithm}\n\n")
            return -1
        
        config2.next_node_index = 0
        return
    
    elif(config2.wrapper_mode == 3 or config2.wrapper_mode >= 7): # SP
        config2.mode_sp = True
        config2.sp_target_angles = calculate_starting_posture()
        return
    
    else:
        return


def calculate_new_thetas(arm):
    if(config2.wrapper_mode == 0): # Naive
        theta_coxa, theta_femur, theta_tibia = arm.inverse_kinematics(config2.target)
        return theta_coxa, theta_femur, theta_tibia
    
    if(config2.wrapper_mode ==1): # A*
        theta_coxa, theta_femur, theta_tibia = arm.inverse_kinematics(config2.path_node_list[config2.next_node_index].position)

        if(np.linalg.norm(arm.error_target_end_effector(config2.path_node_list[config2.next_node_index].position))<config2.tolerance) :
            if(len(config2.path_node_list) > config2.next_node_index+1):
                config2.next_node_index += 1
        return theta_coxa, theta_femur, theta_tibia
    return -1


def calculate_starting_posture(alpha_offset=PI*5/4, beta_offset = PI/4, gamma_offset = PI/4):
    """Calculate, based on the target and obstacle position, the desired starting position for the robotic arm

    Args:
        alpha_offset (float): desired offset for the coxa link (PI/2 -> 90° to Obstacle)

    Returns:
        theta_coxa, theta_femur, theta_tibia: target angles for the starting position
    """
    side = Geometrie.side_point_to_line2(config2.target, (0, 0), config2.center)
    alpha = Geometrie.angle_vector_point((0,0), (1,0), config2.center)
    #print(f"side = {side}, alpha = {alpha}")
    theta_coxa = (alpha + side*alpha_offset) % (2*PI)
    theta_femur = beta_offset * side % (2*PI)
    theta_tibia = gamma_offset * side % (2*PI)
    return theta_coxa, theta_femur, theta_tibia