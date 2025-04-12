import config
import geometry
import robotic_arm
import numpy as np

# Modes:
# 0 : Normal mode
# 1 : Reflect Femur mode
# 2 : Reflect Tibia mode

def switch_to_mode_reflect_femur(arm):
    """Switches to the mode where the femur link needs to change position. Calculate target angles for the new position.

    Args:
        arm (RoboterArm.RoboticArm): Robotic arm to manipulate
    """
    config.goal_reflect_femur_link = arm.reflect_femur_link()
    return

def switch_to_mode_reflect_tibia(arm):
    """Switches to the mode where the tibia link needs to change position. Calculate target angles for the new position.

    Args:
        arm (RoboterArm.RoboticArm): Robotic arm to manipulate
    """
    config.goal_reflect_tibia_link = arm.reflect_tibia_link()
    return

'''
# The three possible modes
# mode_femur: Switches the position of the femur link to 'point' away from the obstacle
# mode_tibia: Switches the position of the tibia link to 'point' away from the obstacle
# normal: The elbows are not near the obstacle or are in the correct posture, the movement of the arm is 
# calculated by the algorithm
'''

def choose_mode(arm, current_mode):
    """Continouusly reeavaluates the current mode and determines if it is still the current one or cause a switch

    Args:
        arm (RoboterArm.RoboticArm): Robotic arm to manipulate
        current_mode (int): current mode of the robotic arm

    Returns:
        int: new current mode of the robotic arm
    """
    # Current mode: normal
    if(current_mode == None):
        current_mode = 0

    if(current_mode == 0):
        # Near obstacle?
        distance_to_obstacle = arm.distance_arm_obstacle(config.center, config.radius)
        if(distance_to_obstacle < config.min_distance_to_obstacle*2):
            # If yes: Elbow posture femur correct? -> reflect Femur mode
            bool_femur, bool_tibia = geometry.booleans_switch_elbows(arm, config.center)
            if(bool_femur == 0):
                switch_to_mode_reflect_femur(arm)
                return 1
            # Elbow posture tibia correct? -> reflect tibia mode
            elif(bool_tibia == 0):
                switch_to_mode_reflect_tibia(arm)
                return 2
        # If no: Continue in normal mode
        else:
            return 0

    # Current mode: reflect femur mode
    elif(current_mode == 1):
        if(arm_near_target_angles(arm, config.goal_reflect_femur_link)):
            # If yes: normal/reflect tibia mode
            return 0
        # If no: Continue in reflect femur mode
        else:
            return 1

    # Current mode: tibia mode
    elif(current_mode == 2):
        # Elbow near tibia goal?
        if(arm_near_target_angles(arm, config.goal_reflect_tibia_link)):
            # If yes: normal
            return 0
        # If no: Continue in tibia mode
        else:
            return 2
    return 0
        
def arm_near_target_angles(arm :robotic_arm.RoboticArm, target_angles, tolerance = 0.1):
    """Checks if the arm posture is within tolerance to the target angles

    Args:
        arm (RoboterArm.RoboticArm): Robotic Arm to manipulate
        target_angles (float[]): target angles for the links of the robotic arm [theta_coxa, theta_femur, theta_tibia]
        tolerance (float, optional): amount of tolerance to the target angles. Defaults to 0.001.

    Returns:
        Bool: True, if arm near target angles. Else False
    """
    if(np.abs(arm.theta_coxa - target_angles[0]) > tolerance):
        return False
    elif(np.abs(arm.theta_femur - target_angles[1]) > tolerance):
        return False
    elif(np.abs(arm.theta_tibia - target_angles[2]) > tolerance):
        return False
    else:
        return True
