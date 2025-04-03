wrapper_mode = 1

# A*
next_node_index = 0
path_node_list = []

target = (-12, 0)

# delta_t Time between frames
delta_t = 150

# Position and radius of the obstacle (circle)
center = (-6, -1)
radius = 2

# Hard maximum velocity
max_velocity = 2

# Lenghts of the arm segments
coxa_length = 7
femur_length = 6
tibia_length = 4

theta_coxa, theta_femur, theta_tibia = 0, 0, 0

# Max. distance between end effector and target point for success
delta_success_distance = 2.5

# damping factor for arm velocity
damping_factor =  0.000108

# rho_0 : max range repulsive field
# k     : repulsive potential gain
rho_0 = 5
k = 15

rho_0_femur = 2
k_femur = 15

rho_0_coxa = 5
k_coxa = 150

# zeta  : attractive potential gain
zeta = 5

mode_sp = True
sp_target_angles = []

# Maximum total time in seconds
timeout = 240

# If the distance between obstacle and arm is smaller than this, stop the arm/abort execution
min_distance_to_obstacle = 2

# Parameters A Star Algorithm
distance_to_neighbour = 1.5
number_neighboring_nodes = 8
#max_distance_to_target = distance_to_neighbour # Should be smaller/equal to distance_to_neighbour

# Parameters inverse Kinematics
tolerance = 2
learning_rate = 0.1

# Change Elbow Posture Mode
goal_reflect_femur_link = []

goal_reflect_tibia_link = []

list_covered_distance = []
time_needed = []
time_needed_calculation = []
timeout = 0
success = 0
error_tibia = 0
error_femur = 0
error_coxa = 0
error_ee = 0
error_no_path = 0

