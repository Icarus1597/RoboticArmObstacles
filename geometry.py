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
    
def side_point_to_line2(point, line_start, line_end):
    """ Determines, from perspective of the direction of the line, if the point is on its right side or left side

    Args:
        point (_type_): coordinates of point
        line_start_x (_type_): coordinates of starting point of the line
        line_end_x (_type_): coordinates of end point of the line

    Returns:
        int: -1, if point is on the left side of the line. 1, if point is on the right side of the line
    """
    # Cross product to determine the side of the line
    cross_product = (line_end[0] - line_start[0]) * (point[1] - line_start[1]) - (line_end[1] - line_start[1]) * (point[0] - line_start[0])

    if cross_product > 0:  # Point is on the left side of the line
        return -1
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

def angle_vector_point(vector_start, vector_end, point):
    """ Calculates the angle between a vector consisting of a start and end point and a vector from said start point to an additional point

    Args:
        vector_start (float[]): start point of the vector, two dimensional position
        vector_end (float[]): end point of the vector, two dimensional position
        point (float[]): another point, two dimensional position

    Returns:
        float: angle between vector and vector from start point to the point
    """
    # Vector start to end
    vector_1 = vector_end[0] - vector_start[0]
    vector_2 = vector_end[1] - vector_start[1]

    # Vector start to point
    vector_to_point_1 = point[0] - vector_start[0]
    vector_to_point_2 = point[1] - vector_start[1]

    # Length of the vectors
    length_vector_to_point = np.sqrt(vector_to_point_1**2 + vector_to_point_2**2)
    length_vector = np.sqrt(vector_1**2 + vector_2**2)

    # Catch error to avoid dividing through zero
    if(length_vector == 0 or length_vector_to_point == 0):
        print(f"Geometrie.angle_vector_point: Error: Division through zero")
        return -1


    # Calculate alpha
    temp = (vector_1*vector_to_point_1 + vector_2*vector_to_point_2)/(length_vector_to_point * length_vector)
    if (np.abs(temp)>1):
        print(f"Geometrie, angle_coxa_joint: Value for Arccos out of range")
        temp = np.sign(temp)* abs(temp) % 1
    #print(f"Temp tibia = {temp}")

    alpha = np.arccos(temp)
    bool = side_point_to_line(point[0], point[1], vector_start[0], vector_start[1], vector_end[0], vector_end[1])
    if(bool==1):
        alpha = -alpha % (np.pi*2)
    return alpha

'''
def angle_vector_point2(vector_start, vector_end, point):
    """ Calculates the angle between a vector consisting of a start and end point and a vector from said start point to an additional point

    Args:
        vector_start (float[]): start point of the vector, two dimensional position
        vector_end (float[]): end point of the vector, two dimensional position
        point (float[]): another point, two dimensional position

    Returns:
        float: angle between vector and vector from start point to the point
    """
    # Vector start to end
    vector_1 = vector_end[0] - vector_start[0]
    vector_2 = vector_end[1] - vector_start[1]

    # Vector start to point
    vector_to_point_1 = point[0] - vector_start[0]
    vector_to_point_2 = point[1] - vector_start[1]

    # Length of the vectors
    length_vector_to_point = np.sqrt(vector_to_point_1**2 + vector_to_point_2**2)
    length_vector = np.sqrt(vector_1**2 + vector_2**2)

    # Catch error to avoid dividing through zero
    if(length_vector == 0 or length_vector_to_point == 0):
        print(f"Geometrie.angle_vector_point: Error: Division through zero")
        return -1


    # Calculate alpha
    temp = (vector_1*vector_to_point_1 + vector_2*vector_to_point_2)/(length_vector_to_point * length_vector)
    if (np.abs(temp)>1):
        print(f"Geometrie, angle_coxa_joint: Value for Arccos out of range")
        temp = np.sign(temp)* abs(temp) % 1
    #print(f"Temp tibia = {temp}")

    alpha = np.arccos(temp)
    return alpha
'''

def direction_coxa(femur_link, target_point, center, target_position):
    """Determines rotation direction for coxa joint so that it avoids the obstacle

    Args:
        femur_link (float[]): current position of the femur link, 2D
        target_point (float[]): position of the target, 2D
        center (float[]): position of the center of the obstacle , 2D
        target_position (float[]): target position of the femur_link (starting posture), 2D

    Returns:
        int: 1, if rotation against the clock, -1, if rotation with the clock
    """
    angle_target_point = angle_vector_point((0,0), femur_link, target_point)
    angle_center = angle_vector_point((0,0), femur_link, center)
    angle_target_position = angle_vector_point((0,0), target_position, target_point)
    if(angle_target_point > angle_center):
        if(angle_target_position < angle_target_point):
           return -1
        else:
            return 1
    else:
        if(angle_target_position > angle_target_point):
            return 1
        else:
            return -1


