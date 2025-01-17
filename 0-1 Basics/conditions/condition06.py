# Program to determine the type of a triangle based on its side lengths

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Example usage
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

print("The triangle is:", triangle_type(side1, side2, side3))