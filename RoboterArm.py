import numpy as np
from numpy.linalg import LinAlgError
import autograd.numpy as anp
import config
import Geometrie

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
        

    
    # Calculates the minimum distance between all links of the arm and an circle-shaped obstacle
    # Input: 
    #   radius: Radius of the obstacle
    #   center: center of the obstacle
    # Output: 
    #   distance: minimum distance between links and obstacle
    def distance_arm_obstacle(self, center, radius) :
        # Calculates distance between each link and circle-obstacle
        distance_coxa = Geometrie.distance_segment_point(center[0], center[1], 0, 0, self.joint_coxa_x, self.joint_coxa_y) - radius
        distance_femur = Geometrie.distance_segment_point(center[0], center[1], self.joint_coxa_x, self.joint_coxa_y, self.joint_femur_x, self.joint_femur_y) - radius
        distance_tibia = Geometrie.distance_segment_point(center[0], center[1], self.joint_femur_x, self.joint_femur_y, self.joint_tibia_x, self.joint_tibia_y) - radius
        
        # Checks if arm touches the obstacle
        if(distance_coxa < 0) :
            print(f"ERROR: Coxa-Link touches the obstacle")
            with open("testresults.txt", "a") as file:
                file.write(f"Test Result: ERROR: Coxa-Link touches the obstacle!\n")
            config.number_error_coxa += 1
            return -1
        if(distance_femur < 0) :
            print(f"ERROR: Femur-Link touches the obstacle")
            with open("testresults.txt", "a") as file:
                file.write(f"Test Result: ERROR: Femur-Link touches the obstacle!\n")
            config.number_error_femur += 1
            return -1
        if(distance_tibia < 0) :
            print(f"ERROR: Tibia-Link touches the obstacle")
            with open("testresults.txt", "a") as file:
                file.write(f"Test Result: ERROR: Tibia-Link touches the obstacle!\n")
            config.number_error_tibia += 1
            return -1

        # Checks if arm is closer to the obstacle than the minimum required distance
        if(distance_coxa < config.min_distance_to_obstacle):
            print(f"WARNING: Coxa too close to obstacle")
            config.mode_ellbow_coxa = True
            with open("testresults.txt", "a") as file:
                file.write(f"Test Result: ERROR: Coxa-Link too close to the obstacle!\n")
        if(distance_femur < config.min_distance_to_obstacle):
            print(f"WARNING: Femur too close to obstacle")
            config.mode_ellbow_coxa = True
            config.mode_ellbow_femur = True
            with open("testresults.txt", "a") as file:
                file.write(f"Test Result: ERROR: Femur-Link too close to the obstacle!\n")
        if(distance_tibia < config.min_distance_to_obstacle):
            print(f"WARNING: Tibia too close to obstacle")
            config.mode_ellbow_femur = True
            with open("testresults.txt", "a") as file:
                file.write(f"Test Result: ERROR: Tibia-Link too close to the obstacle!\n")
        return min(distance_coxa, distance_femur, distance_tibia)


    def error_target_end_effector(self, target):
        return (target[0] - self.end_effector[0], target[1] - self.end_effector[1])
        

    # Nicht inverse_kinematics im eigentlichen Sinne! Bewegt joint langsam zur Zielposition
    def inverse_kinematics(self, target):
        error = self.error_target_end_effector(target)
        jacobian_matrix = self.jacobian_matrix()
        inverse_jacobian_matrix = self.inverse_jacobian_matrix(jacobian_matrix)
        delta_theta = inverse_jacobian_matrix @ error

        #print(f"delta_coxa = {delta_theta[0]}, delta_femur = {delta_theta[1]}, delta_tibia = {delta_theta[2]}")
        
        new_theta_coxa = self.theta_coxa + 0.0001 + np.sign(delta_theta[0]) * np.minimum(abs(config.learning_rate * delta_theta[0]), 0.5)
        new_theta_femur = self.theta_femur + np.sign(delta_theta[1])* np.minimum(abs(config.learning_rate * delta_theta[1]), 0.5)
        new_theta_tibia = self.theta_tibia + np.sign(delta_theta[2])* np.minimum(abs(config.learning_rate * delta_theta[2]), 0.5)

        self.update_joints(new_theta_coxa, new_theta_femur, new_theta_tibia)
        return
    
    def move_to_target(self, target_angles, step_size=0.02, tolerance=0.01):
        """
        Bewegt den Roboterarm in kleinen Schritten zu den Zielwinkeln.

        - target_angles: Ein Array mit den Zielwinkeln [theta_coxa, theta_femur, theta_tibia].
        - step_size: Die Schrittgröße für die Bewegung.
        - tolerance: Die Toleranz, bei der die Bewegung stoppt, wenn die Differenz zwischen aktuellen und Zielwinkeln kleiner ist.
        """

        '''
        # Berechne die Differenz zwischen Zielwinkeln und aktuellen Winkeln
        delta_angles = np.array(target_angles) - np.array([self.theta_coxa, self.theta_femur, self.theta_tibia])
        
        # Solange die Differenz größer als die Toleranz ist, bewege den Arm
        while np.linalg.norm(delta_angles) > tolerance:
            # Bewege die Gelenke in kleinen Schritten
            step = np.sign(delta_angles) * np.minimum(np.abs(delta_angles), step_size)
            
            # Berechne die neuen Winkel
            new_theta_coxa = self.theta_coxa + step[0]
            new_theta_femur = self.theta_femur + step[1]
            new_theta_tibia = self.theta_tibia + step[2]
            
            # Aktualisiere die Gelenkwinkel des Arms
            self.update_joints(new_theta_coxa, new_theta_femur, new_theta_tibia)
            
            # Berechne die neue Differenz
            delta_angles = np.array(target_angles) - np.array([new_theta_coxa, new_theta_femur, new_theta_tibia])
        '''
        delta_angles = np.array(target_angles) - np.array([self.theta_coxa, self.theta_femur, self.theta_tibia])
        new_theta_coxa = self.theta_coxa + np.sign(delta_angles[0]) * np.minimum(np.abs(delta_angles[0]), step_size)
        new_theta_femur = self.theta_femur + np.sign(delta_angles[1]) * np.minimum(np.abs(delta_angles[1]), step_size)
        new_theta_tibia = self.theta_tibia + np.sign(delta_angles[2]) * np.minimum(np.abs(delta_angles[2]), step_size)
        print(f"move to target new thetas: coxa = {new_theta_coxa}, femur = {new_theta_femur}, tibia = {new_theta_tibia}")
        self.update_joints(new_theta_coxa, new_theta_femur, new_theta_tibia)


    def reflect_femur_link(self):
        # Current angles of the links
        theta_coxa = self.theta_coxa  
        theta_femur = self.theta_femur  # Reflect
        theta_tibia = self.theta_tibia 

        if(theta_femur % (np.pi*2) < np.pi):
            factor = 1
        else:
            factor = -1

        # Reflect theta femur
        theta_femur = (- theta_femur) % (np.pi*2)

        # Vector Coxa Joint
        vector_coxa_1 = self.joint_coxa[0]
        vector_coxa_2 = self.joint_coxa[1]

        # Vector Coxa Link to Tibia Link
        vector_coxa_tibia_1 = self.joint_femur[0]
        vector_coxa_tibia_2 = self.joint_femur[1]

        # Length Femur Link to End Effector
        length_coxa_tibia = np.sqrt(vector_coxa_tibia_1**2 + vector_coxa_tibia_2**2)

        # Calculate alpha
        # Definitionsmenge arccos: [-1, 1]
        temp = (vector_coxa_1*vector_coxa_tibia_1 + vector_coxa_2*vector_coxa_tibia_2)/(self.length_femur*length_coxa_tibia)

        if (np.abs(temp)>1):
            print(f"Reflect Femur Link: Value for Arccos out of range")
            temp = np.sign(temp)* abs(temp) % 1
        print(f"Temp femur = {temp}")
        alpha = np.arccos(temp)
        

        # Calculate Theta Coxa
        theta_coxa = (theta_coxa + factor * alpha*2) % (np.pi*2)

        # Calculate theta tibia
        
        # Dritten Winkel im Dreieck über Innnenwinkelsumme berechnen
        gamma = np.pi - alpha + factor * (np.pi - theta_femur)

        theta_tibia = (theta_tibia + factor*2*gamma)

        theta_coxa = theta_coxa % (np.pi*2)
        theta_femur = theta_femur % (np.pi*2)
        theta_tibia = theta_tibia % (np.pi*2)
        
        print(f"Reflect femur link result: coxa = {theta_coxa}, femur = {theta_femur}, tibia = {theta_tibia}")

        return theta_coxa, theta_femur, theta_tibia


    def reflect_tibia_link(self):
        # Current angles of the links
        theta_coxa = self.theta_coxa  # Stays the same
        theta_femur = self.theta_femur  # Calculate
        theta_tibia = self.theta_tibia  # Reflect

        if(theta_tibia % (np.pi*2) < np.pi):
            factor = 1
        else:
            factor = -1

        theta_tibia = - theta_tibia

        # Calculate new theta_femur

        # Vektor Femur Joint
        vector_femur_1 = self.joint_femur[0]- self.joint_coxa[0]
        vector_femur_2 = self.joint_femur[1]- self.joint_coxa[1]

        # Vektor Femur Link to End Effector
        vector_femur_ee_1 = self.joint_tibia[0] - self.joint_coxa[0]
        vector_femur_ee_2 = self.joint_tibia[1] - self.joint_coxa[1]

        # Length Femur Link to End Effector
        length_femur_ee = np.sqrt(vector_femur_ee_1**2 + vector_femur_ee_2**2)

        # Calculate alpha
        temp = (vector_femur_1*vector_femur_ee_1 + vector_femur_2*vector_femur_ee_2)/(self.length_femur*length_femur_ee)
        if (np.abs(temp)>1):
            print(f"Reflect Tibia Link: Value for Arccos out of range")
            temp = np.sign(temp)* abs(temp) % 1
        #print(f"Temp tibia = {temp}")

        alpha = np.arccos(temp)


        # Theta Coxa berechnen
        theta_femur = theta_femur + factor * alpha*2

        theta_coxa = theta_coxa % (np.pi*2)
        theta_femur = theta_femur % (np.pi*2)
        theta_tibia = theta_tibia % (np.pi*2)

        print(f"Reflect tibia link result: coxa = {theta_coxa}, femur = {theta_femur}, tibia = {theta_tibia}")
        return theta_coxa, theta_femur, theta_tibia




