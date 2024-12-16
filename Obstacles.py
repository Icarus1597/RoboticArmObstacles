import PotentialFields as pf

# Method to calculate the distance between a circle and a point
# Input:
#   center:   center point of the circle
#   point:    point for which the distance shall be calculated
#   radius:   radius of the circle
# Ouput:
#   distance: distance between the point and the border of the circle
def distance_to_circle(center, radius, point):
    distance = pf.cartesian_distance(center, point) - radius
    if(distance < 0) : 
        distance = 0
    return distance