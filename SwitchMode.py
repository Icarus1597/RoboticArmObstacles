import config
import Geometrie
import PotentialFields as pf
import RoboterArm
import numpy as np

# Current mode
# 0 : normal mode
# 1 : coxa mode
# 2 : tibia mode
#current_mode = 0 

# Call this methods, if there is a switch to a new mode. When there ought to be a change in the elbow posture, 
# Calculate new goal position for the elbow
def switch_to_mode_coxa(arm):
    config.goal_reflect_femur_link = arm.reflect_femur_link()
    print(f"goal angles femur = {config.goal_reflect_femur_link}")
    return

def switch_to_mode_tibia(arm):
    config.goal_reflect_tibia_link = arm.reflect_tibia_link()
    return

def switch_to_mode_normal():
    return

'''
# The three possible modes
# mode_coxa: Switches the position of the femur link to 'point' away from the obstacle
# mode_tibia: Switches the position of the tibia link to 'point' away from the obstacle
# normal: The elbows are not near the obstacle or are in the correct posture, the movement of the arm is 
# calculated by the algorithm
set_modes = {"ModeCoxa":mode_coxa, "ModeTibia":mode_tibia, "Normal":mode_normal}
'''

# Continouusly reeavaluates the current mode and determines if it is still the current one or veranlasst TODO a switch
# Output: 
#   Current mode
def choose_mode(arm, current_mode):
    # Current mode: normal
    if(current_mode == 0 or current_mode == None):
        # Near obstacle?
        distance_to_obstacle = arm.distance_arm_obstacle(config.center, config.radius)
        if(distance_to_obstacle < 2):
            # If yes: Elbow posture coxa correct? -> coxa mode
            bool_coxa, bool_tibia = Geometrie.booleans_switch_elbows(arm, config.center)
            if(bool_coxa == 0):
                switch_to_mode_coxa(arm)
                return 1
            # Elbow posture tibia correct? -> tibia mode
            elif(bool_tibia == 0):
                switch_to_mode_tibia(arm)
                return 2
        # If no: Continue in normal mode
        else:
            return 0

    # Current mode: coxa mode
    if(current_mode == 1):
        if(arm_near_target_angles(arm, config.goal_reflect_femur_link)):
            # If yes: normal/tibia mode
            return 0
        # If no: Continue in coxa mode
        else:
            return 1

    # Current mode: tibia mode
    if(current_mode == 2):
        # Elbow near tibia goal?
        if(arm_near_target_angles(arm, config.goal_reflect_tibia_link)):
            # If yes: normal
            return 0
        # If no: Continue in tibia mode
        else:
            return 2
        
def arm_near_target_angles(arm :RoboterArm.RoboticArm, target_angles, tolerance = 0.001):
    if(np.abs(arm.theta_coxa - target_angles[0]) > tolerance):
        return False
    elif(np.abs(arm.theta_femur - target_angles[1]) > tolerance):
        return False
    elif(np.abs(arm.theta_tibia - target_angles[2]) > tolerance):
        return False
    else:
        print(f"True: arm near target angles")
        return True
