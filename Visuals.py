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

plt.ion()  # Activates interactive mode
fig2, ax2 = plt.subplots()
x_data_time = []
y_data_distance_to_target = []
line2, = ax2.plot([], [], 'r-', label="Distance")

ax2.set_xlim(0, config.timeout)  # x-Axis 0 to maximum time till abortion
ax2.set_ylim(-2, 30)  # y-Axis (Distance) -2 to 30
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Distance')
ax2.legend()

# Initializes the figure
def init():
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle(center, radius, fc='y')
    return line, point, obstacle_circle

start_time = time.time()

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

    # After a given time, the execution will be aborted
    current_time = time.time()
    if(current_time - start_time > config.timeout) :
        print(f"TIMEOUT")
        ani.event_source.stop()
        plt.close()
        return line, point, #obstacle_circle

    # Calculate distance arm to obstacle. If negative, error and abort execution
    distance = arm.distance_arm_obstacle(center, radius)
    if(distance < config.min_distance_to_obstacle):
        #print(f"ERROR: Arm touches the obstacle!")
        ani.event_source.stop()
        plt.close()
        return line, point, #obstacle_circle

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
        plt.close()
        return line, point, #obstacle_circle

    # Calculates Joint Velocities for U_rep
    v_rep_joint = pf.v_rep_function(distance, rho_0, k)
    joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)

    if(arm.end_effector[1] < 0):
        joint_velocity = joint_velocity_att - joint_velocity_rep + [1E-10,1E-10,1E-10]
    else:
        joint_velocity = joint_velocity_att + joint_velocity_rep + [1E-10,1E-10,1E-10]
    #joint_velocity =  # Very little amount so arm doesn't get stuck in start position
    #joint_velocity =  joint_velocity + joint_velocity_att + joint_velocity_rep

    # Hard maximum velocity for robot arm
    if(np.abs(joint_velocity[0])>max_velocity):
        joint_velocity[0] = np.sign(joint_velocity[0]) * max_velocity
    if(np.abs(joint_velocity[1])>max_velocity):
        joint_velocity[1] = np.sign(joint_velocity[1]) *max_velocity
    if(np.abs(joint_velocity[2])>max_velocity):
        joint_velocity[2] = np.sign(joint_velocity[2]) *max_velocity
    #print(f"joint_velocity={joint_velocity}, jv_att={joint_velocity_att}, jv_rep={joint_velocity_rep}")

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
    distance_to_target = pf.cartesian_distance(arm.end_effector, (target_x, target_y))
    if (distance_to_target) < delta_success_distance :
        print("SUCCESS: Target reached!")
        ani.event_source.stop()
        plt.close()

    # Checks if the other links touch the Obstacle
    distance =  distance_to_circle(center, radius, arm.joint_coxa)
    if(distance == 0):
        print(f"ERROR: Coxa-Link touches the obstacle!")
        ani.event_source.stop()
        plt.close()
        return line, point, obstacle_circle
    distance = distance_to_circle(center, radius, arm.joint_femur)
    if(distance == 0):
        print(f"ERROR: Femur-Link touches the obstacle!")
        ani.event_source.stop()
        plt.close()
        return line, point, obstacle_circle
    #ani.event_source.stop() # If you want to take a closer look to the start-position

    # Füge die neuen Werte zu den Daten hinzu
    x_data_time.append(current_time - start_time)
    y_data_distance_to_target.append(distance_to_target)
    
    # Aktualisiere den Plot
    line2.set_xdata(x_data_time)
    line2.set_ydata(y_data_distance_to_target)
    print(f"Time:{current_time - start_time}, Distance:{distance_to_target}")
    
    # Aktualisiere das Diagramm
    #fig2.canvas.draw()
    #fig2.canvas.flush_events()
    return line, point, obstacle_circle

arm = RoboterArm.RoboticArm(coxa_length,femur_length,tibia_length)
arm.update_joints(theta_coxa, theta_femur, theta_tibia)
# Start the animation
frames = np.linspace(0, 2 * np.pi, delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init) # blit=True
plt.ioff()
plt.show()
