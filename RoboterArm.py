import numpy as np
from numpy.linalg import LinAlgError
import autograd.numpy as anp

# Class RoboticArm:
# Model of a robotic arm with three joints
# with the corresponding link angles and joint lengths
# with methods to initialize the arm, update the position etc.
class RoboticArm:
    # Initializes the arm
    # Inputs:
    # length_coxa:  length of the coxa joint
    # length_femur: length of the femur joint
    # length_tibia: length of the tibia joint
    def __init__(self, length_coxa, length_femur, length_tibia):
        self.length_coxa = length_coxa
        self.length_femur = length_femur
        self.length_tibia = length_tibia
        self.update_joints(0, 0, 0)

    # Updates the positions of the joints (forward kinematics)
    # Inputs:
    # theta_coxa:  angle of the coxa link
    # theta_femur: angle of the femur link
    # theta_tibia: angle of the tibia link
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
    # length_coxa:  length of the coxa joint
    # length_femur: length of the femur joint
    # length_tibia: length of the tibia joint
    # theta_coxa:   coxa angle
    # theta_femur:  femur angle
    # theta_tibia:  tibia angle
    # Ouptut:
    # j_matrix:     jacobian_matrix
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
    # matrix: matrix, to which the inverse shall be calculated
    # Output:
    # inv_matrix: Inverse of matrix. If matrix was singular, pseudoinverse
    def inverse_jacobian_matrix(self, matrix) :
        return np.linalg.pinv(matrix)