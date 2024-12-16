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
import AStarAlgorithm

# Update the posture of the arm
arm = RoboterArm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
arm.update_joints(config.theta_coxa, config.theta_femur, config.theta_tibia)

start_time = time.time() # To track the duration of the test 
covered_distance = 0 # To measure the path length
previous_end_effector_position = arm.end_effector

# Plot: Robotic arm
fig, ax = plt.subplots()
ax.set_aspect('equal')
# Set axis limits considering the link lengths
ax.set_xlim(-(config.coxa_length +config.femur_length + config.tibia_length),  config.coxa_length + config.femur_length + config.tibia_length)
ax.set_ylim(-(config.coxa_length + config.femur_length + config.tibia_length),  config.coxa_length + config.femur_length + config.tibia_length)
line, = ax.plot([], [], 'o-', lw=2)
point, = ax.plot([], [], 'ro', markersize=8)

# Plot: Distance End Effector to target
plt.ion()  # Activates interactive mode
figure_distance_to_target, ax2 = plt.subplots()
x_data_time = []
y_data_distance_to_target = []
line_distance_to_target, = ax2.plot([], [], 'r-', label="Distance")

ax2.set_xlim(0, config.timeout)  # x-Axis 0 to maximum time till abortion
ax2.set_ylim(-2, 30)  # y-Axis (Distance) -2 to 30
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Distance')
ax2.legend()

if plt.get_backend() == 'TkAgg':
    # Set the position of fig
    fig.canvas.manager.window.geometry("+1000+100")
    
    # Set position of figure_distance_to_target
    figure_distance_to_target.canvas.manager.window.geometry("+1000+100")

# Initializes the figure
def init():
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle(config.center, config.radius, fc='y')
    return line, point, obstacle_circle

# Method to calculate the distance between a circle and a point
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
    global previous_end_effector_position
    global covered_distance

    # After a given time, the execution will be aborted
    current_time = time.time()
    if(current_time - start_time > config.timeout) :
        print(f"TIMEOUT")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: TIMEOUT\n")
        config.number_timeout += 1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle

    # Calculate distance arm to obstacle. If negative, error and abort execution
    distance = arm.distance_arm_obstacle(config.center, config.radius)
    if(distance < config.min_distance_to_obstacle):
        #print(f"ERROR: Arm touches the obstacle!")
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle

    # A-Star Algorithm
    path_node_list = AStarAlgorithm.iterative_search_wrapper(arm, (config.target_x, config.target_y))


    # Calculations for the movement of joints: Attractive Velocity
    v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([config.target_x, config.target_y], dtype=anp.float64), config.zeta)
    jacobian_matrix = arm.jacobian_matrix()
    inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
    joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

   
    # Calculate distance to Circle and checks if the End Effector touches the Circle
    distance = distance_to_circle(config.center, config.radius, arm.end_effector)
    '''
    if(distance == 0):
        print(f"ERROR: End-Effector touches the obstacle!")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: ERROR: EE touches the obstacle\n")
        config.number_error_ee +=1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle
    '''
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
    arm.update_joints(theta_coxa, theta_femur, theta_tibia)

    # Actualize data for the next frame
    line.set_data([0, arm.joint_coxa_x, arm.joint_femur_x, arm.joint_tibia_x], [0, arm.joint_coxa_y, arm.joint_femur_y, arm.joint_tibia_y])
    point.set_data([config.target_x], [config.target_y])  # Update the position of the target point
    obstacle_circle = plt.Circle(config.center, config.radius, fc='y')
    plt.figure(fig.number)
    plt.gca().add_patch(obstacle_circle)

    # Stops, when target reached/ close to target
    distance_to_target = pf.cartesian_distance(arm.end_effector, (config.target_x, config.target_y))
    if (distance_to_target) < config.delta_success_distance :
        print("SUCCESS: Target reached!")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: SUCCESS, duration={time.time() - start_time}, covered distance = {covered_distance}\n")
        config.number_success += 1
        config.list_covered_distance.append(covered_distance)
        config.list_time_needed.append(time.time() - start_time)
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
    '''
    # Checks if the other links touch the Obstacle
    # Coxa
    distance =  distance_to_circle(config.center, config.radius, arm.joint_coxa)
    if(distance == 0):
        print(f"ERROR: Coxa-Link touches the obstacle!")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: ERROR: Coxa-Link touches the obstacle!\n")
        config.number_error_coxa += 1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()        
        return line, point, obstacle_circle
    
    # Femur
    distance = distance_to_circle(config.center, config.radius, arm.joint_femur)
    if(distance == 0):
        print(f"ERROR: Femur-Link touches the obstacle!")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: ERROR: Femur-Link touches the obstacle!\n")
        config.number_error_femur += 1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, obstacle_circle
    #ani.event_source.stop() # If you want to take a closer look to the start-position
    '''
    # Append the new data
    x_data_time.append(current_time - start_time)
    y_data_distance_to_target.append(distance_to_target)
    
    # Actualize the figure
    line_distance_to_target.set_xdata(x_data_time)
    line_distance_to_target.set_ydata(y_data_distance_to_target)
    figure_distance_to_target.canvas.draw()

    step_covered_distance = pf.cartesian_distance(previous_end_effector_position, arm.end_effector)
    covered_distance += step_covered_distance
    previous_end_effector_position = arm.end_effector

    return line, point, obstacle_circle

# Start the animation
frames = np.linspace(0, 2 * np.pi, config.delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.ioff()
plt.show()