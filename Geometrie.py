import numpy as np
# TODO

# Function to calculate the reflection of a point P(x0, y0) across a line defined by points (x1, y1) and (x2, y2)
def reflect_on_hypotenuse(arm, x0, y0, x1, y1, x2, y2):
    # Calculate the reflection of the point (x0, y0) across the line (x1, y1) - (x2, y2)
    
    # Compute the slope of the line
    dx = x2 - x1
    dy = y2 - y1
    
    # If the line is vertical (dx == 0), the reflection is straightforward horizontally
    if dx == 0:
        return 2 * x1 - x0, y0
    
    # Calculate the slope of the line
    m = dy / dx
    
    # Calculate the y-intercept b of the line
    b = y1 - m * x1
    
    # Compute the foot of the perpendicular from point P (x0, y0) to the line
    # The perpendicular line has a slope of -1/m
    # Equation of the perpendicular line: y - y0 = -1/m * (x - x0)
    
    # Calculate the intersection point of the two lines (the foot of the perpendicular)
    A = 1 + m**2
    B = 2 * (m * (b - y0) - x0)
    C = x0**2 + (b - y0)**2 - (x1**2 + y1**2)
    
    # Calculate the intersection point
    x_intersection = -B / (2 * A)
    y_intersection = m * x_intersection + b
    
    # The reflection point is at the same distance from the foot of the perpendicular as the original point
    x_reflection = 2 * x_intersection - x0
    y_reflection = 2 * y_intersection - y0
    
    return x_reflection, y_reflection
