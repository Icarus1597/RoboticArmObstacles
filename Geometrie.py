import numpy as np
import math
import autograd.numpy as anp

def which_side_small_angle(angle):
    """ Comment Determines, if the joint is tilted to the right (0) or to the left (1) in the perspective of the start of the link

    Args:
        angle (float): angle of the link

    Returns:
        int: 0 if tilted to the right, 1 if tilted to the left
    """
    if(angle % (2*np.pi) < np.pi):
        return 0
    else:
        return 1
    
def distance_segment_point(point_x, point_y, segment_a_x, segment_a_y, segment_b_x, segment_b_y) :
    """ Calculates the minimum distance between a segment and a point.

    Args:
        point_x (float): x coordinate of the point
        point_y (float): y coordinate of the point
        segment_a_x (float): x coordinate of the starting point of the segment
        segment_a_y (float): y coordinate of the starting point of the segment
        segment_b_x (float): x coordinate of the end point of the segment
        segment_b_y (float): y coordinate of the end point of the segment

    Returns:
        float: minimum distance between the segment and point
    """
    # Calculates slope of the segment
    dx = segment_b_x - segment_a_x
    dy = segment_b_y - segment_a_y

    # Special case
    if (dx == 0):
        return abs(point_x - segment_a_x)
    
    # Calculate foot point
    t = ((point_x - segment_a_x) * dx + (point_y - segment_a_y) * dy) / (dx**2 + dy**2)

    hx = segment_a_x + t * dx
    hy = segment_a_y + t * dy

    # Check if the foot point H is within the segment AB
    if t < 0:
        # If t < 0, the foot point is outside the segment, closest point is A
        return math.sqrt((point_x - segment_a_x)**2 + (point_y - segment_a_y)**2)
    elif t > 1:
        # If t > 1, the foot point is outside the segment, closest point is B
        return math.sqrt((point_x - segment_b_x)**2 + (point_y - segment_b_y)**2)
    else:
        # Otherwise, the foot point H is within the segment, calculate the euclidian distance
        return math.sqrt((point_x - hx)**2 + (point_y - hy)**2)
        
'''
# TODO: Determines, from perspective of the coxa link, if the obstacle is on its right side or left side
# TODO: This is buggy
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
'''

def side_point_to_line(point_x, point_y, line_start_x, line_start_y, line_end_x, line_end_y):
    """ Determines, from perspective of the direction of the line, if the point is on its right side or left side

    Args:
        point_x (_type_): x coordinate of point
        point_y (_type_): y coordinate of point
        line_start_x (_type_): x coordinate of starting point of the line
        line_start_y (_type_): y coordinate of starting point of the line
        line_end_x (_type_): x coordinate of end point of the line
        line_end_y (_type_): y coordinate of end point of the line

    Returns:
        int: 0, if point is on the left side of the line. 1, if point is on the right side of the line
    """
    # Cross product to determine the side of the line
    cross_product = (line_end_x - line_start_x) * (point_y - line_start_y) - (line_end_y - line_start_y) * (point_x - line_start_x)

    if cross_product > 0:  # Point is on the left side of the line
        return 0
    else:  # Point is on the right side of the line
        return 1

def booleans_switch_elbows(arm, center):
    """ Determines, if the elbows need to change side or not

    Args:
        arm (RoboterArm.RoboticArm): robotic arm
        center ((float, float)): center of the obstacle

    Returns:
        int: bool_result_coxa = 1, if on correct side, else 0
        int: bool_result_tibia = 1, if on correct side, else 0
    """
    bool_obstacle_side = side_point_to_line(center[0], center[1], 0, 0, arm.joint_coxa[0], arm.joint_coxa[1])
    bool_coxa_elbow = which_side_small_angle(arm.theta_femur)
    bool_tibia_elbow = which_side_small_angle(arm.theta_tibia)

    if(bool_obstacle_side != bool_coxa_elbow):
        bool_result_coxa = 0
    else: 
        bool_result_coxa = 1

    if(bool_obstacle_side != bool_tibia_elbow):
        bool_result_tibia = 0
    else:
        bool_result_tibia = 1
    
    return bool_result_coxa, bool_result_tibia

def distance_to_circle(center, radius, point):
    """ Method to calculate the distance between a circle and a point.

    Args:
        center ((float, float)): position of the center of the circle
        radius (float): radius of the circle
        point ((float, float)): point for which the distance shall be calculated

    Returns:
        float: minimum distance between the point and the border of the circle
    """
    distance = cartesian_distance(center, point) - radius
    if(distance < 0) : 
        distance = 0
    return distance

def cartesian_distance(point1, point2):
    """ Cartesian distance of two points

    Args:
        point1 ((float, float)): One point
        point2 ((float, float)): Another point

    Returns:
        float: cartesian distance between point1 and point2
    """
    point1 = anp.array(point1, dtype=anp.float64)
    point2 = anp.array(point2, dtype=anp.float64)
    # Calculate the vector of difference
    difference = point1 - point2
    # Calculate the norm of the vector
    distance = anp.sqrt(anp.sum(difference ** 2))
    return distance

