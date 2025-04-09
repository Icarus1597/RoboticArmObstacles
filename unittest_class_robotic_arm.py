import unittest
import config
import numpy as np
import robotic_arm
import geometry

class TestRoboterArm(unittest.TestCase):
    
    def test_update_joints(self):
        arm = robotic_arm.RoboticArm(3, 3, 3)
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
        arm = robotic_arm.RoboticArm(3, 3, 3)
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
    
    '''
    def test_reflect_coxa_and_femur(self):
        arm = RoboterArm.RoboticArm(3, 3, 3)
        arm.update_joints(0, 0, 0)
        result_coxa, result_femur, result_tibia = arm.reflect_coxa_and_femur()
        self.assertAlmostEqual(result_coxa, 0)
        self.assertAlmostEqual(result_femur, 0)
        self.assertAlmostEqual(result_tibia, 0)

        arm.update_joints(0, np.pi, 0)
        result_coxa, result_femur, result_tibia = arm.reflect_coxa_and_femur()
        # TODO Hier sinnvolle Werte einfügen
        #self.assertAlmostEqual(result_coxa, 0)
        #self.assertAlmostEqual(result_femur, 0)
        #self.assertAlmostEqual(result_tibia, 0)

        # End Effector should approximately be at the same location afterwards
        arm.update_joints(result_coxa, result_femur, result_tibia)
        self.assertAlmostEqual(arm.joint_tibia[0], 3)
        self.assertAlmostEqual(arm.joint_tibia[1], 6)
    '''

    def test_reflect_femur_link(self):
        arm = robotic_arm.RoboticArm(3, 3, 3)
        arm.update_joints(0, 0, 0)
        result_coxa, result_femur, result_tibia = arm.reflect_femur_link()
        self.assertAlmostEqual(result_coxa, 0)
        self.assertAlmostEqual(result_femur, 0)
        self.assertAlmostEqual(result_tibia, 0)

        arm.update_joints(0, 50/180*np.pi, -40/180*np.pi)
        result_coxa, result_femur, result_tibia = arm.reflect_femur_link()
        self.assertAlmostEqual(result_coxa, 50/180*np.pi)
        self.assertAlmostEqual(result_femur, 310/180*np.pi)
        self.assertAlmostEqual(result_tibia, 10/180*np.pi)

        arm.update_joints(50/180*np.pi, -50/180*np.pi, 10/180*np.pi)
        result_coxa, result_femur, result_tibia = arm.reflect_femur_link()
        self.assertAlmostEqual(result_coxa, 0)
        self.assertAlmostEqual(result_femur, 50/180*np.pi)
        self.assertAlmostEqual(result_tibia, 320/180*np.pi)

    def test_reflect_tibia_link(self):
        arm = robotic_arm.RoboticArm(3, 3, 3)
        arm.update_joints(0, 0, 0)
        result_coxa, result_femur, result_tibia = arm.reflect_tibia_link()
        self.assertAlmostEqual(result_coxa, 0)
        self.assertAlmostEqual(result_femur, 0)
        self.assertAlmostEqual(result_tibia, 0)

        arm.update_joints(0, 0, 50/180*np.pi)
        result_coxa, result_femur, result_tibia = arm.reflect_tibia_link()
        self.assertAlmostEqual(result_coxa, 0)
        self.assertAlmostEqual(result_femur, 50/180*np.pi) # sinnvoller Winkel?!
        self.assertAlmostEqual(result_tibia, 310/180*np.pi)

        arm.update_joints(0, 50/180*np.pi, -50/180*np.pi)
        result_coxa, result_femur, result_tibia = arm.reflect_tibia_link()
        self.assertAlmostEqual(result_coxa, 0)
        self.assertAlmostEqual(result_femur, 0) # sinnvoller Winkel?!
        self.assertAlmostEqual(result_tibia, 50/180*np.pi)

if __name__ == "__main__":
    unittest.main()