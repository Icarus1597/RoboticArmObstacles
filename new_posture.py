import config
import PotentialFields as pf
import autograd.numpy as anp
import numpy as np
import Geometrie

def calculate_new_thetas(mode, arm, next_node_index = 0, path_node_list = [], mode_start_position = True, alpha = 0):

    # A* TODO
    if(mode == 0):
        return
    
    # PF
    elif(mode == 1):
        # Calculations for the movement of joints: Attractive Velocity
        v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([config.target_x, config.target_y], dtype=anp.float64), config.zeta)
        jacobian_matrix = arm.jacobian_matrix()
        inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
        joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

        # Calculate distance to Circle and checks if the End Effector touches the Circle
        distance = Geometrie.distance_to_circle(config.center, config.radius, arm.end_effector)
    
        # Calculates Joint Velocities for U_rep
        v_rep_joint = pf.v_rep_function(distance, config.rho_0, config.k)
        joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)

        if(arm.end_effector[1] < 0):
            joint_velocity = joint_velocity_att - joint_velocity_rep + [1E-10,1E-10,1E-10] # Very small amount so arm doesn't get stuck in start position
        else:
            joint_velocity = joint_velocity_att + joint_velocity_rep + [1E-10,1E-10,1E-10]

        # Hard maximum velocity for robot arm
        if(np.abs(joint_velocity[0])>config.max_velocity):
            joint_velocity[0] = np.sign(joint_velocity[0]) * config.max_velocity
        if(np.abs(joint_velocity[1])>config.max_velocity):
            joint_velocity[1] = np.sign(joint_velocity[1]) * config.max_velocity
        if(np.abs(joint_velocity[2])>config.max_velocity):
            joint_velocity[2] = np.sign(joint_velocity[2]) * config.max_velocity

        # Calculate the new thetas and update joints
        theta_coxa = arm.theta_coxa + config.delta_t * joint_velocity[0] * config.damping_factor
        theta_femur = arm.theta_femur + config.delta_t * joint_velocity[1] * config.damping_factor
        theta_tibia = arm.theta_tibia + config.delta_t * joint_velocity[2] * config.damping_factor
        return theta_coxa, theta_femur, theta_tibia
    
    # A* elbow TODO
    elif(mode == 2):
        return

    # Naive Approach
    elif(mode == 3):
        return arm.inverse_kinematics((config.target_x, config.target_y))
    
    # PF all links
    elif(mode == 4):
        # Calculations for the movement of joints: Attractive Velocity
        v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([config.target_x, config.target_y], dtype=anp.float64), config.zeta)
        jacobian_matrix = arm.jacobian_matrix()
        inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
        joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

        # Calculate distance to Circle and checks if the End Effector touches the Circle
        distance = Geometrie.distance_to_circle(config.center, config.radius, arm.end_effector)

        # Calculates Joint Velocities for U_rep
        v_rep_joint = pf.v_rep_function(distance, config.rho_0, config.k)
        joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)
        
        
        if(arm.end_effector[1] < 0):
            joint_velocity = joint_velocity_att - joint_velocity_rep + [1E-10,1E-10,1E-10] # Very small amount so arm doesn't get stuck in start position
        else:
            joint_velocity = joint_velocity_att + joint_velocity_rep + [1E-10,1E-10,1E-10]
        

        # Calculates Coxa-Joint Velocities for U_rep
        distance_coxa = Geometrie.distance_to_circle(config.center, config.radius, arm.joint_coxa)
    
        v_rep_joint_coxa = pf.v_rep_function(distance_coxa, config.rho_0_coxa, config.k_coxa)
        jacobian_matrix_coxa = arm.jacobian_matrix_coxa()
        inverse_jacobian_matrix_coxa = arm.inverse_jacobian_matrix(jacobian_matrix_coxa)
        joint_velocity_rep_coxa = pf.joint_velocities_rep(inverse_jacobian_matrix_coxa, v_rep_joint_coxa)

        # Calculates Femur-Joint Velocities for U_rep
        distance_femur = Geometrie.distance_to_circle(config.center, config.radius, arm.joint_femur)

        v_rep_joint_femur = pf.v_rep_function(distance_femur, config.rho_0_femur, config.k_femur)
        jacobian_matrix_femur = arm.jacobian_matrix_femur()
        inverse_jacobian_matrix_femur = arm.inverse_jacobian_matrix(jacobian_matrix_femur)
        joint_velocity_rep_femur = pf.joint_velocities_rep(inverse_jacobian_matrix_femur, v_rep_joint_femur)
        joint_velocity[0] = joint_velocity[0] + joint_velocity_rep_coxa[0] + joint_velocity_rep_femur[0]
        joint_velocity[1] = joint_velocity[1] + joint_velocity_rep_femur[1]

        # Hard maximum velocity for robot arm
        if(np.abs(joint_velocity[0])>config.max_velocity):
            joint_velocity[0] = np.sign(joint_velocity[0]) * config.max_velocity
        if(np.abs(joint_velocity[1])>config.max_velocity):
            joint_velocity[1] = np.sign(joint_velocity[1]) * config.max_velocity
        if(np.abs(joint_velocity[2])>config.max_velocity):
            joint_velocity[2] = np.sign(joint_velocity[2]) * config.max_velocity

        # Calculate the new thetas
        theta_coxa = arm.theta_coxa + config.delta_t * joint_velocity[0] * config.damping_factor
        theta_femur = arm.theta_femur + config.delta_t * joint_velocity[1] * config.damping_factor
        theta_tibia = arm.theta_tibia + config.delta_t * joint_velocity[2] * config.damping_factor*2
        return theta_coxa, theta_femur, theta_tibia
    
    # A* start position TODO
    elif(mode == 5):
        if(mode_start_position):
            target_angles = (alpha, np.pi/2, np.pi/2)
            if(not sm.arm_near_target_angles(arm, target_angles) and arm.distance_arm_obstacle(config.center, config.radius) > 2*config.min_distance_to_obstacle):
                arm.move_to_target(target_angles, tolerance = config.tolerance)
        elif (len(path_node_list)>0):
            return arm.inverse_kinematics(path_node_list[next_node_index].position)
    
    else:
        print(f"In new_posture.calculate_new_thetas: Invalid mode, mode = {mode}")
        return