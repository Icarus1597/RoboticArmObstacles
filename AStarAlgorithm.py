import numpy as np
import PotentialFields as pf
import Obstacles
import config

PI = np.pi

class AStarNode:
    # Initializes the Point for the A-Star search
    # Inputs:
    def __init__(self, position, goal_point):
        self.position = position
        self.goal_point = goal_point
        self.evaluation_function = 0
        self.parent_node = None
    
    def iterative_search(self, open_list, closed_list) :
        for node in open_list:
            print(f"Node: {node.position}")
        node = self.smallest_evaluation_function(open_list)
        open_list.remove(node)
        closed_list.append(node)

        if(node.position == node.goal_point):
            print("SUCCESS!\n")
            return node.path_node_list()
        
        if(len(open_list)== 0 ):
            print("FAIL: Goal point cannot be reached")
            return -1
        
        if(Obstacles.distance_to_circle(config.center, config.radius, node.position)<= 0):
            return -1
        
        neighbouring_nodes = node.generate_neighbouring_nodes()
        for neighbour in neighbouring_nodes:
            neighbour_evaluation_function = neighbour.calculate_evaluation_function()
            if not(closed_list.__contains__(neighbour)):
                if not (open_list.__contains__(neighbour)):
                    open_list.append(neighbour)
                    neighbour.parent_node = node
                else :
                    if(neighbour_evaluation_function < node.evaluation_function):
                        neighbour.parent_node = node
                        neighbour.evaluation_function = neighbour_evaluation_function
        return
    
    # Searches for the node with the smallest evaluation function in the open list
    # Output:
    #   node_smallest_evaluation_function: The node with the smallest evaluation function in open_list
    def smallest_evaluation_function(self, open_list):
        if(open_list == None):
            return -1
        node_smallest_evaluation_function = open_list[0]
        current_smallest_evaluation_function_value = open_list[0].evaluation_function
        for node in open_list:
            if(current_smallest_evaluation_function_value > node.evaluation_function): 
                current_smallest_evaluation_function_value = node.evaluation_function
                node_smallest_evaluation_function = node
        return node_smallest_evaluation_function
    
    # Generates the neighbouring nodes of this node
    # Parameters:
    #   number_neighbouring_nodes:  Number of neighbouring nodes, typically 4/8/16
    #   distance_to_neighbour:      Distance between current node and the neighbours
    # Output:
    #   neighbouring_nodes:         The neighbouring nodes of Type Node
    def generate_neighbouring_nodes(self):
        neighbouring_nodes = []
        for i in range (config.number_neighboring_nodes):
            alpha = 2 * PI / config.number_neighboring_nodes * i
            position_x = self.position[0] + np.cos(alpha)*config.distance_to_neighbour
            position_y = self.position[1] + np.sin(alpha)*config.distance_to_neighbour
            new_node = AStarNode((position_x, position_y), self.goal_point)
            neighbouring_nodes.append(new_node)
        
        return neighbouring_nodes
    
    # Calculates the evaluation function of the node with cartesian distance
    # Output: 
    #   g : Total cost of current node
    #   h : Estimated cost from current node to goal point
    def calculate_evaluation_function(self):
        if(self.parent_node == None):
            g = 0
        else:
            g = self.parent_node.evaluation_function + pf.cartesian_distance(self.parent_node.position, self.position)
        h = pf.cartesian_distance(self.goal_point, self.position)
        return g + h
    
    # Wraps the iterative search and iterates over every node in open_list
    # Input:
    #   arm:    To calculate the initial_point based on the end_effector of the arm
    #   goal_point: Target Point of the End Effector
    # Output:
    #   -1 : If no path is found
    #   path_node_list: list of the nodes of the path found
    def iterative_search_wrapper(self):
        open_list = []
        closed_list = []
        #initial_point = AStarNode(arm.end_effector, goal_point)
        open_list.append(self)

        while open_list:
            result = self.iterative_search(open_list, closed_list)
            if result:
                return result
        return -1
    
    # Backtracking after finding the shortest path 
    # Output:
    #   path_node_list: return a list of all the nodes on the shortest path 
    def path_node_list(self):
        path_node_list = []
        current_node = self
        path_node_list.append(self)
        while(current_node.parent_node != None):
            path_node_list.append(current_node.parent_node)
            current_node = current_node.parent_node
        path_node_list.reverse()
        return path_node_list