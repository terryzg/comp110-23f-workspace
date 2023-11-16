"""Defining a Point!"""


from __future__ import annotations


__Author__ = "730697392"


class Point:
    """A point on a (x,y) coordinate."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Creates a point with x and y coordinates."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point with scaled coodinates."""
        scale_x = self.x * factor
        scale_y = self.y * factor
        return Point(scale_x, scale_y)

    def __str__(self) -> str:
        """str operator overload."""
        output: str = f"x:{self.x}; y:{self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, factor: int | float) -> Point:
        """Addition operator overload."""
        return Point(self.x + factor, self.y + factor)

