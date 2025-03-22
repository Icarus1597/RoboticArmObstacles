import numpy as np
from autograd import grad
import Geometrie
import config

def u_att_function(pos_ee, pos_target, zeta) :
    """ Calculates the Attractive Potential Field to attract the end effector to the target point

    Args:
        pos_ee ((float, float)): position of the end effector of robotic arm
        pos_target ((float, float)): position of the target point
        zeta (float): attractive potential gain

    Returns:
        float: attractive potential field value for current position of end effector
    """
    # rho : cartesian distance end effector pos_ee and target pos_target
    rho = Geometrie.cartesian_distance(pos_target, pos_ee)

    u_att = 1/2 * zeta * rho **2
    return u_att
    
def u_rep_function(pos_ee, rho_0, k) :
    """Calculates the Repulsive Potential Field which repels from the obstacle

    Args:
        rho_b (float): minimum distance robot linkage TODO ? to obstacle
        rho_0 (float): max range repulsive field
        k (float): repulsive potential gain

    Returns:
        float : Repulsive Potential Field
    """
    rho_b = Geometrie.distance_to_circle(config.center, config.radius, pos_ee)
    if (rho_b <= rho_0) :
        u_rep = 1/2 * k * (1/rho_b - 1/rho_0) ** 2
        return u_rep
    return 0.

def v_att_function(pos_ee, pos_target, zeta) :
    """ Attraction Velocity (gradient of the potential field) in Cartesian Space.

    Args:
        pos_ee ((float, float)): position end effector
        pos_target ((float, float)): position target
        zeta (float): attractive potential gain

    Returns: 
        float[] : attraction velocity in cartesian space
    """
    def potential_function_att(pos_ee):
        return u_att_function(pos_ee, pos_target, zeta)
    
    # Calculate the gradient with respect to pos_ee
    grad_function = grad(potential_function_att)
    
    # Compute the gradient at the given pos_ee
    v_att = grad_function(pos_ee)
    return -v_att

def V_att(v_att): 
    """ Converts v_att to vector with omega_att the angular velocity (which is zero)

    Args:
        v_att (float): Attraction Velocity in Cartesian Space

    Returns:
        float[] : Attraction Velocity in Cartesian SPace Array 3x1 with added omega_att = 0
    """
    return np.array([v_att[0], v_att[1]]).T

def v_rep_function(pos_ee, rho_0, k) :
    """ Repulsive Velocity in Cartesian Space

    Args:
        rho_b (float): minimum distance arm linkage to obstacle
        rho_0 (float): max range repulsive field
        k (float): repulsive potential gain

    Returns:
        float[] : Gradient of the Potential Field and Repulsive Velocity in Cartesian Space, 2x1 vector
    """
    def potential_function_rep(pos_ee):
        return u_rep_function(pos_ee, rho_0, k)
    
    # Calculate the gradient with respect to rho_b
    grad_function = grad(potential_function_rep)

    # Compute the gradient with the given rho_b
    v_rep = grad_function(pos_ee)
    return -v_rep


def V_rep(v_rep):
    """ Repulsive Velocity in Cartesian Space with angular velocity added

    Args:
        v_rep (float[]): Repulsive Velocity in Cartesian Space, is a Scalar TODO input output in comment passt nicht zusammen

    Returns:
        float[]: Repulsive Velocity in Cartesian Space, is a 3x1 Vector, with added Angular Velocities omega_rep
    """
    return np.array([v_rep[0], v_rep[1]]).T

def joint_velocities_att(inverse_jacobian_matrix, v_att) :
    """Calculates the Joint Velocities from Cartesian Space to Joint Space for the Attractive Velocity

    Args:
        inverse_jacobian_matrix (float[][]): Inverse Jacobian Matrix of current state of the robotic arm
        v_att (float[]): Attraction Velocity in Cartesian Space

    Returns:
        float[] : Attraction Velocity in Joint Space
    """
    v_att_vec = V_att(v_att)
    return np.dot(inverse_jacobian_matrix, v_att_vec)

def joint_velocities_rep(inverse_jacobian_matrix, v_rep) :
    """ Calculates the Joint Velocities from Cartesian Space to Joint Space for the Repulsive Velocity.

    Args:
        inverse_jacobian_matrix (float[][]): Inverse Jacobian Matrix of current state of the robotic arm
        v_rep (float[]): Repulsive Velocity in Cartesian Space

    Returns:
        float[] : Repulsive Velocity in Joint Space
    """
    return np.dot(inverse_jacobian_matrix, V_rep(v_rep))

