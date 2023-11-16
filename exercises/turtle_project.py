"""Calm Sunset in the Mountains."""

__author__ = "730697392"

from turtle import Turtle, colormode, done 
colormode(255)
 
toe: Turtle = Turtle()
toe.speed(15)


def main() -> None:
    """The entrypoint of my scene."""
    sky(toe, 100, 100, 100)
    grass(toe, 100, 100, 100)
    sun(toe, 100, 100, 100)
    mountains(toe, 100, 100, 100)
    done()


def sky(turtle: Turtle, x: float, y: float, width: float) -> None:
    """The beautiful sky."""
    toe.penup()
    toe.goto(-500, -500)
    toe.pendown()
    toe.fillcolor(251, 178, 106)
    toe.begin_fill()
    i: int = 0
    while i < 4:
        toe.forward(2000)
        toe.left(90)
        i += 1
    toe.end_fill()


def grass(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Implements the grass in the scene."""
    toe.pencolor(99, 188, 94)
    toe.penup()
    toe.goto(-500, -500)
    toe.pendown()
    toe.fillcolor(99, 188, 94)
    toe.begin_fill()
    i: int = 0
    while i < 2:
        toe.forward(1000)
        toe.left(90)
        toe.forward(430)
        toe.left(90)
        i += 1
    toe.end_fill()


def sun(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Creates a sun that appears in the scene."""
    toe.pencolor("yellow")
    toe.penup() 
    toe.goto(5, -150)
    toe.pendown()
    toe.fillcolor("yellow")
    toe.begin_fill()
    toe.circle(200)
    toe.end_fill()


def mountains(turtle: Turtle, x: float, y: float, width: float) -> None:
    """Generates mountains."""
    toe.color("black")
    positions = [(-450, -160), (-200, -210), (0, -130), ]
    for x, y in positions:
        toe.fillcolor("grey")
        toe.begin_fill()
        toe.penup()
        toe.goto(x, y)
        toe.pendown()
        for _ in range(3):
            toe.forward(400)
            toe.left(120)
        toe.end_fill()
        toe.penup()
    done()


if __name__ == "__main__":
    main()