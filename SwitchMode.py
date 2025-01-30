import config
import Geometrie

# I think this set thingy is not doing what its supposed to do TODO

# Call this methods, if there is a switch to a new mode. When there ought to be a change in the elbow posture, 
# Calculate new goal position for the elbow
def mode_coxa(arm):
    config.coxa_elbow_goal = Geometrie.reflect_on_hypotenuse(config.center[0], config.center[1], 
                                                             0, 0, 
                                                             arm.joint_coxa[0], arm.joint_coxa[1])
    return 

def mode_tibia(arm):
    config.tibia_elbow_goal = Geometrie.reflect_on_hypotenuse(config.center[0], config.center[1], 
                                                              arm.joint_femur[0], arm.joint_femur[1], 
                                                              arm.joint_tibia[0], arm.joint_tibia[1])
    return

def mode_normal():
    return

# The three possible modes
# mode_coxa: Switches the position of the femur link to 'point' away from the obstacle
# mode_tibia: Switches the position of the tibia link to 'point' away from the obstacle
# normal: The elbows are not near the obstacle or are in the correct posture, the movement of the arm is 
# calculated by the algorithm
set_modes = {"ModeCoxa":mode_coxa, "ModeTibia":mode_tibia, "Normal":mode_normal}

# Calculates based on the current mode the new thetas of the arm
def calculate_new_thetas():
    return

# Continouusly reeavaluates the current mode and determines if it is still the current one or veranlasst TODO a switch
def choose_mode():
    return