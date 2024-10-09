import numpy as np

# Test Parameter:
# Position of the target
target_x, target_y = -12,0

# delta_t Time between frames
delta_t = 300

# Position and radius of the obstacle (circle)
center = (-6, 0)
radius = 4

# Hard maximum velocity
max_velocity = 2

# Lenghts of the arm segments
coxa_length = 7
femur_length = 6
tibia_length = 4

# Max. distance between end effector and target point for success
delta_success_distance = 0.2

# damping factor for arm velocity
damping_factor =  0.0001

# rho_0 : max range repulsive field
# k     : repulsive potential gain
rho_0 = 2
k = 20

# zeta  : attractive potential gain
zeta = 5

# Start Position of the arm (posture/angles):
theta_coxa = np.pi/2
theta_femur = 0
theta_tibia = 0
