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
points = [[3,4], [7.5,11],[3,8]]

# Initializes the figure
def init():
    line.set_data([], [])
    point.set_data([], [])
    #obstacle_circle = plt.Circle((0.5, 0.5), radius=0.5, fc='y')
    
    obstacle_polygon = plt.Polygon(points)
    #plt.gca().add_patch(circle)
    return line, point, obstacle_polygon

# Updates the frame
def update(frame):
    
    #arm.update_joints(arm.theta_coxa, arm.theta_femur, arm.theta_tibia)

    # Calculations for the movement of joints: Attractive Velocity
    #print(f"pos_ee/joint_tibia:{arm.joint_tibia}")
    v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([target_x, target_y], dtype=anp.float64), 1)
    jacobian_matrix = arm.jacobian_matrix()
    inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
    joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

    # Creates shapely Polygon to calculate the distance between End Effector and Polygon
    point_ee = Point(arm.end_effector)
    #points = [(3,4), (9,5), (7,8), (3,8), (3,4)]
    obstacle_polygon_shapely = Polygon(points)
    distance = point_ee.distance(obstacle_polygon_shapely)
    if(distance == 0):
        print(f"ERROR: End-Effector touches the obstacle!")
        ani.event_source.stop()
        return line, point, obstacle_polygon
    #print(f"Distance Point to Polygon: {distance}")

    # Calculates Joint Velocities for U_rep
    v_rep_joint = pf.v_rep_function(distance, 0.5, 2)
    joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)

    #print(f"joint_vel_att:{joint_velocity_att}, joint_vel_rep:{joint_velocity_rep}")
    joint_velocity = joint_velocity_att - joint_velocity_rep
    #print(f"Joint Velocity:{joint_velocity}")
    #x0, y0 = 0, 0

    delta_coxa, delta_femur, delta_tibia = joint_velocity
    #print(f"d_coxa:{delta_coxa}, d_femur:{delta_femur}, d_tibia:{delta_tibia}")
    daempfungsfaktor = 0.0001
    theta_coxa = arm.theta_coxa + delta_t * joint_velocity[0] * daempfungsfaktor
    theta_femur = arm.theta_femur + delta_t * joint_velocity[1] * daempfungsfaktor
    theta_tibia = arm.theta_tibia + delta_t * joint_velocity[2] * daempfungsfaktor
    arm.update_joints(theta_coxa, theta_femur, theta_tibia)

    # Debug-Ausgaben
    #print(f"Frame: {frame}, Coxa Joint: ({arm.joint_coxa_x}, {arm.joint_coxa_y}), Femur Joint: ({arm.joint_femur_x}, {arm.joint_femur_y}), Tibia Joint: ({arm.joint_tibia_x}, {arm.joint_tibia_x})")
    line.set_data([0, arm.joint_coxa_x, arm.joint_femur_x, arm.joint_tibia_x], [0, arm.joint_coxa_y, arm.joint_femur_y, arm.joint_tibia_y])
    #line.set_data([x0, x1, x2, x3], [y0, y1, y2, y3])
    point.set_data([target_x], [target_y])  # Update the position of the additional point
    #obstacle_circle = plt.Circle((0.5, 0.5), radius=0.5, fc='y')
    #plt.gca().add_patch(obstacle_circle)
    obstacle_polygon = plt.Polygon(points)    
    plt.gca().add_patch(obstacle_polygon)

    # Abbruchbedingung: target_point = point_ee
    if np.linalg.norm(np.array(arm.end_effector) - np.array([target_x, target_y])) < 0.1:
        print("Target reached!")
        ani.event_source.stop()

    # Checks if the other links touch the Polygon
    point_coxa = Point(arm.joint_coxa)
    point_femur = Point(arm.joint_femur)
    distance = point_coxa.distance(obstacle_polygon_shapely)
    if(distance == 0):
        print(f"ERROR: Coxa-Link touches the obstacle!")
        #ani.event_source.stop()
        #return line, point, obstacle_polygon
    distance = point_femur.distance(obstacle_polygon_shapely)
    if(distance == 0):
        print(f"ERROR: Femur-Link touches the obstacle!")
        #ani.event_source.stop()
        #return line, point, obstacle_polygon
            
    return line, point, obstacle_polygon

arm = RoboterArm.RoboticArm(7,6,4)
frames = np.linspace(0, 2 * np.pi, delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
#plt.axis('scaled')
plt.show()