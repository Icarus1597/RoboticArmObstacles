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
    config.coxa_elbow_goal = Geometrie.reflect_on_hypotenuse(config.center[0], config.center[1], 
                                                             0, 0, 
                                                             arm.joint_coxa[0], arm.joint_coxa[1])
    config.goal_femur_angle = arm.calculate_femur_angle(config.coxa_elbow_goal)
    return

def switch_to_mode_tibia(arm):
    config.tibia_elbow_goal = Geometrie.reflect_on_hypotenuse(config.center[0], config.center[1], 
                                                              arm.joint_femur[0], arm.joint_femur[1], 
                                                              arm.joint_tibia[0], arm.joint_tibia[1])
    config.goal_tibia_angle = arm.calculate_tibia_angle(config.tibia_elbow_goal)
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

# Calculates based on the current mode the new thetas of the arm
def calculate_new_thetas(): # TODO: Methode nicht an dieser Stelle nötig
    return

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
        # Elbow near coxa elbow goal?
        error_elbow = pf.cartesian_distance(config.coxa_elbow_goal, arm.joint_coxa)
        if(error_elbow < 0.1):
            # If yes: normal/tibia mode
            return 0
        # If no: Continue in coxa mode
        else:
            return 1

    # Current mode: tibia mode
    if(current_mode == 2):
        # Elbow near tibia goal?
        error_elbow = pf.cartesian_distance(config.coxa_elbow_goal, arm.joint_femur)
        if(error_elbow < 0.1):
            # If yes: normal
            return 0
        # If no: Continue in tibia mode
        else:
            return 2