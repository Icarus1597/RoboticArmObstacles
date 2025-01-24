import numpy as np
# TODO

# Function to calculate the reflection of a point P(x0, y0) across a line defined by points (x1, y1) and (x2, y2)
def reflect_on_hypotenuse(arm, x0, y0, x1, y1, x2, y2):
    # Calculate the reflection of the point (x0, y0) across the line (x1, y1) - (x2, y2)
    
    # Compute the slope of the line
    dx = x2 - x1
    dy = y2 - y1
    
    # If the line is vertical (dx == 0), the reflection is straightforward horizontally
    if dx == 0:
        return 2 * x1 - x0, y0
    
    # Calculate the slope of the line
    m = dy / dx
    
    # Calculate the y-intercept b of the line
    b = y1 - m * x1
    
    # Compute the foot of the perpendicular from point P (x0, y0) to the line
    # The perpendicular line has a slope of -1/m
    # Equation of the perpendicular line: y - y0 = -1/m * (x - x0)
    
    # Calculate the intersection point of the two lines (the foot of the perpendicular)
    A = 1 + m**2
    B = 2 * (m * (b - y0) - x0)
    C = x0**2 + (b - y0)**2 - (x1**2 + y1**2)
    
    # Calculate the intersection point
    x_intersection = -B / (2 * A)
    y_intersection = m * x_intersection + b
    
    # The reflection point is at the same distance from the foot of the perpendicular as the original point
    x_reflection = 2 * x_intersection - x0
    y_reflection = 2 * y_intersection - y0
    
    return x_reflection, y_reflection

# TODO: Comment Determines, if the joint is tilted to the right (0) or to the left (1) 
# in the perspective of the ursprung of the link
# Input:
#   angle
# Output:
#   0 if eingeschlagen to the right side
#   1 if eingeschlagen to the left side
def which_side_small_angle(angle):
    if(angle % (2*np.pi) < np.pi):
        return 0
    else:
        return 1
    
# TODO: Determines, from perspective of the coxa link, if the obstacle is on its right side or left side
# Input:
#   arm: To know the position and current posture of the coxa link
#   center: Center Point of the Obstacle
# Ouput:
#   0 : Obstacle is on the right side of coxa TODO is this correct? Should be correct
#   1 : Obstacle is on the left side of coxa
def which_side_obstacle_to_coxa(arm, center):
    # Calculate the slope of the coxa link under the presumption, that the arm's origin is always (0,0)
    m = arm.joint_coxa[1]/arm.joint_coxa[0]

    f_center = m * center[0]

    if (f_center > center[1]):
        return 0
    else:
        return 1
    
# Determines, if the elbows need to change side or not
# Input:
#   arm: Robotic arm
#   center: center of the obstacle
# Output:
#   bool_result_coxa: 0, if on correct side, else 1
#   bool_result_tibia: 0, if on correct side, else 1
def booleans_switch_elbows(arm, center):
    bool_obstacle_side = which_side_obstacle_to_coxa(arm, center)
    bool_coxa_elbow = which_side_small_angle(arm.theta_femur)
    bool_tibia_elbow = which_side_small_angle(arm.theta_tibia)

    if(bool_obstacle_side == bool_coxa_elbow):
        bool_result_coxa = 0
    else: 
        bool_result_coxa = 1

    if(bool_obstacle_side == bool_tibia_elbow):
        bool_result_tibia = 0
    else:
        bool_result_tibia = 1
