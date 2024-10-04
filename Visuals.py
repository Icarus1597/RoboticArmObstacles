import numpy as np
import RoboterArm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PotentialFields as pf
import time
import autograd.numpy as anp
from shapely.geometry import Point, Polygon
from matplotlib.patches import Polygon as mpl_polygon
import config

# Parameters
target_x, target_y = config.target_x, config.target_y  # Coordinates of the target point
delta_t = config.delta_t
center = config.center
radius = config.radius
max_velocity = config.max_velocity
zeta = config.zeta
rho_0 = config.rho_0
k = config.k
damping_factor = config.damping_factor
delta_success_distance = config.delta_success_distance
theta_coxa = config.theta_coxa
theta_femur = config.theta_femur
theta_tibia = config.theta_tibia
coxa_length = config.coxa_length
femur_length = config.femur_length
tibia_length = config.tibia_length

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-(coxa_length+femur_length+tibia_length),  coxa_length+femur_length+tibia_length)
ax.set_ylim(-(coxa_length+femur_length+tibia_length),  coxa_length+femur_length+tibia_length)
line, = ax.plot([], [], 'o-', lw=2)
point, = ax.plot([], [], 'ro', markersize=8)

# Initializes the figure
def init():
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle(center, radius, fc='y')
    return line, point, obstacle_circle

# Method to calculate the distance between a circle and a point. TODO: Maybe put this in another Script
# Input:
#   center:   center point of the circle
#   point:    point for which the distance shall be calculated
#   radius:   radius of the circle
# Ouput:
#   distance: distance between the point and the border of the circle
def distance_to_circle(center, radius, point):
    distance = pf.cartesian_distance(center, point) - radius
    if(distance < 0) : 
        distance = 0
    return distance

# Updates the frame
def update(frame):

    # Calculations for the movement of joints: Attractive Velocity
    v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([target_x, target_y], dtype=anp.float64), zeta)
    jacobian_matrix = arm.jacobian_matrix()
    inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
    joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

    # Calculate distance to Circle and checks if the End Effector touches the Circle
    distance = distance_to_circle(center, radius, arm.end_effector)
    if(distance == 0):
        print(f"ERROR: End-Effector touches the obstacle!")
        ani.event_source.stop()
        return line, point, #obstacle_circle

    # Calculates Joint Velocities for U_rep
    v_rep_joint = pf.v_rep_function(distance, rho_0, k)
    joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)

    joint_velocity = joint_velocity_att - joint_velocity_rep

    # Hard maximum velocity for robot arm
    if(np.abs(joint_velocity[0])>max_velocity):
        joint_velocity[0] = np.sign(joint_velocity[0]) * max_velocity
    if(np.abs(joint_velocity[1])>max_velocity):
        joint_velocity[1] = np.sign(joint_velocity[1]) *max_velocity
    if(np.abs(joint_velocity[2])>max_velocity):
        joint_velocity[2] = np.sign(joint_velocity[2]) *max_velocity
    print(f"joint_velocity={joint_velocity}, jv_att={joint_velocity_att}, jv_rep={joint_velocity_rep}")

    # Calculate the new thetas
    theta_coxa = arm.theta_coxa + delta_t * joint_velocity[0] * damping_factor
    theta_femur = arm.theta_femur + delta_t * joint_velocity[1] * damping_factor
    theta_tibia = arm.theta_tibia + delta_t * joint_velocity[2] * damping_factor
    arm.update_joints(theta_coxa, theta_femur, theta_tibia)

    # Actualize data for the next frame
    line.set_data([0, arm.joint_coxa_x, arm.joint_femur_x, arm.joint_tibia_x], [0, arm.joint_coxa_y, arm.joint_femur_y, arm.joint_tibia_y])
    point.set_data([target_x], [target_y])  # Update the position of the additional point
    obstacle_circle = plt.Circle(center, radius, fc='y')
    plt.gca().add_patch(obstacle_circle)

    # Stops, when target reached/ close to target
    if (pf.cartesian_distance(arm.end_effector, (target_x, target_y))) < delta_success_distance :
        print("SUCCESS: Target reached!")
        ani.event_source.stop()

    # Checks if the other links touch the Obstacle
    distance =  distance_to_circle(center, radius, arm.joint_coxa)
    if(distance == 0):
        print(f"ERROR: Coxa-Link touches the obstacle!")
        #ani.event_source.stop()
        return line, point, obstacle_circle
    distance = distance_to_circle(center, radius, arm.joint_femur)
    if(distance == 0):
        print(f"ERROR: Femur-Link touches the obstacle!")
        #ani.event_source.stop()
        return line, point, obstacle_circle
            
    return line, point, obstacle_circle

arm = RoboterArm.RoboticArm(coxa_length,femur_length,tibia_length)
arm.update_joints(theta_coxa, theta_femur, theta_tibia)
# Start the animation
frames = np.linspace(0, 2 * np.pi, delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.show()
