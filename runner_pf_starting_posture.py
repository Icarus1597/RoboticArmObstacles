import numpy as np
import robotic_arm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import config
import autograd.numpy as anp
import potential_fields as pf
import switch_mode as sm
import geometry

PI = np.pi

# Update the posture of the arm
arm = robotic_arm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
arm.update_joints(config.theta_coxa, config.theta_femur, config.theta_tibia)

start_time = time.time() # To track the duration of the test 
covered_distance = 0 # To measure the path length
previous_end_effector_position = arm.end_effector
mode_start_position = True
time_end_algorithm = -1
time_start_algorithm = -1

# Plot: Robotic arm
fig, ax = plt.subplots()
ax.set_aspect('equal')
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

def calculate_starting_position(alpha_offset):
    """Calculate, based on the target and obstacle position, the desired starting position for the robotic arm

    Args:
        alpha_offset (float): desired offset for the coxa link (PI/2 -> 90° to Obstacle)

    Returns:
        theta_coxa, theta_femur, theta_tibia: target angles for the starting position
    """
    side = geometry.side_point_to_line2((config.target_x, config.target_y), (0, 0), config.center)
    alpha = geometry.angle_vector_point((0,0), (1,0), config.center)
    #print(f"side = {side}, alpha = {alpha}")
    theta_coxa = (alpha + side*alpha_offset) % (2*PI)
    theta_femur = PI/4 * side % (2*PI)
    theta_tibia = PI/4 * side % (2*PI)
    #print(f"side = {side}, alpha = {alpha}, coxa, femur, tibia = {theta_coxa}, {theta_femur}, {theta_tibia}")
    return theta_coxa, theta_femur, theta_tibia

def init():
    """Initializes the figure with the robotic arm, target point and one obstacle in shape of a circle.

    Returns:
        _type_: shapes to be displayed in the plot
    """
    line.set_data([], [])
    point.set_data([], [])
    obstacle_circle = plt.Circle(config.center, config.radius, fc='y')
    #mode_start_position = True
    return line, point, obstacle_circle

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
    global mode_start_position
    global time_end_algorithm
    global time_start_algorithm

    # After a given time, the execution will be aborted
    current_time = time.time()
    ax2.set_xlim(0, current_time - start_time)  # x-Axis 0 to current_time
    if(current_time - start_time > config.timeout) :
        print(f"TIMEOUT")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: TIMEOUT\n")
        config.pf_sp_number_timeout += 1
        ani.event_source.stop()
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point,

    current_time = time.time()
    # Calculate distance arm to obstacle. If negative, error and abort execution
    distance = arm.distance_arm_obstacle(config.center, config.radius)
    if(distance < 0):
        ani.event_source.stop()
        if(distance == -1):
            config.pf_sp_number_error_coxa +=1
        elif(distance == -2):
            config.pf_sp_number_error_femur +=1
        elif(distance == -3):
            config.pf_sp_number_error_tibia +=1
        else:
            config.pf_sp_number_error_ee +=1
        plt.figure(fig.number)
        plt.close()
        plt.figure(figure_distance_to_target.number)
        plt.close()
        return line, point, #obstacle_circle

    if(mode_start_position):
        target_angles = calculate_starting_position(alpha_offset=PI*5/4)
        if(not sm.arm_near_target_angles(arm, target_angles)):
            target_position = (config.coxa_length * np.cos(target_angles[0]), config.coxa_length * np.sin(target_angles[0]))
            arm.move_to_target_direction(target_angles, target_position)
        else:
            mode_start_position = False
            with open("testresults.txt", "a") as file:
                file.write(f"Successfully Reached starting posture\n")

    else: 
        # PF method
        # Calculations for the movement of joints: Attractive Velocity
        v_att_joint = pf.v_att_function(arm.joint_tibia, anp.array([config.target_x, config.target_y], dtype=anp.float64), config.zeta)
        jacobian_matrix = arm.jacobian_matrix()
        inverse_jacobian_matrix = arm.inverse_jacobian_matrix(jacobian_matrix)
        joint_velocity_att = pf.joint_velocities_att(inverse_jacobian_matrix, v_att_joint)

        # Calculates Joint Velocities for U_rep
        v_rep_joint = pf.v_rep_function(arm.end_effector, config.rho_0, config.k)
        joint_velocity_rep = pf.joint_velocities_rep(inverse_jacobian_matrix, v_rep_joint)

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
    distance_to_target = geometry.cartesian_distance(arm.end_effector, (config.target_x, config.target_y))
    if (distance_to_target) < config.delta_success_distance :
        print("SUCCESS: Target reached!")
        with open("testresults.txt", "a") as file:
            file.write(f"Test Result: SUCCESS, duration={time.time() - start_time}, calculation_time = {time_end_algorithm - time_start_algorithm}, covered distance = {covered_distance}\n")
        config.pf_sp_number_success += 1
        config.pf_sp_list_covered_distance.append(covered_distance)
        config.pf_sp_time_needed.append(time.time() - start_time)
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