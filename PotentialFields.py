import numpy as np
from autograd import grad
import autograd.numpy as anp

# Attractive Potential Field 
# Inputs:
# pos_ee     : position end effector
# pos_target : position target
# zeta       : attractive potential gain
# Ouputs:
# u_att      : attractive potential field
def u_att_function(pos_ee, pos_target, zeta) :
    #print(f"pos_ee:{pos_ee}, pos_target:{pos_target}")
    # rho : cartesian distance end effector pos_ee and target pos_target
    rho = cartesian_distance(pos_target, pos_ee)
    #print(f"Distance EE to target: {rho}")
    u_att = 1/2 * zeta * rho **2
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

# Converts v_att to Vector with omega_att the angular velocity (which is zero)
# Input:
# v_att : Attraction Velocity in Cartesian Space
# Output:
# V_att : Attraction Velocity in Cartesian SPace Array 3x1 with added omega_att = 0
def V_att(v_att): 
    #TODO: muss ich überhaupt transponieren?
    return np.array([v_att[0], v_att[1]]).T

# Repulsive Velocity in Cartesian Space
# Input:
# rho_b : minimum distance robot body TODO to obstacle
# rho_0 : max range repulsive field
# k     : repulsive potential gain
# Output:
# v_rep: Gradient of the Potential Field and Repulsive Velocity in Cartesian Space
def v_rep_function(rho_b, rho_0, k) :
    if(rho_b <= rho_0):
        v_rep = k * (1/rho_b - 1/rho_0) * 1 / rho_b**2
        return v_rep
    return 0
#def v_rep_function(pos_ee, pos_obstacle, rho_b, rho_0, k):
   # if rho_b <= rho_0:
   #     grad_rep = (1 / rho_b - 1 / rho_0) * (1 / rho_b**2)
   #     rep_direction = (pos_ee - pos_obstacle) / rho_b  # Vector pointing away from the obstacle
   #     v_rep = k * grad_rep * rep_direction
   #     return v_rep
  #  return np.zeros_like(pos_ee)

# Repulsive Velocity in Cartesian Space with angular velocity added
# Input:
# v_rep : Repulsive Velocity in Cartesian Space, is a Scalar
# Output:
# V_rep : Repulsive Velocity in Cartesian Space, is a 3x1 Vector, with added Angular Velocities omega_rep
def V_rep(v_rep):
    return np.array([0, v_rep])

# Calculates the Joint Velocities from Cartesian Space to Joint Space for the Attractive Velocity
# Inputs:
# inverse_jacobian_matrix: Inverse Jacobian Matrix of current state of the robotic arm
# v_att                  : Attraction Velocity in Cartesian Space
# Output:
# Attraction Velocity in Joint Space
def joint_velocities_att(inverse_jacobian_matrix, v_att) :
    v_att_vec = V_att(v_att)
    return np.dot(inverse_jacobian_matrix, v_att_vec)
    #return np.dot(inverse_jacobian_matrix, V_att(v_att))

# Calculates the Joint Velocities from Cartesian Space to Joint Space for the Repulsive Velocity
# Inputs:
# inverse_jacobian_matrix: Inverse Jacobian Matrix of current state of the robotic arm
# v_rep                  : Repulsive Velocity in Cartesian Space
# Output:
# Repulsive Velocity in Joint Space
def joint_velocities_rep(inverse_jacobian_matrix, v_rep) :
    return np.dot(inverse_jacobian_matrix, V_rep(v_rep))

