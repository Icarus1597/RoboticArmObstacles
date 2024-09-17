import numpy as np
from autograd import grad
import autograd.numpy as anp


# Traditional Potential Field (https://www.mdpi.com/1424-8220/23/7/3754)

# Attractive Potential Field 
# Inputs:
# pos_ee     : position end effector
# pos_target : position target
# zeta       : attractive potential gain
# Ouputs:
# u_att      : attractive potential field
def u_att_function(pos_ee, pos_target, zeta) :
    # rho : cartesian distance end effector pos_ee and target pos_target
    rho = cartesian_distance(pos_ee, pos_target)
    u_att = 1/2 * zeta * rho * rho
    return u_att

# Cartesian distance of two points
# Inputs:
# point1, point2: the two points for which the distance between them shall be calculated
# Outputs: 
# distance      : cartesian distance between point1 and point2
def cartesian_distance(point1, point2):
    point1 = anp.array(point1, dtype=anp.float64)
    point2 = anp.array(point2, dtype=anp.float64)
    # Calculate the vector of difference
    difference = point1 - point2
    # Calculate the norm of the vector
    distance = anp.sqrt(anp.sum(difference ** 2))
    return distance
    
# Repulsive Potential Field
# Inputs:
# rho_b : minimum distance robot body TODO to obstacle
# rho_0 : max range repulsive field
# k     : repulsive potential gain
# Outputs:
# u_rep : Repulsive Potential Field
def u_rep_function(rho_b, rho_0, k) :
    if (rho_b <= rho_0) :
        u_rep = 1/2 * k * pow((1/rho_b - 1/rho_0), 2)
    else :
        u_rep = 0
    return u_rep

# Attraction Velocity (gradient of the potential field) in Cartesian Space
# Inputs:
# pos_ee      : position end effector
# pos_target  : position target
# zeta        : attractive potential gain
# Ouputs:
# -v_att      : attraction velocity in cartesian space
def v_att_function(pos_ee, pos_target, zeta) :
    def potential_function(pos_ee):
        return u_att_function(pos_ee, pos_target, zeta)
    
    # Calculate the gradient with respect to pos_ee
    grad_function = grad(potential_function)
    
    # Compute the gradient at the given pos_ee
    v_att = grad_function(pos_ee)
    
    return -v_att

# TODO
def V_att(v_att):
    return np.array([0, v_att[0], v_att[1]])

# Repulsive Velocity in Cartesian Space
# Input:
# rho_b : minimum distance robot body TODO to obstacle
# rho_0 : max range repulsive field
# k     : repulsive potential gain
# Output:
# -v_rep: Gradient of the Potential Field and Repulsive Velocity in Cartesian Space
def v_rep_function(rho_b, rho_0, k) :
    def potential_funkction(rho_b):
        return u_rep_function(rho_b, rho_0, k)
    v_rep = grad(potential_funkction)
    return -v_rep

# TODO
def V_rep(v_rep):
    return np.array([0, v_rep[0], v_rep[1]])

# Calculates the Joint Velocities from Cartesian Space to Joint Space for the Attractive Velocity
# Inputs:
# inverse_jacobian_matrix: Inverse Jacobian Matrix of current state of the robotic arm
# v_att                  : Attraction Velocity in Cartesian Space
# Output:
# Attraction Velocity in Joint Space
def joint_velocities_att(inverse_jacobian_matrix, v_att) :
    #print("Inverse Jacobian Matrix:")
    #print(inverse_jacobian_matrix)
    #print("v_att:")
    #print(v_att)
    return inverse_jacobian_matrix * V_att(v_att)

# Calculates the Joint Velocities from Cartesian Space to Joint Space for the Repulsive Velocity
# Inputs:
# inverse_jacobian_matrix: Inverse Jacobian Matrix of current state of the robotic arm
# v_rep                  : Repulsive Velocity in Cartesian Space
# Output:
# Repulsive Velocity in Joint Space
def joint_velocities_rep(inverse_jacobian_matrix, v_rep) :
    return inverse_jacobian_matrix * V_rep(v_rep)

