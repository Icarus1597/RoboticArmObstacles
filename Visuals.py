import numpy as np
import RoboterArm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PotentialFields as pf
import time
import autograd.numpy as anp
from shapely.geometry import Point, Polygon
#from matplotlib.patches import Polygon as mpl_polygon

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
line, = ax.plot([], [], 'o-', lw=2)
point, = ax.plot([], [], 'ro', markersize=8)

# Initializes the figure
def init():
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle((0.5, 0.5), radius=0.5, fc='y')
    points = [[1,1], [2, 3], [3,2], [3,5], [1,4]]
    obstacle_polygon = plt.Polygon(points)
    #plt.gca().add_patch(circle)
    return line, point, obstacle_circle, obstacle_polygon

# Updates the frame
def update(frame):
    # Define the coordinates of the target point
    target_x, target_y = 1, 1  # Coordinates of the target point
    arm.update_joints(arm.theta_coxa, arm.theta_femur, arm.theta_tibia)

    # Calculations for the movement of joints
    #U_att_joint = pf.U_att_function(arm.joint3, np.array([target_x, target_y]), 1.1)
    v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([target_x, target_y], dtype=anp.float64), 1.1)
    jacobian_matrix = arm.jacobian_matrix(arm.length_coxa,      arm.length_femur,      arm.length_tibia, 
                                          arm.get_theta_coxa(), arm.get_theta_femur(), arm.get_theta_tibia())
    inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
    joint_velocity = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)
    #print("Joint Velocity:")
    #print(joint_velocity)
    x0, y0 = 0, 0
    #x1, y1 = arm.joint_coxa
    #x2, y2 = arm.joint_femur
    #x3, y3 = arm.joint_tibia
    x1 = joint_velocity[0][1]
    y1 = joint_velocity[0][2]
    x2 = joint_velocity[1][1]
    y2 = joint_velocity[1][2]
    x3 = joint_velocity[2][1]
    y3 = joint_velocity[2][2]
    

    # Debug-Ausgaben
    #print(f"Frame: {frame}, Coxa Joint: ({x1}, {y1}), Femur Joint: ({x2}, {y2}), Tibia Joint: ({x3}, {y3})")
    
    line.set_data([x0, x1, x2, x3], [y0, y1, y2, y3])
    point.set_data(target_x, target_y)  # Update the position of the additional point
    obstacle_circle = plt.Circle((0.5, 0.5), radius=0.5, fc='y')
    plt.gca().add_patch(obstacle_circle)
    points = [(1,1), (2, 3), (3,2), (3,5), (1,4)]
    obstacle_polygon = plt.Polygon(points)

    # Creates shapely Polygon to calculate the distance between End Effector and Polygon
    point_ee = Point(x3, y3)
    obstacle_polygon_shapely = Polygon(points)
    distance = point_ee.distance(obstacle_polygon_shapely)
    print(f"Distance Point to Polygon: {distance}")

    plt.gca().add_patch(obstacle_polygon)
    return line, point, obstacle_circle, obstacle_polygon

arm = RoboterArm.RoboticArm(1.5, 1.0, 0.5)
frames = np.linspace(0, 2 * np.pi, 300)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
#plt.axis('scaled')
plt.show()