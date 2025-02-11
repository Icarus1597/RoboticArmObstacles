import numpy as np
import RoboterArm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import PotentialFields as pf
import time
import autograd.numpy as anp
import config
import AStarAlgorithm
import Obstacles
import SwitchMode as sm

# Update the posture of the arm
arm = RoboterArm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
arm.update_joints(config.theta_coxa, config.theta_femur, config.theta_tibia)

start_time = time.time() # To track the duration of the test 
covered_distance = 0 # To measure the path length
previous_end_effector_position = arm.end_effector

# Plot: Robotic arm
fig, ax = plt.subplots()
ax.set_aspect('equal') #TODO ?
# Set axis limits considering the link lengths
arm_length = config.coxa_length + config.femur_length + config.tibia_length
ax.set_xlim(-arm_length,  arm_length)
ax.set_ylim(-arm_length,  arm_length)
line, = ax.plot([], [], 'o-', lw=2)
point, = ax.plot([], [], 'ro', markersize=8)

# Plot: Distance End Effector to target
plt.ion()  # Activates interactive mode
figure_distance_to_target, ax2 = plt.subplots()
x_data_time = []
y_data_distance_to_target = []
line_distance_to_target, = ax2.plot([], [], 'r-', label="Distance")

# Plot: Searched Points of the A-Star Algorithm
search_points_plot, ax_search_points = plt.subplots()
plt.figure(search_points_plot.number) # To make sure, the correct plot is the active one
ax_search_points.set_aspect('equal')
# Set axis limits considering the link lengths

ax_search_points.set_xlim(-arm_length,  arm_length)
ax_search_points.set_ylim(-arm_length,  arm_length)

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

# A-Star Algorithm
initial_point = AStarAlgorithm.AStarNode(arm.end_effector, (config.target_x, config.target_y))
time_start_algorithm = time.time()
path_node_list = initial_point.iterative_search_wrapper(search_points_plot)
time_end_algorithm = time.time()
config.list_time_needed_for_calculation.append(time_end_algorithm - time_start_algorithm)


next_node_index = 0

# Updates the frame
def update(frame):
    global previous_end_effector_position
    global covered_distance
    global next_node_index
    
    current_time = time.time()
    # Calculate distance arm to obstacle. If negative, error and abort execution
    distance = arm.distance_arm_obstacle(config.center, config.radius)
    if(distance < config.min_distance_to_obstacle):
        #print(f"ERROR: Arm touches the obstacle!")
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        plt.figure(search_points_plot.number)
        plt.close()
        return line, point, #obstacle_circle

    # Calculate distance to Circle and checks if the End Effector touches the Circle
    distance = Obstacles.distance_to_circle(config.center, config.radius, arm.end_effector)

    # Punkte nacheinander abfahren path node list

    # TODO calculate new thetas here
    current_mode = sm.choose_mode(arm)
    print(f"Current Mode = {current_mode}")
    if (current_mode == 0):
        #arm.inverse_kinematics((config.target_x, config.target_y))
        arm.inverse_kinematics(path_node_list[next_node_index].position)
    if (current_mode == 1):
        arm.inverse_kinematics_with_knee(arm.joint_tibia, config.goal_femur_angle)
    if (current_mode == 2):
        arm.inverse_kinematics_with_tibia(arm.joint_tibia, config.goal_tibia_angle)
    
    #arm.inverse_kinematics(path_node_list[next_node_index].position)
    #print(f"End-Effector Position:{arm.end_effector}, Next Path Node:{path_node_list[next_node_index].position}")
   

    if(np.linalg.norm(arm.error_target_end_effector(path_node_list[next_node_index].position))<config.tolerance) :
        if(len(path_node_list) > next_node_index+1):
            next_node_index += 1
        else:
            print(f"End of path node list reached")

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
            file.write(f"Test Result: SUCCESS, duration={time.time() - start_time}, calculation_time = {time_end_algorithm - time_start_algorithm}, covered distance = {covered_distance}\n")
        config.number_success += 1
        config.list_covered_distance.append(covered_distance)
        config.list_time_needed.append(time.time() - start_time)
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        plt.figure(search_points_plot.number)
        plt.close()

    # Append the new data
    x_data_time.append(current_time - start_time)
    y_data_distance_to_target.append(distance_to_target)
    
    # Actualize the figure
    line_distance_to_target.set_xdata(x_data_time)
    line_distance_to_target.set_ydata(y_data_distance_to_target)
    figure_distance_to_target.canvas.draw()

    # Track covered distance
    step_covered_distance = pf.cartesian_distance(previous_end_effector_position, arm.end_effector)
    covered_distance += step_covered_distance
    previous_end_effector_position = arm.end_effector

    return line, point, obstacle_circle

# Start the animation
frames = np.linspace(0, 2 * np.pi, config.delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.ioff()
plt.show()