# Obstacle avoidance of a planar robotic arm with A*-Algorithm and Potential Fields Method

This project provides several approaches of path planning for an 3-DOF robotic arm with obstacle avoidance. The approaches are based on A* algorithm and artificial Potential Fields method, with extensions. 

## Files
1. config
2. geometry
3. robotic_arm
4. a_star_algorithm
5. potential_fields
6. switch_mode
7. print_test_results
8. runner
9. test_runner
10. unittest Classes

## 1. config
Here, several testing parameters are stored as well as test results and statistics.

## 2. geometry
Methods calculating cartesian distances and angles between different objects. Also, methods that calculate on which side of a line a point lies are defined here.

## 3. robotic_arm
Contains Class RoboticArm. Model of the arm, functions to manipulate the posture of it like forward and inverse kinematics.

## 4. a_star_algorithm
Implements the A* algorithm.

## 5. potential_fields
Implements the artificial potential fields method.

## 6. switch_mode
Is needed for the elbows extension, where the arm, under certain circumstances, changes the posture of its middle links. Determines, if the arm is moving normally, reflects the femur link or reflects the tibia link.

## 7. print_test_results
Methods to print the test results for each approach in testresults.txt. Prints success rate, rate and cause of unsuccessful tests, and statistics e.g. average covered distance by the end effector, average duration.

## 8. runner
There are a total of nine runners, with each implementing a different approach.
- 0 : Naive Approach
- 1 : A* without extensions
- 2 : A* algorithm with elbow extension
- 3 : A* with starting posture extension
- 4 : A* with extension apply PF method on links. See "Obstacle avoidance path planning of 6-DOF robotic arm based on improved A∗ algorithm and artificial potential field method" by Tang et al., 2023
- 5 : PF method without extensions
- 6 : PF method with extension apply repulsive potential field on all links.
- 7 : PF method with starting posture extension
- 8 : PF method with both starting posture and linkage extension

## 9. test_runner
Multiple scripts whith each of them can run a series of multiple tests.
- test_runner_calibrate_parameters: To ensure that the parameters of A* and PF method approaches are roughly the same with no obstacle influencing the path of the end effector. This leads to better comparability
- test_runner: a pre-defined set of about 80 tests. The target position is (-12, 0), the starting posture of the arm, obstacle radius and position varies.
- test_runner_closer_target: a pre-defined set of about 70 tests. Similar to test_runner, but here, the target position also varies.
- test_runner_random: create tests where the initial arm posture, target position, obstacle position and center are randomized.
- test_runner_starting_posture: a pre-defined set of 20 tests. Implemented to compare differnt starting postures.
- test_runner_multiple: Define a test scope combining multiple runs of the above runners (with different approaches)

## 10. unittest Classes
Test classes that validate the a_star_algorithm, geometry and robotic_arm methods.




