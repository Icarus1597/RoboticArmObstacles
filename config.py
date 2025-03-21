import numpy as np

# Test Parameter:
# Position of the target
target_x, target_y = -12,0.1

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

# Max. distance between end effector and target point for success
delta_success_distance = 2.5

# damping factor for arm velocity
damping_factor =  0.000108

# rho_0 : max range repulsive field
# k     : repulsive potential gain
rho_0 = 5
k = 15

rho_0_femur = tibia_length
k_femur = 100

rho_0_coxa = 3
k_coxa = 100

# zeta  : attractive potential gain
zeta = 1

PI = np.pi
# Start Position of the arm (posture/angles):
theta_coxa = 0
theta_femur = PI/2
theta_tibia = PI/2

# Maximum total time in seconds
timeout = 240

# If the distance between obstacle and arm is smaller than this, stop the arm/abort execution
min_distance_to_obstacle = 2

""" config.wrapper_mode: (in config)
0 : Naive Approach
1 : A*
2 : A* algorithm with own approach to avoid obstacle with whole linkage reflecting elbows
3 : A* with adjusting starting position
4 : A* inspired by Tang with PF for linkage
5 : PF
6 : PF Linkage
7 : PF Starting Position
8 : PF Starting Position and Linkage
"""
wrapper_mode = 0
# For mode 0 : A* algorithm
astar_list_covered_distance = []
astar_time_needed = []
astar_time_needed_calculation = []
astar_number_success = 0
astar_number_error_tibia = 0
astar_number_error_femur = 0
astar_number_error_coxa = 0
astar_number_error_no_path = 0
astar_number_error_ee = 0
astar_timeout = 0

# For mode 1 : conventional Potential Field method
pf_list_covered_distance = []
pf_time_needed = []
pf_number_timeout = 0
pf_number_success = 0
pf_number_error_tibia = 0
pf_number_error_femur = 0
pf_number_error_coxa = 0
pf_number_error_ee = 0

# For mode 2 : A* with changig elbow posture
elbow_start_position_list_covered_distance = []
elbow_start_position_time_needed = []
elbow_start_position_time_needed_calculation = []
elbow_start_position_number_timeout = 0
elbow_start_position_number_success = 0
elbow_start_position_number_error_tibia = 0
elbow_start_position_number_error_femur = 0
elbow_start_position_number_error_coxa = 0
elbow_start_position_number_error_ee = 0

# For mode 3 : Naive Approach
naive_list_covered_distance = []
naive_list_time_needed = []
naive_number_success = 0
naive_number_error_tibia = 0
naive_number_error_femur = 0
naive_number_error_coxa = 0
naive_number_error_ee = 0

# For mode 4 : PF applied to all links
pf_all_links_list_covered_distance = []
pf_all_links_time_needed = []
pf_all_links_number_timeout = 0
pf_all_links_number_success = 0
pf_all_links_number_error_tibia = 0
pf_all_links_number_error_femur = 0
pf_all_links_number_error_coxa = 0
pf_all_links_number_error_ee = 0

# PF starting position
pf_sp_list_covered_distance = []
pf_sp_time_needed = []
pf_sp_number_timeout = 0
pf_sp_number_success = 0
pf_sp_number_error_tibia = 0
pf_sp_number_error_femur = 0
pf_sp_number_error_coxa = 0
pf_sp_number_error_ee = 0

# PF starting position and whole linkage
pf_sp_linkage_list_covered_distance = []
pf_sp_linkage_time_needed = []
pf_sp_linkage_number_timeout = 0
pf_sp_linkage_number_success = 0
pf_sp_linkage_number_error_tibia = 0
pf_sp_linkage_number_error_femur = 0
pf_sp_linkage_number_error_coxa = 0
pf_sp_linkage_number_error_ee = 0

# For mode 5: A* algorithm but moves to specific start position first
astar_start_position_list_covered_distance = []
astar_start_position_time_needed = []
astar_start_position_time_needed_calculation = []
astar_start_position_number_timeout = 0
astar_start_position_number_success = 0
astar_start_position_number_error_tibia = 0
astar_start_position_number_error_femur = 0
astar_start_position_number_error_coxa = 0
astar_start_position_number_error_ee = 0

# A* algorithm after Tang
astar_tang_list_covered_distance = []
astar_tang_time_needed = []
astar_tang_time_needed_calculation = []
astar_tang_number_timeout = 0
astar_tang_number_success = 0
astar_tang_number_error_tibia = 0
astar_tang_number_error_femur = 0
astar_tang_number_error_coxa = 0
astar_tang_number_error_ee = 0
astar_tang_number_error_no_path = 0

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