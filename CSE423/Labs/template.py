from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

STROKE = 5
WIDTH = 640
HEIGHT = 480
WINDOW_TITLE = b"WINDOW"


def drawLine(x1, y1, x2, y2):
    glPointSize(STROKE)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def drawPoint(x, y):
    glPointSize(STROKE)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


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
    glOrtho(0.0, 500, 0.0, 400, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    setColor("YELLOW")
    drawLine(100, 30, 390, 30)
    drawPoint(245, 60)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(WINDOW_TITLE)
glutDisplayFunc(showScreen)

glutMainLoop()
