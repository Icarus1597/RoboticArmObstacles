import unittest
import AStarAlgorithm
import config

class TestAStarAlgorithm(unittest.TestCase):
    
    def test_constructor(self):
        node = AStarAlgorithm.AStarNode((4, 5), (6, 7))

        self.assertEqual(node.position, (4, 5))
        self.assertEqual(node.goal_point, (6, 7))
        self.assertEqual(node.true_cost, 0)
        self.assertAlmostEqual(node.estimated_cost, 2.82842712474)
        self.assertEqual(node.parent_node, None)
        
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

        node3 = AStarAlgorithm.AStarNode((10, 10), (10, 10))
        evaluation_function3 = node3.calculate_evaluation_function()

        self.assertAlmostEqual(evaluation_function3, 0)

        node2.parent_node = node3
        evaluation_function2 = node2.calculate_evaluation_function()

        self.assertAlmostEqual(evaluation_function2, 25.4558441227)

        node4 = AStarAlgorithm.AStarNode((1,8), (10, 10))
        node4.parent_node = node2
        node2.parent_node = node
        node.calculate_evaluation_function()
        evaluation_function2 = node2.calculate_evaluation_function()

        self.assertAlmostEqual(node2.true_cost, 1.41421356237)

        node4.calculate_evaluation_function()

        self.assertAlmostEqual(node4.true_cost, 8.41421356237)
        self.assertAlmostEqual(node4.estimated_cost, 9.219544457292)
        self.assertAlmostEqual(node4.calculate_evaluation_function(), 17.63375801966)

    def test_smallest_evaluation_function(self):
        node = AStarAlgorithm.AStarNode((4, 5), (6, 7))

        self.assertEqual(node.smallest_evaluation_function(None), -1)

        open_list = []
        open_list.append(node)

        self.assertEqual(node.smallest_evaluation_function(open_list), node)

        node2 = AStarAlgorithm.AStarNode((4, 6), (6, 7))
        node2.calculate_evaluation_function()
        open_list.append(node2)

        self.assertEqual(node.smallest_evaluation_function(open_list), node2)
        self.assertNotEqual(node.smallest_evaluation_function(open_list), node)

        node3 = AStarAlgorithm.AStarNode((6,7), (6,7))
        node3.calculate_evaluation_function()
        open_list.append(node3)

        self.assertEqual(node.smallest_evaluation_function(open_list), node3)

        node3.parent_node = node2
        node3.calculate_evaluation_function()

        self.assertEqual(node.smallest_evaluation_function(open_list), node2)

    def test_path_node_list(self):
        node = AStarAlgorithm.AStarNode((4, 5), (6, 7))

        self.assertEqual(len(node.path_node_list()), 1)

        node2 = AStarAlgorithm.AStarNode((1, 2), (6, 7))
        node2.parent_node = node
        path_node_list = node2.path_node_list()

        self.assertEqual(len(path_node_list), 2)
        self.assertEqual(path_node_list[0], node)
        self.assertEqual(path_node_list[1], node2)

        node3 = AStarAlgorithm.AStarNode((1, 5), (6, 7))
        node3.parent_node = node2
        path_node_list = node3.path_node_list()

        self.assertEqual(len(path_node_list), 3)
        self.assertEqual(path_node_list[0], node)
        self.assertEqual(path_node_list[1], node2)
        self.assertEqual(path_node_list[2], node3)


if __name__ == "__main__":
    unittest.main()
