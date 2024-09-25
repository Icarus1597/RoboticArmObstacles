import numpy as np
import RoboterArm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PotentialFields as pf
import time
import autograd.numpy as anp
from shapely.geometry import Point, Polygon
from matplotlib.patches import Polygon as mpl_polygon

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5,15)
ax.set_ylim(-5,15)
line, = ax.plot([], [], 'o-', lw=2)
point, = ax.plot([], [], 'ro', markersize=8)
target_x, target_y = 8, 8  # Coordinates of the target point
delta_t = 300
center = (4.5, 7.5)
radius = (2.5)

# Initializes the figure
def init():
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle(center, radius, fc='y')
    return line, point, obstacle_circle

def distance_to_circle(center, radius, point):
    distance = pf.cartesian_distance(center, point) - radius
    return distance

# Updates the frame
def update(frame):

    # Calculations for the movement of joints: Attractive Velocity
    v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([target_x, target_y], dtype=anp.float64), 1)
    jacobian_matrix = arm.jacobian_matrix()
    inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
    joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

    # Calculate distance to Circle
    distance = distance_to_circle(center, radius, arm.end_effector)
    if(distance <= 0):
        print(f"ERROR: End-Effector touches the obstacle!")
        ani.event_source.stop()
        return line, point, obstacle_circle

    # Calculates Joint Velocities for U_rep
    v_rep_joint = pf.v_rep_function(distance, 0.5, 2)
    joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)

    joint_velocity = joint_velocity_att - joint_velocity_rep

    daempfungsfaktor = 0.0001
    theta_coxa = arm.theta_coxa + delta_t * joint_velocity[0] * daempfungsfaktor
    theta_femur = arm.theta_femur + delta_t * joint_velocity[1] * daempfungsfaktor
    theta_tibia = arm.theta_tibia + delta_t * joint_velocity[2] * daempfungsfaktor
    arm.update_joints(theta_coxa, theta_femur, theta_tibia)

    line.set_data([0, arm.joint_coxa_x, arm.joint_femur_x, arm.joint_tibia_x], [0, arm.joint_coxa_y, arm.joint_femur_y, arm.joint_tibia_y])
    point.set_data([target_x], [target_y])  # Update the position of the additional point
    obstacle_circle = plt.Circle(center, radius, fc='y')
    plt.gca().add_patch(obstacle_circle)

    # Abbruchbedingung: target_point = point_ee
    if np.linalg.norm(np.array(arm.end_effector) - np.array([target_x, target_y])) < 0.1:
        print("Target reached!")
        ani.event_source.stop()

    # Checks if the other links touch the Polygon
    point_coxa = Point(arm.joint_coxa)
    point_femur = Point(arm.joint_femur)
    distance =  distance_to_circle(center, radius, arm.joint_coxa)
    if(distance <= 0):
        print(f"ERROR: Coxa-Link touches the obstacle!")
        ani.event_source.stop()
        return line, point, obstacle_circle
    distance = distance_to_circle(center, radius, arm.joint_femur)
    if(distance <= 0):
        print(f"ERROR: Femur-Link touches the obstacle!")
        ani.event_source.stop()
        return line, point, obstacle_circle
            
    return line, point, obstacle_circle

arm = RoboterArm.RoboticArm(7,6,4)
frames = np.linspace(0, 2 * np.pi, delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
#plt.axis('scaled')
plt.show()