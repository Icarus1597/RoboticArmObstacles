import numpy as np

# Test Parameter:
# Position of the target
target_x, target_y = -12,0

# delta_t Time between frames
delta_t = 300

# Position and radius of the obstacle (circle)
center = (-6, -1)
radius = 2

# Hard maximum velocity
max_velocity = 2

# Lenghts of the arm segments
coxa_length = 7
femur_length = 6
tibia_length = 4

# Max. distance between end effector and target point for success
delta_success_distance = 2

# damping factor for arm velocity
damping_factor =  0.0001

# rho_0 : max range repulsive field
# k     : repulsive potential gain
rho_0 = 4
k = 15

# zeta  : attractive potential gain
zeta = 1.1

PI = np.pi
# Start Position of the arm (posture/angles):
theta_coxa = 3/2*np.pi
theta_femur = 0
theta_tibia = 0
theta_coxa = PI/4
theta_femur = PI
theta_tibia = PI

# Maximum total time in seconds
timeout = 120

# If the distance between obstacle and arm is smaller than this, stop the arm/abort execution
min_distance_to_obstacle = 0.25