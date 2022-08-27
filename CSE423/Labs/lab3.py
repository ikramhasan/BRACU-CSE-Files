from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

STROKE = 3
WIDTH = 500
HEIGHT = 500
WINDOW_TITLE = b"LAB 3"


def drawPoint(x, y):
    glPointSize(STROKE)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def midpointCircle(x1, y1, rad):
    d = 1 - rad
    x = 0
    y = rad

    drawCirclePoints(x, y, x1, y1)

    while x < y:
        if d < 0:
            d = d + 2*x + 3
            x = x+1
        else:
            d = d + 2*x - 2*y + 5
            x = x+1
            y = y-1

        drawCirclePoints(x, y, x1, y1)


def drawCirclePoints(x, y, x0, y0):
    drawPoint(x+x0, y+y0)
    drawPoint(y+y0, x+x0)
    drawPoint(y+y0, -x+x0)
    drawPoint(x+x0, -y+y0)
    drawPoint(-x+x0, -y+y0)
    drawPoint(-y+y0, -x+x0)
    drawPoint(-y+y0, x+x0)
    drawPoint(-x+x0, y+y0)


def setColor(color):
    if color == "RED":
        glColor3f(1.0, 0.0, 0.0)
    elif color == "GREEN":
        glColor3f(0.0, 1.0, 0.0)
    elif color == "BLUE":
        glColor3f(0.0, 0.0, 1.0)
    elif color == "YELLOW":
        glColor3f(1.0, 1.0, 0.0)
    elif color == "ORANGE":
        glColor3f(1.0, 0.5, 0.0)
    else:
        glColor3f(0.0, 1.0, 0.0)


def iterate():
    glViewport(0, 0, WIDTH, HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    setColor("GREEN")
    midpointCircle(250, 250, 150)
    setColor("ORANGE")
    midpointCircle(250, 250, 70)
    midpointCircle(300, 300, 70)
    midpointCircle(200, 200, 70)
    midpointCircle(300, 200, 70)
    midpointCircle(200, 300, 70)
    midpointCircle(330, 250, 70)
    midpointCircle(170, 250, 70)
    midpointCircle(250, 170, 70)
    midpointCircle(250, 330, 70)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(WINDOW_TITLE)
glutDisplayFunc(showScreen)

glutMainLoop()
