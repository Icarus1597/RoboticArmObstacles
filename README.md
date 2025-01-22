# Obstacle avoidance of a planar robotic arm with A*-Algorithm and Potential Fields Method
## Content
1. RoboterArm.py
2. config.py
3. PotentialFields.py
4. Visuals.py
5. AStarAlgorithm.py
6. AStarWrapper.py
7. Obstacles.py
8. Test.py

## RoboterArm.py
#### Contains RoboticArm Class with attributes for the link lengths
- update_joints: updates the posture of the joints given the corresponding thetas
- jacobian_matrix: calculates the Jacobian Matrix for the current posture
- inverse_jacobian_matrix: Calculates the pseudoinverse of a Jacobian Matrix
- distance_segment_point: Calculates the distance between a link and a point
- distance_arm_obstacle: Calculates the distance between an obstacle and the arm using the distance_segment_point method
- error_target_end_effector: Calculates the distance between the target point and the end effector
- inverse_kinematics: Calculates new thetas to move the arm towards a specified target
## config.py
#### Specifies parameters for the arm and algorithms
## PotentialFields.py
#### Calculates the Potential Fields and resulting joint velocities for the arm
- u_att_function: calculates the attractive potential field
- cartesian_distance: Calculates the cartesian distance between two points
- u_rep_function: similar to u_att_function, calculates the repulsive potential field
- v_att_function: Calculates the Attraction Velocity based on u_att_function in Cartesian Space
- V_att: adds to the result of v_att_function the Angular Velocity
- v_rep_function: Calculates the Repulsive Velocity based on u_rep_function in Cartesian Space
- V_rep: adds to the result of v_rep_function the Angular Velocity 
- joint_velocities_att: Converts v_att from Cartesian Space to Joint Space
- joint_velocities_rep: Converts v_rep from Cartesian Space to Joint Space
## Visuals.py
#### - Wrapper for Potential Fields Method
#### - Handles the animation and movement of the robotic arm, using the Potential Fields Method
## AStarAlgorithm.py
#### Implements the A* Algorithm and defines class A* Node
- init: Initializes a new A* Node
- iterative_search: searches the node with the smallest estimated cost and adds all its neighbours to the open_list
- is_contained_in_list: Determines, if a node is already contained in the list, depending on the position of the nodes
- smallest_evaluation_function: Searches for the node with the smallest evaluation function in the open list
- generate_neighbouring_nodes: Generates the neighbouring nodes of the given node
- calculate_evaluation_function: Calculates the evaluation function of the node using cartesian distance
- iterative_search_wrapper: Wraps the iterative search and iterates over every node in open_list, searching for the shortest path form the initial node to the target point
- path_node_list: Backtracking after finding the shortest path, returns list in the correct order to be used by the arm
## AStarWrapper.py
#### Similar to Visuals.py, handles the animation, computation of the A* Algorithm and movement of the robotic arm
## Obstacles.py
#### To calculate the distance from the obstacle(s) to the robotic arm
## Test.py
#### Defines a series of tests with different arm, target and obstacle positions and size to thoroughly test the algorithms, tracking the covered distance, durance and success rate


