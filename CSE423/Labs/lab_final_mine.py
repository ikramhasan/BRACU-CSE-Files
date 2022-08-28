from OpenGL.GL import *
from OpenGL.GLUT import *

STROKE = 5
WIDTH = 500
HEIGHT = 500
WINDOW_TITLE = b"LAB FINAL"


def draw_line(x1, y1, x2, y2):
    glPointSize(STROKE)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def draw_point(x, y):
    glPointSize(STROKE)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_rect(x1, y1, x2, y2):
    draw_line(x1, y2, x2, y2)
    draw_line(x1, y1, x1, y2)
    draw_line(x2, y1, x2, y2)
    draw_line(x1, y1, x2, y1)


def draw_triangle(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()


def draw_circle(x1, y1, rad):
    d = 1 - rad
    x = 0
    y = rad

    draw_circle_points(x, y, x1, y1)

    while x < y:
        if d < 0:
            d = d + 2*x + 3
            x = x+1
        else:
            d = d + 2*x - 2*y + 5
            x = x+1
            y = y-1

        draw_circle_points(x, y, x1, y1)


def draw_circle_points(x, y, x0, y0):
    draw_point(x + x0, y + y0)
    draw_point(y + y0, x + x0)
    draw_point(y + y0, -x + x0)
    draw_point(x + x0, -y + y0)
    draw_point(-x + x0, -y + y0)
    draw_point(-y + y0, -x + x0)
    draw_point(-y + y0, x + x0)
    draw_point(-x + x0, y + y0)


def set_color(color):
    if color == "RED":
        glColor3f(1.0, 0.0, 0.0)
    elif color == "GREEN":
        glColor3f(0.0, 1.0, 0.0)
    elif color == "BLUE":
        glColor3f(0.0, 0.0, 1.0)
    elif color == "BLACK":
        glColor3f(0.0, 0.0, 0.0)
    elif color == "ORANGE":
        glColor3f(1.0, 0.5, 0.0)
    elif color == "WHITE":
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(0.0, 1.0, 0.0)


def iterate():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, WIDTH, 0.0, HEIGHT, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def getZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        dx = 1

    if dy == 0:
        dy = -1

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            zone = 0

        elif dx < 0 and dy > 0:
            zone = 3

        elif dx < 0 and dy < 0:
            zone = 4

        elif dx > 0 and dy < 0:
            zone = 7

    else:
        if dx > 0 and dy > 0:
            zone = 1

        elif dx < 0 and dy > 0:
            zone = 2

        elif dx < 0 and dy < 0:
            zone = 5

        elif dx > 0 and dy < 0:
            zone = 6

    convertToZone0(x1, y1, x2, y2, zone)


def convertToZone0(x1, y1, x2, y2, zone):
    X1 = x1
    Y1 = y1
    X2 = x2
    Y2 = y2

    if zone == 0:
        x_1 = X1
        y_1 = Y1
        x_2 = X2
        y_2 = Y2

    elif zone == 1:
        x_1 = Y1
        y_1 = X1
        x_2 = Y2
        y_2 = X2

    elif zone == 2:
        x_1 = Y1
        y_1 = -X1
        x_2 = Y2
        y_2 = -X2

    elif zone == 3:
        x_1 = -X1
        y_1 = Y1
        x_2 = -X2
        y_2 = Y2

    elif zone == 4:
        x_1 = -X1
        y_1 = -Y1
        x_2 = -X2
        y_2 = -Y2

    elif zone == 5:
        x_1 = -Y1
        y_1 = -X1
        x_2 = -Y2
        y_2 = -X2

    elif zone == 6:
        x_1 = -Y1
        y_1 = X1
        x_2 = -Y2
        y_2 = X2

    elif zone == 7:
        x_1 = X1
        y_1 = -Y1
        x_2 = X2
        y_2 = -Y2

    midpointLine(x_1, y_1, x_2, y_2, zone)


def midpointLine(x_1, y_1, x_2, y_2, zone):
    dX = x_2 - x_1
    dY = y_2 - y_1

    if dX == 0:
        dX = 1

    if dY == 0:
        dY = -1

    d = 2 * dY - dX
    NE = 2 * (dY - dX)
    E = 2 * dY

    X = x_1
    Y = y_1

    while X < x_2:
        revertTo(X, Y, zone)
        X = X + 1

        if d > 0:
            Y = Y + 1
            d = d + NE
        else:
            d = d + E


def revertTo(X, Y, zone):
    if zone == 0:
        x = X
        y = Y
        draw(x, y)

    if zone == 1:
        x = Y
        y = X
        draw(x, y)

    if zone == 2:
        x = -Y
        y = X
        draw(x, y)

    if zone == 3:
        x = -X
        y = Y
        draw(x, y)

    if zone == 2:
        x = -Y
        y = X
        draw(x, y)

    if zone == 5:
        x = -Y
        y = -X
        draw(x, y)

    if zone == 6:
        x = Y
        y = -X
        draw(x, y)

    if zone == 7:
        x = X
        y = -Y
        draw(x, y)


def draw(X, Y):
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(X, Y)
    glEnd()


def show_screen():
    x1 = 100
    y1 = 100
    x2 = WIDTH / 2
    x3 = 400
    y2 = 300
    y3 = 200
    y4 = y2
    y5 = y1
    x4 = x3
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    set_color("GREEN")
    draw_triangle(x1, y1, x1, y2, x2, y3)
    set_color("RED")
    draw_triangle(x2, y3, x1, y2, x3, y4)
    set_color("RED")
    draw_triangle(x2, y3, x1, y2, x3, y4)
    set_color("BLUE")
    draw_triangle(x2, y3, x3, y4, x3, y1)
    set_color("ORANGE")
    draw_triangle(x4, y5, x2, y3, x1, y1)
    set_color("WHITE")
    draw_circle(x1, y1, 30)
    set_color("WHITE")
    draw_circle(x1, y2, 30)
    set_color("WHITE")
    draw_circle(x3, y4, 30)
    set_color("WHITE")
    draw_circle(x4, y5, 30)
    getZone(250, y3+150, 250, y5 - 100)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(WINDOW_TITLE)
glutDisplayFunc(show_screen)

glutMainLoop()
