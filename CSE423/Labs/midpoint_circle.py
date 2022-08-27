from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 here
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # where the pixel shows
    glEnd()


def circle_point(x, y, x0, y0):
    draw_points(x+x0, y+y0)
    draw_points(y+y0, x+x0)
    draw_points(y+y0, -x+x0)
    draw_points(x+x0, -y+y0)
    draw_points(-x+x0, -y+y0)
    draw_points(-y+y0, -x+x0)
    draw_points(-y+y0, x+x0)
    draw_points(-x+x0, y+y0)


def midpoint_circle(radius, x0, y0):
    d = 1-radius
    x = 0
    y = radius
    circle_point(x, y, x0, y0)
    while x < y:
        if d < 0:
            d = d + 2*x + 3
            x = x+1
        else:
            d = d + 2*x - 2*y + 5
            x = x+1
            y = y-1
        circle_point(x, y, x0, y0)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # color set (RGB)
    # callING THE METHODS
    radius = 150
    x = 250
    y = 250

    midpoint_circle(radius, x, y)
    midpoint_circle(radius/2, x+50, y+50)
    midpoint_circle(radius / 2, x - 50, y - 50)
    midpoint_circle(radius / 2, x + 50, y - 50)
    midpoint_circle(radius / 2, x - 50, y + 50)

    midpoint_circle(radius / 2, x + 80, y)
    midpoint_circle(radius / 2, x - 80, y)
    midpoint_circle(radius / 2, x, y - 80)
    midpoint_circle(radius / 2, x, y + 80)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Screen")
glutDisplayFunc(showScreen)

glutMainLoop()
