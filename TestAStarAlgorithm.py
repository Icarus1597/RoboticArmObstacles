import unittest
import AStarAlgorithm
import config

class TestAStarAlgorithm(unittest.TestCase):
    
    def test_constructor(self):
        node = AStarAlgorithm.AStarNode((4, 5), (6, 7))

        self.assertEqual(node.position, (4, 5))
        self.assertEqual(node.goal_point, (6, 7))
        self.assertEqual(node.evaluation_function, 0)
        self.assertEqual(node.parent_node, None)

    def test_smallest_evaluation_function(self):
        node = AStarAlgorithm.AStarNode((4, 5), (6, 7))

        self.assertEqual(node.smallest_evaluation_function(None), -1)

        open_list = []
        open_list.append(node)

        self.assertEqual(node.smallest_evaluation_function(open_list), node)

        node2 = AStarAlgorithm.AStarNode((4, 6), (8, 7))
        node2.evaluation_function = 5
        open_list.append(node2)

        self.assertEqual(node.smallest_evaluation_function(open_list), node)

        node.evaluation_function = 6

        self.assertEqual(node.smallest_evaluation_function(open_list), node2)
        self.assertNotEqual(node.smallest_evaluation_function(open_list), node)

        node3 = AStarAlgorithm.AStarNode((3, 3), (2, 2))
        open_list.append(node3)

        self.assertEqual(node.smallest_evaluation_function(open_list), node3)
        
    def test_generate_neighbouring_nodes(self):
        node = AStarAlgorithm.AStarNode((0, 0), (6, 7))
        config.number_neighboring_nodes = 8
        config.distance_to_neighbour = 1
        neighbouring_nodes = node.generate_neighbouring_nodes()

        self.assertEqual(len(neighbouring_nodes), 8)
        self.assertEqual(neighbouring_nodes[0].position, (1, 0))
        self.assertAlmostEqual(neighbouring_nodes[2].position[0], 0)
        self.assertAlmostEqual(neighbouring_nodes[2].position[1], 1)

    def test_calculate_evaluation_function(self):
        node = AStarAlgorithm.AStarNode((0, 0), (10, 10))
        evaluation_function = node.calculate_evaluation_function()

        self.assertAlmostEqual(evaluation_function, 14.142135623)

        node2 = AStarAlgorithm.AStarNode((1, 1), (10, 10))
        evaluation_function2 = node2.calculate_evaluation_function()

        self.assertAlmostEqual(evaluation_function2, 12.727922061)

        # TODO




if __name__ == "__main__":
    unittest.main()
