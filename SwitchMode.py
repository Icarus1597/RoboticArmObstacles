import config
import Geometrie
import PotentialFields as pf

# I think this set thingy is not doing what its supposed to do TODO

# Current mode
# 0 : normal mode
# 1 : coxa mode
# 2 : tibia mode
current_mode = 0 

# Call this methods, if there is a switch to a new mode. When there ought to be a change in the elbow posture, 
# Calculate new goal position for the elbow
def switch_to_mode_coxa(arm):
    config.goal_reflect_femur_link = arm.reflect_femur_link()
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
def choose_mode(arm):
    # Current mode: normal
    if(current_mode == 0):
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
        # Elbow near coxa elbow goal? TODO this doesn't make sense
        error_elbow = pf.cartesian_distance(config.goal_reflect_femur_link[1], arm.joint_coxa)
        if(error_elbow < 0.1):
            # If yes: normal/tibia mode
            return 0
        # If no: Continue in coxa mode
        else:
            return 1

    # Current mode: tibia mode
    if(current_mode == 2):
        # Elbow near tibia goal? TODO this doesn't make sense
        error_elbow = pf.cartesian_distance(config.goal_reflect_tibia_link[2], arm.joint_femur)
        if(error_elbow < 0.1):
            # If yes: normal
            return 0
        # If no: Continue in tibia mode
        else:
            return 2