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
    '''
    def jacobian_matrix_knee(self):
        """
        Berechnet die Jacobian-Matrix für das Kniegelenk (Femur-Tibia).
        
        - Die Matrix berücksichtigt die Änderungen der Position des Knies (x, y)
        basierend auf den Gelenkwinkeln:
        - theta_femur (Femur-Gelenk)
        - theta_tibia (Tibia-Gelenk)
        
        Rückgabe:
        - 2x2 Matrix mit den partiellen Ableitungen der Knie-Position (x, y)
        nach den Gelenkwinkeln (theta_femur, theta_tibia).
        """
        # Coxa-Femur und Femur-Tibia Längen
        l1 = self.length_femur  # Länge des Femur-Segments
        l2 = self.length_tibia   # Länge des Tibia-Segments

        # Berechnung der partiellen Ableitungen
        # x-Ableitungen
        dx_dtheta_femur = -l1 * np.sin(self.theta_coxa + self.theta_femur) - l2 * np.sin(self.theta_coxa + self.theta_femur + self.theta_tibia)
        dx_dtheta_tibia = -l2 * np.sin(self.theta_coxa + self.theta_femur + self.theta_tibia)

        # y-Ableitungen
        dy_dtheta_femur = l1 * np.cos(self.theta_coxa + self.theta_femur) + l2 * np.cos(self.theta_coxa + self.theta_femur + self.theta_tibia)
        dy_dtheta_tibia = l2 * np.cos(self.theta_coxa + self.theta_femur + self.theta_tibia)

        # Setze die Jacobian-Matrix für das Kniegelenk zusammen (2x2 Matrix für das Knie)
        jacobian_knee = np.array([
            [dx_dtheta_femur, dx_dtheta_tibia],
            [dy_dtheta_femur, dy_dtheta_tibia]
        ])
        
        return jacobian_knee
    '''
    


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
    
    def move_to_target(self, target_angles, step_size=0.001, tolerance=0.01):
        """
        Bewegt den Roboterarm in kleinen Schritten zu den Zielwinkeln.

        - target_angles: Ein Array mit den Zielwinkeln [theta_coxa, theta_femur, theta_tibia].
        - step_size: Die Schrittgröße für die Bewegung.
        - tolerance: Die Toleranz, bei der die Bewegung stoppt, wenn die Differenz zwischen aktuellen und Zielwinkeln kleiner ist.
        """
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
    
    # For posture changing of femur link
    def calculate_femur_angle(self, elbow_target):
        """
        Berechnet den Winkel des Femur-Links (zwischen Coxa und Femur)
        anhand der Zielkoordinaten des Ellbogens.
        """
        x_elbow, y_elbow = elbow_target
        distance = np.sqrt(x_elbow**2 + y_elbow**2)  # Distanz vom Ursprung zum Ellbogen

        if distance > (self.length_femur + self.length_tibia) or distance < abs(self.length_femur - self.length_tibia):
            raise ValueError("Das Ziel ist außerhalb des Arbeitsbereichs des Arms")

        # Berechnung des Femur-Winkels mit Cosinusregel
        cos_theta_femur = (self.length_femur**2 + distance**2 - self.length_tibia**2) / (2 * self.length_femur * distance)
        cos_theta_femur = np.clip(cos_theta_femur, -1.0, 1.0)  # Numerische Sicherheit
        femur_angle = np.arccos(cos_theta_femur)  # Winkel in Bogenmaß

        return femur_angle  # In Radiant

    # For posture changing of tibia link
    def calculate_tibia_angle(self, end_effector_target, elbow_target):
        """
        Berechnet den Winkel des Tibia-Links (zwischen Femur und Tibia)
        anhand der Zielkoordinaten des Endeffektors.
        """
        x_eff, y_eff = end_effector_target
        x_elbow, y_elbow = elbow_target
        distance = np.sqrt((x_eff - x_elbow)**2 + (y_eff - y_elbow)**2)  # Distanz Ellbogen-Endeffektor

        if distance > (self.length_femur + self.length_tibia) or distance < abs(self.length_femur - self.length_tibia):
            raise ValueError("Das Ziel ist außerhalb des Arbeitsbereichs des Arms")

        # Berechnung des Tibia-Winkels mit Cosinusregel
        cos_theta_tibia = (self.length_femur**2 + self.length_tibia**2 - distance**2) / (2 * self.length_femur * self.length_tibia)
        cos_theta_tibia = np.clip(cos_theta_tibia, -1.0, 1.0)  # Numerische Sicherheit
        tibia_angle = np.arccos(cos_theta_tibia)  # Winkel in Bogenmaß

        return tibia_angle  # In Radiant
    
    '''
    # TODO for tibia link
    def inverse_kinematics_with_tibia(self, target, tibia_angle=None):
        """
        Berechnet die inverse Kinematik für den planaren Roboterarm mit einem Zielwinkel für das Tibia-Gelenk (Femur-Tibia-Winkel).

        - target: Endeffektor-Zielposition (x, y)
        - tibia_angle: Zielwinkel für das Tibia-Gelenk (Femur-Tibia-Winkel)
        """
        # Berechne den Fehler des Endeffektors
        error = self.error_target_end_effector(target)
        
        # Berechne die Jacobian-Matrix
        jacobian_matrix = self.jacobian_matrix()

        # Falls ein Ziel-Tibiawinkel gegeben ist, berücksichtige ihn in der Berechnung
        if tibia_angle is not None:
            # Berechne die Abweichung vom Zielwinkel
            tibia_error = tibia_angle - self.theta_tibia
            
            # Füge den Tibia-Fehler als zusätzliche Zeile zur Jacobian-Matrix hinzu
            jacobian_matrix_tibia = self.jacobian_matrix_tibia()#.reshape(2, 1)
            #jacobian_matrix_tibia = np.reshape(jacobian_matrix_tibia, (1, -1))
            jacobian_matrix = np.concatenate((jacobian_matrix, jacobian_matrix_tibia), axis=1)
            
            # Erweitere den Fehler-Vektor um die Tibia-Abweichung
            error = np.append(error, tibia_error)

        # Berechne das Delta für die Gelenkwinkel
        inverse_jacobian_matrix = self.inverse_jacobian_matrix(jacobian_matrix)
        delta_theta = inverse_jacobian_matrix @ error

        # Update der Gelenkwinkel mit den berechneten Änderungen
        new_theta_coxa = self.theta_coxa + np.sign(delta_theta[0]) * np.minimum(abs(config.learning_rate * delta_theta[0]), 0.5)
        new_theta_femur = self.theta_femur + np.sign(delta_theta[1]) * np.minimum(abs(config.learning_rate * delta_theta[1]), 0.5)
        new_theta_tibia = self.theta_tibia + np.sign(delta_theta[2]) * np.minimum(abs(config.learning_rate * delta_theta[2]), 0.5)

        # Falls ein Zielwinkel für das Tibia-Gelenk gegeben ist, nutze diesen als neuen Winkel
        if tibia_angle is not None:
            new_theta_tibia = tibia_angle  

        # Aktualisiere die Gelenkwinkel des Arms
        self.update_joints(new_theta_coxa, new_theta_femur, new_theta_tibia)

        return
    
    def jacobian_matrix_tibia(self):
        """
        Berechnet die Jacobian-Matrix für das Tibia-Gelenk.
        
        - Die Matrix berücksichtigt die Änderungen der Position des Tibia-Endpunkts (x, y)
        basierend auf den Gelenkwinkeln:
        - theta_femur (Femur-Gelenk)
        - theta_tibia (Tibia-Gelenk)
        
        Rückgabe:
        - 2x1 Matrix mit den partiellen Ableitungen der Tibia-Position (x, y)
        nach dem Gelenkwinkel (theta_tibia).
        """
        # Femur-Tibia und Tibia Längen
        l1 = self.length_femur  # Länge des Femur-Segments
        l2 = self.length_tibia   # Länge des Tibia-Segments

        # Berechnung der partiellen Ableitungen
        # x-Ableitung
        dx_dtheta_tibia = -l2 * np.sin(self.theta_coxa + self.theta_femur + self.theta_tibia)

        # y-Ableitung
        dy_dtheta_tibia = l2 * np.cos(self.theta_coxa + self.theta_femur + self.theta_tibia)

        # Setze die Jacobian-Matrix für das Tibia-Gelenk zusammen (2x1 Matrix für Tibia)
        jacobian_tibia = np.array([
            [dx_dtheta_tibia],
            [dy_dtheta_tibia]
        ])

        jacobian_tibia = np.array([dx_dtheta_tibia, dy_dtheta_tibia])#.reshape(2, 1)
        
        return jacobian_tibia
    


    # TODO for femur link
    def inverse_kinematics_with_knee(self, target, knee_angle=None):
        """
        Berechnet die inverse Kinematik für den planaren Roboterarm mit einem Zielwinkel für das Knie (Coxa-Femur-Gelenk).

        - target: Endeffektor-Zielposition (x, y)
        - knee_angle: Zielwinkel für das Coxa-Femur-Gelenk
        """
        # Berechne den Fehler des Endeffektors
        error = self.error_target_end_effector(target)
        
        # Berechne die Jacobian-Matrix
        jacobian_matrix = self.jacobian_matrix()

        # Falls ein Ziel-Kniewinkel gegeben ist, berücksichtige ihn in der Berechnung
        if knee_angle is not None:
            # Berechne die Abweichung vom Zielwinkel
            knee_error = knee_angle - self.theta_femur
            
            # Füge den Knie-Fehler als zusätzliche Zeile zur Jacobian-Matrix hinzu
            jacobian_matrix_knee = self.jacobian_matrix_knee()#.reshape(2, 1)
            jacobian_matrix = np.concatenate((jacobian_matrix, jacobian_matrix_knee), axis=1)
            
            # Erweitere den Fehler-Vektor um die Knie-Abweichung
            error = np.append(error, knee_error)

        # Berechne das Delta für die Gelenkwinkel
        inverse_jacobian_matrix = self.inverse_jacobian_matrix(jacobian_matrix)
        delta_theta = inverse_jacobian_matrix @ error

        # Update der Gelenkwinkel mit den berechneten Änderungen
        new_theta_coxa = self.theta_coxa + np.sign(delta_theta[0]) * np.minimum(abs(config.learning_rate * delta_theta[0]), 0.5)
        new_theta_femur = self.theta_femur + np.sign(delta_theta[1]) * np.minimum(abs(config.learning_rate * delta_theta[1]), 0.5)
        new_theta_tibia = self.theta_tibia + np.sign(delta_theta[2]) * np.minimum(abs(config.learning_rate * delta_theta[2]), 0.5)

        # Falls ein Zielwinkel für das Knie gegeben ist, nutze diesen als neuen Winkel
        if knee_angle is not None:
            new_theta_femur = knee_angle  

        # Aktualisiere die Gelenkwinkel des Arms
        self.update_joints(new_theta_coxa, new_theta_femur, new_theta_tibia)

        return
    
    import numpy as np

    '''

    #So funktioniert das nicht wie ich mir das vorgestellt habe
    

    # For posture changing of the tibia link
    def reflect_tibia_and_femur(self):
        """
        Spiegelt den Tibia-Link und berechnet auch den Femur-Winkel,
        während der Coxa-Winkel unverändert bleibt.
        """
        # Aktuelle Gelenkwinkel
        theta_coxa = self.theta_coxa  # Coxa-Winkel bleibt unverändert
        theta_femur = self.theta_femur  # Femur-Winkel, der angepasst werden muss
        theta_tibia = self.theta_tibia  # Tibia-Winkel, der gespiegelt werden soll
        
        # Spiegeln des Tibia-Winkels (umkehren des Winkels)
        new_theta_tibia = -theta_tibia
        
        # Um den Femur-Winkel zu berechnen, nutzen wir die Inverse Kinematik
        # Nehmen wir an, dass der Arm auf einer Ebene funktioniert (planarer Roboterarm)
        
        # Berechnung der neuen Winkel
        # Hier müssen wir die neuen Theta-Werte durch inverse Kinematik berechnen
        # Diese Berechnungen setzen voraus, dass du eine Methode hast, um die
        # Gelenkwinkel zu berechnen, die den Endeffektor an der gewünschten Position
        # halten. Zum Beispiel könnte das so aussehen:

        # Berechne die Endeffektor-Position, basierend auf den aktuellen Werten
        x_end_effector = self.length_coxa * np.cos(theta_coxa) + self.length_femur * np.cos(theta_coxa + theta_femur) + self.length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia)
        y_end_effector = self.length_coxa * np.sin(theta_coxa) + self.length_femur * np.sin(theta_coxa + theta_femur) + self.length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia)
        
        # Berechne die neue Position des Endeffektors, wenn der Tibia gespiegelt wird
        # (die X- und Y-Position bleiben gleich, aber der Tibia-Winkel wird gespiegelt)
        new_x_end_effector = self.length_coxa * np.cos(theta_coxa) + self.length_femur * np.cos(theta_coxa + theta_femur) + self.length_tibia * np.cos(theta_coxa + theta_femur + new_theta_tibia)
        new_y_end_effector = self.length_coxa * np.sin(theta_coxa) + self.length_femur * np.sin(theta_coxa + theta_femur) + self.length_tibia * np.sin(theta_coxa + theta_femur + new_theta_tibia)
        
        # Berechne den Fehler in der Endeffektor-Position
        delta_x = x_end_effector - new_x_end_effector
        delta_y = y_end_effector - new_y_end_effector
        
        # Berechne den neuen Femur-Winkel unter Verwendung der inverse Kinematik
        # Hier könnte eine Näherung verwendet werden, um den Femur-Winkel zu berechnen, damit der Fehler minimiert wird.
        # Ein Beispiel könnte wie folgt aussehen:
        delta_theta_femur = np.arctan2(delta_y, delta_x)  # Dies ist eine einfache Näherung
        
        # Berechne den neuen Femur-Winkel
        new_theta_femur = theta_femur + delta_theta_femur
        
        # Setze die neuen Winkel
        self.update_joints(theta_coxa, new_theta_femur, new_theta_tibia)
        
        return theta_coxa, new_theta_femur, new_theta_tibia
    
    
    #import numpy as np

    # For posture changing of the femur link
    def reflect_coxa_and_femur(self):
        """
        Spiegelt den Coxa- und Femur-Link und berechnet die neuen Gelenkwinkel,
        während der Tibia-Winkel unverändert bleibt.
        """
        # Aktuelle Gelenkwinkel
        theta_coxa = self.theta_coxa  # Coxa-Winkel, der reflektiert werden soll
        theta_femur = self.theta_femur  # Femur-Winkel, der ebenfalls reflektiert wird
        theta_tibia = self.theta_tibia  # Tibia-Winkel bleibt unverändert
        
        # Spiegeln des Coxa-Winkels (umkehren des Winkels)
        new_theta_coxa = -theta_coxa
        
        # Spiegeln des Femur-Winkels (umkehren des Winkels)
        new_theta_femur = -theta_femur
        
        # Berechne die Endeffektor-Position, basierend auf den aktuellen Werten
        x_end_effector = self.length_coxa * np.cos(theta_coxa) + self.length_femur * np.cos(theta_coxa + theta_femur) + self.length_tibia * np.cos(theta_coxa + theta_femur + theta_tibia)
        y_end_effector = self.length_coxa * np.sin(theta_coxa) + self.length_femur * np.sin(theta_coxa + theta_femur) + self.length_tibia * np.sin(theta_coxa + theta_femur + theta_tibia)
        
        # Berechne die neue Position des Endeffektors, wenn der Coxa- und Femur-Winkel gespiegelt werden
        new_x_end_effector = self.length_coxa * np.cos(new_theta_coxa) + self.length_femur * np.cos(new_theta_coxa + new_theta_femur) + self.length_tibia * np.cos(new_theta_coxa + new_theta_femur + theta_tibia)
        new_y_end_effector = self.length_coxa * np.sin(new_theta_coxa) + self.length_femur * np.sin(new_theta_coxa + new_theta_femur) + self.length_tibia * np.sin(new_theta_coxa + new_theta_femur + theta_tibia)
        
        # Berechne den Fehler in der Endeffektor-Position
        delta_x = x_end_effector - new_x_end_effector
        delta_y = y_end_effector - new_y_end_effector
        
        # Berechne den Fehler in den Gelenkwinkeln (zum Beispiel durch inverse Kinematik)
        delta_theta_coxa = np.arctan2(delta_y, delta_x)  # Dies ist eine einfache Näherung
        delta_theta_femur = np.arctan2(delta_y, delta_x)  # Auch eine Näherung
        
        # Berechne den neuen Coxa- und Femur-Winkel
        new_theta_coxa += delta_theta_coxa
        new_theta_femur += delta_theta_femur
        
        # Setze die neuen Winkel
        self.update_joints(new_theta_coxa, new_theta_femur, theta_tibia)
        
        return new_theta_coxa, new_theta_femur, theta_tibia


