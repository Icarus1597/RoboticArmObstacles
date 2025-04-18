import numpy as np
import geometry
import config

PI = np.pi


class AStarNode:

    def __init__(self, position, goal_point):
        """ Initializes the intial point for the A* search

        Args:
            position ((float, float)): position of the initial point
            goal_point ((float, float)): position of the goal point
        """
        self.position = position
        self.goal_point = goal_point
        self.true_cost = 0
        self.estimated_cost = geometry.cartesian_distance(position, goal_point)
        self.parent_node = None
    
    def iterative_search(self, open_list, closed_list) :
        """ Searches for the node with the smallest evaluation_function
            Checks if the node is near the target (-> terminates) or is too close to the obstacle (-> abort)

        Args:
            open_list (node[]): list of not yet searched nodes
            closed_list (node[]): list of already searched nodes

        Returns:
            node[]: if target reached, list of the nodes on the path. Else, return nothing
        """

        if(len(open_list)== 0 ):
            print("FAIL: Goal point cannot be reached")
            return -1
        
        node = self.smallest_evaluation_function(open_list)
        open_list.remove(node)
        closed_list.append(node)

        if(np.abs(node.position[0] - node.goal_point[0]) < config.distance_to_neighbour and 
           np.abs(node.position[1] - node.goal_point[1]) < config.distance_to_neighbour):
            return node.path_node_list()
        
        if(geometry.distance_to_circle(config.center, config.radius, node.position) < config.min_distance_to_obstacle):
            return
        
        neighbouring_nodes = node.generate_neighbouring_nodes()
        for neighbour in neighbouring_nodes:
            neighbour_evaluation_function = neighbour.calculate_evaluation_function()
            if not(neighbour.is_contained_in_list(closed_list)):
                if not (neighbour.is_contained_in_list(open_list)):
                    open_list.append(neighbour)
                    neighbour.parent_node = node
                else :
                    if(neighbour_evaluation_function < (node.true_cost + node.estimated_cost)):
                        neighbour.parent_node = node
                        neighbour.evaluation_function = neighbour_evaluation_function
        return

    def is_contained_in_list(self, list):
        """ Determines if the node is in the list or not, comparing the positions.

        Args:
            list (node[]): list of nodes

        Returns:
            bool: True, if node is contained in list, else False
        """
        for node in list:
            if (np.abs(node.position[0] - self.position[0]) < config.distance_to_neighbour/10 and np.abs(node.position[1]- self.position[1])< config.distance_to_neighbour/10):
                return True
        return False

    def smallest_evaluation_function(self, open_list):
        """ Searches for the node with the smallest evaluation function in the open list.

        Args:
            open_list (node[]): list of nodes

        Returns:
            node: The node with the smallest evaluation function in open_list
        """
        if(open_list == None):
            return -1
        node_smallest_evaluation_function = open_list[0]
        current_smallest_evaluation_function_value = open_list[0].calculate_evaluation_function()
        for node in open_list:
            if(current_smallest_evaluation_function_value > node.calculate_evaluation_function()): 
                current_smallest_evaluation_function_value = node.calculate_evaluation_function()
                node_smallest_evaluation_function = node
        return node_smallest_evaluation_function
    
    def generate_neighbouring_nodes(self):
        """ Generates the neighbouring nodes of this node.

        Returns:
            node[]: list of the neighbouring nodes of this node
        """
        neighbouring_nodes = []
        for i in range (config.number_neighboring_nodes):
            alpha = 2 * PI / config.number_neighboring_nodes * i
            position_x = self.position[0] + np.cos(alpha)*config.distance_to_neighbour
            position_y = self.position[1] + np.sin(alpha)*config.distance_to_neighbour
            new_node = AStarNode((position_x, position_y), self.goal_point)
            neighbouring_nodes.append(new_node)
        
        return neighbouring_nodes
    
    def calculate_evaluation_function(self):
        """ Calculates the evaluation function of the node with cartesian distance.

        Returns:
            float: value of the evaluation function of this node
        """
        if(self.parent_node == None):
            self.true_cost = 0
        else:
            self.true_cost = self.parent_node.true_cost + geometry.cartesian_distance(self.parent_node.position, self.position)
        self.estimated_cost = geometry.cartesian_distance(self.goal_point, self.position)
        return self.true_cost + self.estimated_cost
    
    def iterative_search_wrapper(self):
        """Iterativly searches nodes in open_list until target is reached of open_list is empty.

        Returns:
            node[]: If path to target found, else return -1
        """
        open_list = []
        closed_list = []
        open_list.append(self)

        while open_list:
            result = self.iterative_search(open_list, closed_list)
            if result:
                return result
        return -1
    
    def path_node_list(self):
        """ Backtracking after finding the shortest path. Reverses the list.

        Returns:
            node[]: return a list of all the nodes on the shortest path, in correct order from initial point to goal point.
        """
        path_node_list = []
        current_node = self
        path_node_list.append(self)
        while(current_node.parent_node != None):
            path_node_list.append(current_node.parent_node)
            current_node = current_node.parent_node
        path_node_list.reverse()
        target_node = AStarNode((config.target_x, config.target_y), (config.target_x, config.target_y))
        path_node_list.append(target_node)
        return path_node_list