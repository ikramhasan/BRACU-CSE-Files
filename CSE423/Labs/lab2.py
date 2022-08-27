from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


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
    glColor3f(1.0, 0.5, 0.0)

    # call the draw methods here
    # 9
    getZone(400, 320, 550, 320)
    getZone(400, 200, 550, 200)
    getZone(400, 320, 400, 400)
    getZone(400, 400, 550, 400)
    getZone(550, 200, 550, 320)
    getZone(500, 200, 500, 400)

    # getZone(570, 400, 570, 200)
    # getZone(450, 320, 450, 400)
    # getZone(450, 400, 570, 400)
    # getZone(450, 400, 570, 400)
    # getZone(450, 320, 570, 320)

    # 4
    getZone(370, 400, 370, 200)
    getZone(370, 200, 320, 160)
    # getZone(270, 400, 270, 320)
    #
    getZone(270, 320, 370, 400)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(600, 600)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 2")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
