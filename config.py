import numpy as np

# Test Parameter:
# Position of the target
target_x, target_y = -12,0.1

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
min_distance_to_obstacle = 0.75

# Counter for types of test results
number_timeout = 0
number_success = 0
number_error_ee = 0
number_error_tibia = 0
number_error_femur = 0
number_error_coxa = 0

# Lists to later calculate mean of covered distance and time needed
list_covered_distance = []
list_time_needed = []
list_time_needed_for_calculation = []

# Parameters A Star Algorithm
distance_to_neighbour = 1.5
number_neighboring_nodes = 8
#max_distance_to_target = distance_to_neighbour # Should be smaller/equal to distance_to_neighbour

# Parameters inverse Kinematics
tolerance = 0.5
learning_rate = 0.1

# Change Ellbow Posture Mode
coxa_elbow_goal = (0,0)
goal_femur_angle = 0

tibia_elbow_goal = (0,0)
goal_tibia_angle = 0