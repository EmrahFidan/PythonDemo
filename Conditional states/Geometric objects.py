def check_triangle_type(side1, side2, side3):
    # Check if all sides are equal
    if side1 == side2 == side3:
        return "EQUILATERAL TRIANGLE"
    # Check if at least two sides are equal
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "ISOSCELES TRIANGLE"
    else:
        return "TRIANGLE"


def check_quadrilateral_type(side1, side2, side3, side4):
    # Check if all sides are equal (opposite sides are parallel)
    if side1 == side2 == side3 == side4:
        return "SQUARE"
    # Check if opposite sides are equal (and adjacent sides are also equal)
    elif (side1 == side2 and side3 == side4) or (side1 == side3 and side2 == side4) or (side1 == side4 and side2 == side3):
        return "RECTANGLE"
    else:
        return "QUADRILATERAL"


def main():
    print("You can enter triangle (3) or quadrilateral (4)")
    shape_type = int(input("Enter the shape you want: "))

    if shape_type == 4:
        side1 = int(input("1st side: "))
        side2 = int(input("2nd side: "))
        side3 = int(input("3rd side: "))
        side4 = int(input("4th side: "))
        print(check_quadrilateral_type(side1, side2, side3, side4))
    elif shape_type == 3:
        side1 = int(input("1st side: "))
        side2 = int(input("2nd side: "))
        side3 = int(input("3rd side: "))
        # Check if the input sides can form a valid triangle using the triangle inequality theorem
        if abs(side1 + side2) > side3 and abs(side1 + side3) > side2 and abs(side2 + side3) > side1:
            print(check_triangle_type(side1, side2, side3))
        else:
            print("Does not form a triangle....")
    else:
        print("Invalid shape....")


if __name__ == "__main__":
    main()
