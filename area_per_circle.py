#!/usr/bin/env python3
# Created by: Joyceline
# Created on: Sept 26 2026
# This program calculates the circumference and area of a circle.
import math


def main():
    # get the radius of the circle from the user and convert to a float
    radius = float(input("Enter the radius of the circle (mm): "))

    # Calculate the circumference of the circle
    circumference = 2 * math.pi * radius

    # Calculate the area of the circle
    area = math.pi * radius ** 2

    # Display the circumference and area to the user with proper units
    print("")
    print("Circumference is {} mm.".format(circumference))
    print("Area is {} mm².".format(area))
    print("\nDone.")


if __name__ == "__main__":
    main()
