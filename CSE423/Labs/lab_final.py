from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

STROKE = 5
WIDTH = 500
HEIGHT = 500
WINDOW_TITLE = b"LAB FINAL"


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


def drawRect(x1, y1, x2, y2):
    drawLine(x1, y2, x2, y2)
    drawLine(x1, y1, x1, y2)
    drawLine(x2, y1, x2, y2)
    drawLine(x1, y1, x2, y1)


def drawCircle(x1, y1, rad):
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
    setColor("YELLOW")
    for i in range(4):
        mul = i * 55
        drawRect(100 + mul, 100 + mul, 400 - mul, 400 - mul)
        if mul < 140:
            drawCircle(HEIGHT / 2, WIDTH / 2, 140 - mul)
        else:
            drawCircle(HEIGHT / 2, WIDTH / 2, 10)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(WINDOW_TITLE)
glutDisplayFunc(showScreen)

glutMainLoop()
