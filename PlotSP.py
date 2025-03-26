import numpy as np
import RoboterArm
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import config
import SwitchMode as sm
import Geometrie

PI = np.pi

alpha_offset = PI*3/2
beta_offset = PI
gamma_offset = beta_offset

def calculate_theta_coxa():
    side = Geometrie.side_point_to_line2((config.target_x, config.target_y), (0, 0), config.center)
    alpha = Geometrie.angle_vector_point((0,0), (1,0), config.center)
    print(f"side = {side}, alpha = {alpha}")
    alpha = (alpha + side*alpha_offset) % (2*PI)
    config.theta_femur = beta_offset * side % (2*PI)
    config.theta_tibia = gamma_offset * side % (2*PI)
    return alpha

config.theta_coxa = calculate_theta_coxa()
# Update the posture of the arm
arm = RoboterArm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
arm.update_joints(config.theta_coxa, config.theta_femur, config.theta_tibia)

# Plot: Robotic arm
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Set axis limits considering the link lengths
arm_length = config.coxa_length + config.femur_length + config.tibia_length
ax.set_xlim(-arm_length,  arm_length)
ax.set_ylim(-arm_length,  arm_length)
line, = ax.plot([], [], 'o-', lw=2)
point, = ax.plot([], [], 'ro', markersize=8)

line.set_data([], [])
point.set_data([], [])
obstacle_circle = plt.Circle(config.center, config.radius, fc='y')

# Actualize data for the next frame
line.set_data([0, arm.joint_coxa_x, arm.joint_femur_x, arm.joint_tibia_x], [0, arm.joint_coxa_y, arm.joint_femur_y, arm.joint_tibia_y])
point.set_data([config.target_x], [config.target_y])  # Update the position of the target point
obstacle_circle = plt.Circle(config.center, config.radius, fc='y')
plt.figure(fig.number)
plt.gca().add_patch(obstacle_circle)

#plt.show()
plt.savefig('starting_posture_5.pdf', bbox_inches='tight')