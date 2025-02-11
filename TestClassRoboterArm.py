import unittest
import config
import numpy as np
import RoboterArm
import Geometrie

class TestRoboterArm(unittest.TestCase):
    
    def test_update_joints(self):
        arm = RoboterArm.RoboticArm(3, 3, 3)
        arm.update_joints(0, 0, 0)
        self.assertEqual(arm.theta_coxa, 0)
        self.assertEqual(arm.theta_femur, 0)
        self.assertEqual(arm.theta_tibia, 0)
        
        self.assertEqual(arm.end_effector[0], 9)
        self.assertEqual(arm.end_effector[1], 0)

        arm.update_joints(0, 0, np.pi)
        self.assertEqual(arm.theta_coxa, 0)
        self.assertEqual(arm.theta_femur, 0)
        self.assertEqual(arm.theta_tibia, np.pi)
        self.assertEqual(arm.end_effector[0], 3)
        self.assertAlmostEqual(arm.end_effector[1], 0)

        arm.update_joints(np.pi, 0, np.pi/2)
        self.assertEqual(arm.theta_coxa, np.pi)
        self.assertEqual(arm.theta_femur, 0)
        self.assertEqual(arm.theta_tibia, np.pi/2)
        self.assertAlmostEqual(arm.end_effector[0], -6)
        self.assertAlmostEqual(arm.end_effector[1], -3)

        arm.update_joints(0, np.pi/2, np.pi/2)
        self.assertEqual(arm.theta_coxa, 0)
        self.assertEqual(arm.theta_femur, np.pi/2)
        self.assertEqual(arm.theta_tibia, np.pi/2)
        self.assertAlmostEqual(arm.end_effector[0], 0)
        self.assertAlmostEqual(arm.end_effector[1], 3)
        return
    
    def test_distance_arm_obstacle(self):
        arm = RoboterArm.RoboticArm(3, 3, 3)
        arm.update_joints(0, 0, 0)
        result = arm.distance_arm_obstacle((-3, 0), 1)
        self.assertEqual(result, 2)

        arm.update_joints(0, np.pi/2, np.pi/2)
        result = arm.distance_arm_obstacle((-3, 3), 1)
        self.assertEqual(result, 2)

        result = arm.distance_arm_obstacle((6, 3), 1)
        self.assertEqual(result, 2)

        result = arm.distance_arm_obstacle((0, 0), 1)
        self.assertEqual(result, -1)

        result = arm.distance_arm_obstacle((3, 1), 1)
        self.assertEqual(result, -1)

        result = arm.distance_arm_obstacle((0, 2), 1.25)
        self.assertEqual(result, -1)

        # TODO: Cases closer to obstacle than minimum required distance
        return

if __name__ == "__main__":
    unittest.main()