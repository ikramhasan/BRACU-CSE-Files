from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

STROKE = 5
WIDTH = 640
HEIGHT = 480
WINDOW_TITLE = b"LAB 4"

# Defining region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

x_max = 400
y_max = 300
x_min = 100
y_min = 50

# Function to compute region code for a point(x, y)


def computeCode(x, y):
    code = INSIDE
    if x < x_min:      # to the left of rectangle
        code |= LEFT

        print(f"Here in left since x is: {x}")
    elif x > x_max:    # to the right of rectangle
        code |= RIGHT
        print(f"Here in right since x is: {x}")

    if y < y_min:      # below the rectangle
        code |= BOTTOM
        print(f"Here in bottom since y is: {y}")
    elif y > y_max:    # above the rectangle
        code |= TOP
        print(f"Here in top since y is: {y}")

    return code


# Implementing Cohen-Sutherland algorithm
def cohenSutherlandClip(x1, y1, x2, y2):

    # Compute region codes for P1, P2
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False
    count = 0
    print(f"Code 1: {code1}")
    print(f"Code 2: {code2}")

    print(f"Code 1 in binary: {bin(code1)}")
    print(f"Code 2 in binary: {bin(code2)}")

    while True:
        # If both endpoints lie within rectangle
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # If both endpoints are outside rectangle
        elif (code1 & code2) != 0:
            break

        # Some segment lies within the rectangle
        else:

            # Line Needs clipping
            # At least one of the points is outside,
            # select it
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            # using formulas y = y1 + slope * (x - x1),
            # x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

                # point is above the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_max - y1) / (y2 - y1)
                y = y_max

            elif code_out & BOTTOM:

                # point is below the clip rectangle
                x = x1 + (x2 - x1) * \
                    (y_min - y1) / (y2 - y1)
                y = y_min

            elif code_out & RIGHT:

                # point is to the right of the clip rectangle
                y = y1 + (y2 - y1) * \
                    (x_max - x1) / (x2 - x1)
                x = x_max

            elif code_out & LEFT:

                # point is to the left of the clip rectangle
                y = y1 + (y2 - y1) * \
                    (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

            print(f"Updated Code 1: {code1}")
            print(f"Updated Code 2: {code2}")

            print(f"Updated Code 1 in binary: {bin(code1)}")
            print(f"Updated Code 2 in binary: {bin(code2)}")
        count += 1

    if accept:
        print("Line accepted from %.2f, %.2f to %.2f, %.2f" % (x1, y1, x2, y2))
        setColor("GREEN")
        drawLine(x1, y1, x2, y2)
        print(f"Number of times it requires to clip: {count}")

    else:
        print("Line rejected")
        setColor("RED")
        drawLine(x1, y1, x2, y2)
        print(f"Number of times it requires to clip: {count}")


def drawLine(x1, y1, x2, y2):
    glPointSize(STROKE)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
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
    drawLine(x_min, y_min, x_max, y_min)
    drawLine(x_max, y_min, x_max, y_max)
    drawLine(x_max, y_max, x_min, y_max)
    drawLine(x_min, y_max, x_min, y_min)
    cohenSutherlandClip(207, 253, 184, 85)
    print("---------------------------------------------------")
    cohenSutherlandClip(350, 280, 200, 60)
    print("---------------------------------------------------")
    cohenSutherlandClip(50, 150, 80, 300)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(WINDOW_TITLE)
glutDisplayFunc(showScreen)

glutMainLoop()
