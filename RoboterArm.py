import numpy as np
from numpy.linalg import LinAlgError
import autograd.numpy as anp
import math
import config

# Class RoboticArm:
# Model of a robotic arm with three joints
# with the corresponding link angles and joint lengths
# with methods to initialize the arm, update the position etc.
class RoboticArm:
    # Initializes the arm
    # Inputs:
    #   length_coxa:  length of the coxa joint
    #   length_femur: length of the femur joint
    #   length_tibia: length of the tibia joint
    def __init__(self, length_coxa, length_femur, length_tibia):
        self.length_coxa = length_coxa
        self.length_femur = length_femur
        self.length_tibia = length_tibia
        self.update_joints(0, 0, 0)

    # Updates the positions of the joints (forward kinematics)
    # Inputs:
    #   theta_coxa:  angle of the coxa link
    #   theta_femur: angle of the femur link
    #   theta_tibia: angle of the tibia link
    def update_joints(self, theta_coxa, theta_femur, theta_tibia):
        
        self.theta_coxa = theta_coxa
        self.theta_femur = theta_femur
        self.theta_tibia = theta_tibia

        # Update position of coxa-joint (end of the first segment)
        self.joint_coxa_x = self.length_coxa * np.cos(theta_coxa)
        self.joint_coxa_y = self.length_coxa * np.sin(theta_coxa)
        self.joint_coxa = anp.array([self.joint_coxa_x, self.joint_coxa_y], dtype=anp.float64)

        # Update position of the femur-joint (end of the second segment)
        self.joint_femur_x = self.joint_coxa_x + self.length_femur * np.cos(theta_coxa + theta_femur)
        self.joint_femur_y = self.joint_coxa_y + self.length_femur * np.sin(theta_coxa + theta_femur)
        self.joint_femur = anp.array([self.joint_femur_x, self.joint_femur_y], dtype=anp.float64)

        # Update position of the tibia-joint (end of the third segment)
        self.joint_tibia_x = self.joint_femur_x + self.length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia)   
        self.joint_tibia_y = self.joint_femur_y + self.length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia) 
        self.joint_tibia = anp.array([self.joint_tibia_x, self.joint_tibia_y], dtype=anp.float64)
        self.end_effector = self.joint_tibia

        #print(f"theta_coxa:{theta_coxa}, theta_femur:{theta_femur}, theta_tibia:{theta_tibia}")
        #print(f"joint_coxa:{self.joint_coxa_x},{self.joint_coxa_y}, joint_femur:{self.joint_femur_x}, {self.joint_femur_y}")

    # Calculate the Jacobian Matrix
    # Inputs:
    #   length_coxa:  length of the coxa joint
    #   length_femur: length of the femur joint
    #   length_tibia: length of the tibia joint
    #   theta_coxa:   coxa angle
    #   theta_femur:  femur angle
    #   theta_tibia:  tibia angle
    # Ouptut:
    #   j_matrix:     jacobian_matrix
    def jacobian_matrix(self) :
        j_matrix = np.array([
            [-self.length_coxa * np.sin(self.theta_coxa) - self.length_femur * np.sin(self.theta_coxa + self.theta_femur) - self.length_tibia * np.sin(self.theta_coxa + self.theta_femur + self.theta_tibia),
            -self.length_femur * np.sin(self.theta_coxa + self.theta_femur) - self.length_tibia * np.sin(self.theta_coxa + self.theta_femur + self.theta_tibia),
            -self.length_tibia * np.sin(self.theta_coxa + self.theta_femur + self.theta_tibia)],
            
            [self.length_coxa * np.cos(self.theta_coxa) + self.length_femur * np.cos(self.theta_coxa + self.theta_femur) + self.length_tibia * np.cos(self.theta_coxa + self.theta_femur + self.theta_tibia),
            self.length_femur * np.cos(self.theta_coxa + self.theta_femur) + self.length_tibia * np.cos(self.theta_coxa + self.theta_femur + self.theta_tibia),
            self.length_tibia * np.cos(self.theta_coxa + self.theta_femur + self.theta_tibia)],
            
        ])
        return j_matrix


    # Calculate the Inverse of the Jacobian Matrix. If given matrix is singular, calculates the pseudoinverse instead
    # Input:
    #   matrix: matrix, to which the inverse shall be calculated
    # Output:
    #   inv_matrix: Inverse of matrix. If matrix was singular, pseudoinverse
    def inverse_jacobian_matrix(self, matrix) :
        return np.linalg.pinv(matrix)


    # Calculates the minimum distance between a segment and a point
    # Input: 
    #   point: (Point) 
    #   segment_a, segment_b: (Point) start- and endpoint of the segment
    # Output:
    #   minimum distance between the segment and point
    def distance_segment_point(self, point_x, point_y, segment_a_x, segment_a_y, segment_b_x, segment_b_y) :
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
        

    
    # Calculates the minimum distance between all links of the arm and an circle-shaped obstacle
    # Input: 
    #   radius: Radius of the obstacle
    #   center: center of the obstacle
    # Output: 
    #   distance: minimum distance between links and obstacle
    def distance_arm_obstacle(self, center, radius) :
        # Calculates distance between each link and circle-obstacle
        distance_coxa = self.distance_segment_point(center[0], center[1], 0, 0, self.joint_coxa_x, self.joint_coxa_y) - radius
        distance_femur = self.distance_segment_point(center[0], center[1], self.joint_coxa_x, self.joint_coxa_y, self.joint_femur_x, self.joint_femur_y) - radius
        distance_tibia = self.distance_segment_point(center[0], center[1], self.joint_femur_x, self.joint_femur_y, self.joint_tibia_x, self.joint_tibia_y) - radius
        
        # Checks if arm touches the obstacle
        if(distance_coxa < 0) :
            print(f"ERROR: Coxa-Link touches the obstacle")
            return -1
        if(distance_femur < 0) :
            print(f"ERROR: Femur-Link touches the obstacle")
            return -1
        if(distance_tibia < 0) :
            print(f"ERROR: Tibia-Link touches the obstacle")
            return -1

        # Checks if arm is closer to the obstacle than the minimum required distance
        if(distance_coxa < config.min_distance_to_obstacle):
            print(f"WARNING: Coxa too close to obstacle")
        if(distance_femur < config.min_distance_to_obstacle):
            print(f"WARNING: Femur too close to obstacle")
        if(distance_tibia < config.min_distance_to_obstacle):
            print(f"WARNING: Tibia too close to obstacle")
        return min(distance_coxa, distance_femur, distance_tibia)
        