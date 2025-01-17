import math

def circle_stats(radius):
    """
    Calculate the area and circumference of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        tuple: A tuple containing the area (float) and circumference (float) of the circle.
    """
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))
area, circumference = circle_stats(radius)
print("Area of the circle: ", area) 
print("Circumference of the circle: ", math.floor(circumference))
print("Circumference of the circle: ", circumference)