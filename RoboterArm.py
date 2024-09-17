import numpy as np
from numpy.linalg import LinAlgError
import autograd.numpy as anp

# Class RoboticArm:
# Model of a robotic arm with three joints
# with the corresponding link angles and joint lengths
# with methods to initialize the arm, update the position etc.
class RoboticArm:
    theta_coxa = 0
    theta_femur = 0
    theta_tibia = 0

    # Initializes the arm
    # Inputs:
    # length_coxa:  length of the coxa joint
    # length_femur: length of the femur joint
    # length_tibia: length of the tibia joint
    def __init__(self, length_coxa, length_femur, length_tibia):
        self.length_coxa = length_coxa
        self.length_femur = length_femur
        self.length_tibia = length_tibia
        self.joint_coxa = anp.array([0, 0], dtype=anp.float64)
        self.joint_femur = anp.array([0, 0], dtype=anp.float64)
        self.joint_tibia = anp.array([0, 0], dtype=anp.float64)
        self.end_effector = anp.array([0, 0])

    # Updates the positions of the joints (forward kinematics)
    # Inputs:
    # theta_coxa:  angle of the coxa link
    # theta_femur: angle of the femur link
    # theta_tibia: angle of the tibia link
    def update_joints(self, theta_coxa, theta_femur, theta_tibia):
        # Update position of coxa-joint (end of the first segment)
        x1 = self.length_coxa * np.cos(theta_coxa)
        y1 = self.length_coxa * np.sin(theta_coxa)
        self.joint_coxa = anp.array([x1, y1], dtype=anp.float64)

        # Update position of the femur-joint (end of the second segment)
        x2 = x1 + self.length_femur * np.cos(theta_coxa + theta_femur)
        y2 = y1 + self.length_femur * np.sin(theta_coxa + theta_femur)
        self.joint_femur = anp.array([x2, y2], dtype=anp.float64)

        # Update position of the tibia-joint (end of the third segment)
        x3 = x2 + self.length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia)   
        y3 = y2 + self.length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia) 
        self.joint_tibia = anp.array([x3, y3], dtype=anp.float64)
        self.end_effector = self.joint_tibia

    # Getter and Setter for the thetas

    # Get the coxa angle
    # Output:
    # theta_coxa: coxa angle
    def get_theta_coxa(self):
        return self.theta_coxa
    
    # Set the coxa angle
    # Input:
    # theta_coxa: new value for the coxa angle
    def set_theta_coxa(self, theta_coxa):
        self.theta_coxa = theta_coxa
    
    # Get the femur angle
    # Output:
    # theta_femur: femur angle
    def get_theta_femur(self):
        return self.theta_femur
    
    # Set the femur angle
    # Input:
    # theta_femur: new value for the femur angle
    def set_theta_femur(self, theta_femur):
        self.theta_femur = theta_femur

    # Get the tibia angle
    # Output:
    # theta_tibia: tibia angle
    def get_theta_tibia(self):
        return self.theta_tibia
    
    # Set the tibia angle
    # Input:
    # theta_tibia: new value for the tibia angle
    def set_theta_tibia(self, theta_tibia):
        self.theta_tibia = theta_tibia

    # Calculate the Jacobian Matrix
    # Inputs:
    # length_coxa:  length of the coxa joint
    # length_femur: length of the femur joint
    # length_tibia: length of the tibia joint
    # theta_coxa:   coxa angle
    # theta_femur:  femur angle
    # theta_tibia:  tibia angle
    # Ouptut:
    # j_matrix:     jacobian_matrix
    def jacobian_matrix(self, length_coxa, length_femur, length_tibia, theta_coxa, theta_femur, theta_tibia) :
        j_matrix = np.array([
            [-length_coxa * np.sin(theta_coxa) - length_femur * np.sin(theta_coxa + theta_femur) - length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia),
            -length_femur * np.sin(theta_coxa + theta_femur) - length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia),
            -length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia)],
            
            [length_coxa * np.cos(theta_coxa) + length_femur * np.cos(theta_coxa + theta_femur) + length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia),
            length_femur * np.cos(theta_coxa + theta_femur) + length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia),
            length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia)],
            
            [1, 1, 1]
        ])
        return j_matrix


    # Calculate the Inverse of the Jacobian Matrix. If given matrix is singular, calculates the pseudoinverse instead
    # Input:
    # matrix: matrix, to which the inverse shall be calculated
    # Output:
    # inv_matrix: Inverse of matrix. If matrix was singular, pseudoinverse
    def inverse_jacobian_matrix(self, matrix) :
        try:
        # Try to calculate the inverse matrix
            inv_matrix = np.linalg.inv(matrix)
        except LinAlgError:
            # If the matrix is singular, calculate the pseudoinverse instead
            inv_matrix = np.linalg.pinv(matrix)
            #print("Matrix is singular. Pseudoinverse:")
            #print(inv_matrix)
        return inv_matrix