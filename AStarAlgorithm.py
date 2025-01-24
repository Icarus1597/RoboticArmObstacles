import numpy as np
import matplotlib.pyplot as plt
import PotentialFields as pf
import Obstacles
import config
import time

PI = np.pi

class AStarNode:
    # Initializes the Point for the A-Star search
    # Inputs:
    def __init__(self, position, goal_point):
        self.position = position
        self.goal_point = goal_point
        self.true_cost = 0
        self.estimated_cost = pf.cartesian_distance(position, goal_point)
        self.parent_node = None
    
    def iterative_search(self, open_list, closed_list, search_points_plot) :
        #for node in open_list:
            #print(f"Node: {node.position}")

        if(len(open_list)== 0 ):
            print("FAIL: Goal point cannot be reached")
            return -1
        
        node = self.smallest_evaluation_function(open_list)
        open_list.remove(node)
        closed_list.append(node)

        x = np.array([node.position[0]])
        y = np.array([node.position[1]])
        
        plt.figure(search_points_plot.number) #To make sure, the correct plot is the active one
        plt.scatter(x, y)
        plt.show()

        if(np.abs(node.position[0] - node.goal_point[0]) < config.distance_to_neighbour and 
           np.abs(node.position[1] - node.goal_point[1]) < config.distance_to_neighbour):
            print("SUCCESS! Reached goal point in AStar Path Calculation\n")
            return node.path_node_list()
        
        if(Obstacles.distance_to_circle(config.center, config.radius, node.position) < config.min_distance_to_obstacle):
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

    # Determines if the node is in the list or not, comparing the position
    # Input:
    #   list: list to search the node
    # Output:
    #   True, if there is a node in the list at the same position
    #   False, if there is not a node in the list at the same position
    def is_contained_in_list(self, list):
        for node in list:
            if (np.abs(node.position[0] - self.position[0]) < config.distance_to_neighbour/10 and np.abs(node.position[1]- self.position[1])< config.distance_to_neighbour/10):
                return True
        return False

    
    # Searches for the node with the smallest evaluation function in the open list
    # Output:
    #   node_smallest_evaluation_function: The node with the smallest evaluation function in open_list
    def smallest_evaluation_function(self, open_list):
        if(open_list == None):
            return -1
        node_smallest_evaluation_function = open_list[0]
        current_smallest_evaluation_function_value = open_list[0].calculate_evaluation_function()
        for node in open_list:
            if(current_smallest_evaluation_function_value > node.calculate_evaluation_function()): 
                current_smallest_evaluation_function_value = node.calculate_evaluation_function()
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
            self.true_cost = 0
        else:
            self.true_cost = self.parent_node.true_cost + pf.cartesian_distance(self.parent_node.position, self.position)
        self.estimated_cost = pf.cartesian_distance(self.goal_point, self.position)
        return self.true_cost + self.estimated_cost
    
    # Wraps the iterative search and iterates over every node in open_list
    # Input:
    #   arm:    To calculate the initial_point based on the end_effector of the arm
    #   goal_point: Target Point of the End Effector
    # Output:
    #   -1 : If no path is found
    #   path_node_list: list of the nodes of the path found
    def iterative_search_wrapper(self, search_points_plot):
        open_list = []
        closed_list = []
        #initial_point = AStarNode(arm.end_effector, goal_point)
        open_list.append(self)

        while open_list:
            result = self.iterative_search(open_list, closed_list, search_points_plot)
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
        print(f"Length Path Node List = {len(path_node_list)}")
        return path_node_list