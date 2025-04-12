import unittest
import config
import numpy as np
import robotic_arm
import geometry

class Testgeometry(unittest.TestCase):

    def test_which_side_small_angle(self):
        arm = robotic_arm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
        arm.update_joints(np.pi/4, np.pi/2, np.pi*3/2)
        self.assertEqual(geometry.which_side_small_angle(arm.theta_coxa), 0)
        self.assertEqual(geometry.which_side_small_angle(arm.theta_femur), 0)
        self.assertEqual(geometry.which_side_small_angle(arm.theta_tibia), 1)

    def test_distance_segment_point(self):
        result = geometry.distance_segment_point(3, 3, 0, 0, 0, 5)
        self.assertEqual(result, 3)

        result = geometry.distance_segment_point(-3, 3, 0, 0, 0, 5)
        self.assertEqual(result, 3)
    
    def test_side_point_to_line(self):
        result = geometry.side_point_to_line((1, 0), (0, 0), (1, 1))
        self.assertEqual(result, 1)

        result = geometry.side_point_to_line((0, 1), (0, 0), (1, 1))
        self.assertEqual(result, -1)

        result = geometry.side_point_to_line((0, 1), (1, 1), (0, 0))
        self.assertEqual(result, 1)
        return
    
    def test_boolean_switch_elbow(self):
        arm = robotic_arm.RoboticArm(config.coxa_length,config.femur_length,config.tibia_length)
        arm.update_joints(np.pi/4, np.pi/4, np.pi/4)
        config.center = (-1, 5)
        bool_result_coxa, bool_result_tibia = geometry.booleans_switch_elbows(arm, config.center)

        # Should both be on correct side
        self.assertEqual(bool_result_coxa, 1)
        self.assertEqual(bool_result_tibia, 1)

        arm.update_joints(np.pi/4, np.pi/4, np.pi*3/2)
        config.center = (-1, 5)
        bool_result_coxa, bool_result_tibia = geometry.booleans_switch_elbows(arm, config.center)

        # Coxa should still be correct, tibia on the other side
        self.assertEqual(bool_result_coxa, 1)
        self.assertEqual(bool_result_tibia, 0)

        arm.update_joints(np.pi/4*5, np.pi/4, 0)
        config.center = (-1, 5)
        bool_result_coxa, bool_result_tibia = geometry.booleans_switch_elbows(arm, config.center)

        # Should both be on wrong side
        self.assertEqual(bool_result_coxa, 0)
        self.assertEqual(bool_result_tibia, 0)
        return
    
    def test_angle_vector_joint(self):
        arm = robotic_arm.RoboticArm(1, 1, 1)
        arm.update_joints(0, 0, 0)
        config.center = (0, 3)
        alpha = geometry.angle_vector_point((0,0), arm.joint_coxa, config.center)
        self.assertAlmostEqual(alpha, np.pi/2)

        config.center = (1, 1)
        alpha = geometry.angle_vector_point((0,0), arm.joint_coxa, config.center)
        self.assertAlmostEqual(alpha, np.pi/4)

        config.center = (1, -1)
        alpha = geometry.angle_vector_point((0,0), arm.joint_coxa, config.center)
        self.assertAlmostEqual(alpha, 7*np.pi/4)

        arm.update_joints(np.pi/2, 0, 0)
        config.center = (3, 0)
        alpha = geometry.angle_vector_point((0,0), arm.joint_coxa, config.center)
        self.assertAlmostEqual(alpha, 3*np.pi/2)

        config.center = (0,0)
        alpha = geometry.angle_vector_point((0,0), arm.joint_coxa, config.center)
        self.assertAlmostEqual(alpha, -1)

        config.center = (-6, 0)
        alpha = geometry.angle_vector_point((0,0), (1, 0), config.center)
        self.assertAlmostEqual(alpha, np.pi)
        alpha = (alpha + np.pi) % (2*np.pi)
        self.assertAlmostEqual(alpha, 0)

    def test_direction_coxa(self):
        config.target_x, config.target_y = (0, 5)
        config.center = (5, 5)
        config.radius = 2

        arm = robotic_arm.RoboticArm(1, 1, 1)
        arm.update_joints(0, 0, 0)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), 1)

        arm.update_joints(np.pi, 0, 0)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), 1)

        config.target_x, config.target_y = (5, 5)
        config.center = (0, 5)
        arm.update_joints(0, 0, 0)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), -1)

        arm.update_joints(np.pi, 0, 0)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), -1)

        arm.update_joints(0, 0, 0)
        config.target_x, config.target_y = (-5, 0)
        config.center = (0, 5)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), 1)

        arm.update_joints(np.pi, 0, 0)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), -1)

        config.target_x, config.target_y = (5, -4)
        config.center = (5, -2)
        arm.update_joints(0, 0, 0)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), -1)

        config.target_x, config.target_y = (5, -2)
        config.center = (5, -4)
        self.assertEqual(geometry.direction_coxa(arm.joint_femur, (config.target_x, config.target_y), config.center), 1)

if __name__ == "__main__":
    unittest.main()
    