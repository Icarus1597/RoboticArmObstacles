import numpy as np
import robotic_arm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import config
import a_star_algorithm
import switch_mode as sm
import geometry
import potential_fields as pf

PI = np.pi

# Update the posture of the arm
arm = robotic_arm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
arm.update_joints(config.theta_coxa, config.theta_femur, config.theta_tibia)

start_time = time.time() # To track the duration of the test 
covered_distance = 0 # To measure the path length
previous_end_effector_position = arm.end_effector
time_end_algorithm = -1
time_start_algorithm = -1

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

ax2.set_xlim(0, config.timeout)  # x-Axis 0 to maximum time till abortion
ax2.set_ylim(-2, 30)  # y-Axis (Distance) -2 to 30
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Distance')
ax2.legend()

alpha = geometry.angle_vector_point((0,0), (5, 0), config.center)
alpha = (alpha + np.pi) % (2*np.pi)
print(f"alpha = {alpha}")

if plt.get_backend() == 'TkAgg':
    # Set the position of fig
    fig.canvas.manager.window.geometry("+1000+100")
    
    # Set position of figure_distance_to_target
    figure_distance_to_target.canvas.manager.window.geometry("+1000+100")

def init():
    """Initializes the figure with the robotic arm, target point and one obstacle in shape of a circle.

    Returns:
        _type_: shapes to be displayed in the plot
    """
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle(config.center, config.radius, fc='y')
    return line, point, obstacle_circle

next_node_index = 0
path_node_list = []

# A* algorithm
initial_point = a_star_algorithm.AStarNode(arm.end_effector, (config.target_x, config.target_y))
time_start_algorithm = time.time()
path_node_list = initial_point.iterative_search_wrapper()

time_end_algorithm = time.time()
config.astar_tang_time_needed_calculation.append(time_end_algorithm - time_start_algorithm)

# Updates the frame
def update(frame):
    """ Updates the frame. Calculates the new thetas based on A* algorithm for the Robotic Arm and updates its position.

    Args:
        frame (_type_): _description_

    Returns:
        _type_: shapes to be displayed in the plot
    """
    global previous_end_effector_position
    global covered_distance
    global next_node_index
    global path_node_list
    global time_end_algorithm
    global time_start_algorithm

    # After a given time, the execution will be aborted
    current_time = time.time()
    if(current_time - start_time > config.timeout) :
        print(f"TIMEOUT")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: TIMEOUT\n")
        config.astar_tang_number_timeout += 1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle

    if(path_node_list == -1):
        print(f"Error: No path to target found")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: Error. No path to target found\n")
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle

    current_time = time.time()
    ax2.set_xlim(0, current_time - start_time)  # x-Axis 0 to current_time
    # Calculate distance arm to obstacle. If negative, error and abort execution
    distance = arm.distance_arm_obstacle(config.center, config.radius)
    if(distance < 0):
        ani.event_source.stop()
        if(distance == -1):
            config.astar_tang_number_error_coxa +=1
        elif(distance == -2):
            config.astar_tang_number_error_femur +=1
        elif(distance == -3):
            config.astar_tang_number_error_tibia +=1
        else:
            config.astar_tang_number_error_ee +=1
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle

    # Calculate distance to Circle and checks if the End Effector touches the Circle
    distance = geometry.distance_to_circle(config.center, config.radius, arm.end_effector)
    distance_coxa = geometry.distance_segment_point(config.center[0], config.center[1], 0, 0, arm.joint_coxa_x, arm.joint_coxa_y) - config.radius
    distance_femur = geometry.distance_segment_point(config.center[0], config.center[1], arm.joint_coxa_x, arm.joint_coxa_y, arm.joint_femur_x, arm.joint_femur_y) - config.radius

    distance_coxa_link = geometry.distance_to_circle(config.center, config.radius, (0,0))
    distance_to_obstacle = min(config.min_distance_to_obstacle, distance_coxa_link)    
    if(distance_femur < config.min_distance_to_obstacle or distance_coxa < distance_to_obstacle):
        #print(f"AStarTang: PF mode")
        # Calculates Coxa-Joint Velocities for U_rep
        #distance_coxa = Geometrie.distance_to_circle(config.center, config.radius, arm.joint_coxa)
    
        v_rep_joint_coxa = pf.v_rep_function(arm.joint_coxa, config.rho_0_coxa, config.k_coxa)
        jacobian_matrix_coxa = arm.jacobian_matrix_coxa()
        inverse_jacobian_matrix_coxa = arm.inverse_jacobian_matrix(jacobian_matrix_coxa)
        joint_velocity_rep_coxa = pf.joint_velocities_rep(inverse_jacobian_matrix_coxa, v_rep_joint_coxa)

        # Calculates Femur-Joint Velocities for U_rep
        #distance_femur = Geometrie.distance_to_circle(config.center, config.radius, arm.joint_femur)

        v_rep_joint_femur = pf.v_rep_function(arm.joint_femur, config.rho_0_femur, config.k_femur)
        jacobian_matrix_femur = arm.jacobian_matrix_femur()
        inverse_jacobian_matrix_femur = arm.inverse_jacobian_matrix(jacobian_matrix_femur)
        joint_velocity_rep_femur = pf.joint_velocities_rep(inverse_jacobian_matrix_femur, v_rep_joint_femur)
        
        joint_velocity = [joint_velocity_rep_coxa[0] + joint_velocity_rep_femur[0], joint_velocity_rep_femur[1]]

        # Hard maximum velocity for robot arm
        if(np.abs(joint_velocity[0])>config.max_velocity):
            joint_velocity[0] = np.sign(joint_velocity[0]) * config.max_velocity
        if(np.abs(joint_velocity[1])>config.max_velocity):
            joint_velocity[1] = np.sign(joint_velocity[1]) * config.max_velocity
        #if(np.abs(joint_velocity[2])>config.max_velocity):
        #    joint_velocity[2] = np.sign(joint_velocity[2]) * config.max_velocity

        # Calculate the new thetas
        theta_coxa = arm.theta_coxa + config.delta_t * joint_velocity[0] * config.damping_factor
        theta_femur = arm.theta_femur + config.delta_t * joint_velocity[1] * config.damping_factor
        #theta_tibia = arm.theta_tibia + config.delta_t * joint_velocity[2] * config.damping_factor*2
        arm.update_joints(theta_coxa, theta_femur, arm.theta_tibia)
          
    #else: # mode A*
    # Punkte nacheinander abfahren path node list
    #print(f"path_node_list length = {len(path_node_list)}")
    if(path_node_list != -1):
        theta_coxa, theta_femur, theta_tibia= arm.inverse_kinematics(path_node_list[next_node_index].position)
        arm.update_joints(theta_coxa+1E-5, theta_femur, theta_tibia)
    else:
        print(f"Error: path_node_list empty/None")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: Error. Arm in start position too close to obstacle\n")
        config.astar_tang_number_error_no_path +=1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle


    if(np.linalg.norm(arm.error_target_end_effector(path_node_list[next_node_index].position))<config.tolerance) :
        if(len(path_node_list) > next_node_index+1):
            next_node_index += 1

    # Actualize data for the next frame
    line.set_data([0, arm.joint_coxa_x, arm.joint_femur_x, arm.joint_tibia_x], [0, arm.joint_coxa_y, arm.joint_femur_y, arm.joint_tibia_y])
    point.set_data([config.target_x], [config.target_y])  # Update the position of the target point
    obstacle_circle = plt.Circle(config.center, config.radius, fc='y')
    plt.figure(fig.number)
    plt.gca().add_patch(obstacle_circle)
    

    # Stops, when target reached/ close to target
    distance_to_target = geometry.cartesian_distance(arm.end_effector, (config.target_x, config.target_y))
    if (distance_to_target) < config.delta_success_distance :
        print("SUCCESS: Target reached!")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: SUCCESS, duration={time.time() - start_time}, calculation_time = {time_end_algorithm - time_start_algorithm}, covered distance = {covered_distance}\n")
        config.astar_tang_number_success += 1
        config.astar_tang_list_covered_distance.append(covered_distance)
        config.astar_tang_time_needed.append(time.time() - start_time)
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()

    # Append the new data
    x_data_time.append(current_time - start_time)
    y_data_distance_to_target.append(distance_to_target)
    
    # Actualize the figure
    line_distance_to_target.set_xdata(x_data_time)
    line_distance_to_target.set_ydata(y_data_distance_to_target)
    figure_distance_to_target.canvas.draw()

    # Track covered distance
    step_covered_distance = geometry.cartesian_distance(previous_end_effector_position, arm.end_effector)
    covered_distance += step_covered_distance
    previous_end_effector_position = arm.end_effector

    return line, point, obstacle_circle

# Start the animation
frames = np.linspace(0, 2 * np.pi, config.delta_t)
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)
plt.ioff()
plt.show()