import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_point(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_line(i, j, x, y):
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2f(i, j)
    glVertex2f(x, y)
    glEnd()


def draw_house():
    glBegin(GL_LINES)
    # glBegin(GL_LINES)
    # glVertex2f(100,30)
    # glVertex2f(390, 30)

    # glVertex2f(100, 30)
    # glVertex2f(99, 230)

    # glVertex2f(390, 30)
    # glVertex2f(390, 230)

    # glVertex2f(99,230)
    # glVertex2f(390, 230)

    # glVertex2f(99, 230)
    # glVertex2f(245, 380)

    # glVertex2f(390, 230)
    # glVertex2f(245, 380)

    # glVertex2f(120, 160)
    # glVertex2f(119,210)

    # glVertex2f(120, 160)
    # glVertex2f(170, 160)

    # glVertex2f(170, 160)
    # glVertex2f(170, 210)

    # glVertex2f(119, 210)
    # glVertex2f(170, 210)

    # glVertex2f(320, 160)
    # glVertex2f(319, 210)

    # glVertex2f(320, 160)
    # glVertex2f(370, 160)

    # glVertex2f(370, 160)
    # glVertex2f(370, 210)

    # glVertex2f(319, 210)
    # glVertex2f(370, 210)

    # glVertex2f(199, 170)
    # glVertex2f(290, 170)

    # glVertex2f(199, 170)
    # glVertex2f(200,30)

    # glVertex2f(290, 170)
    # glVertex2f(290, 30)
    # glEnd()

    # glBegin(GL_POINTS)
    # glVertex2f(280,80)
    # glEnd()

    glVertex2f(200, 30)
    glVertex2f(200, 100)

# top
    glVertex2f(200, 100)
    glVertex2f(300, 100)

# left
    glVertex2f(300, 100)
    glVertex2f(300, 30)
 # right
    glVertex2f (300, 30)
    glVertex2f (200, 30)

          # glVertex2f (10, -50)



    # door
    glColor3f(0.0,0.0,1.0) 
    glBegin(GL_POLYGON)
    # left

    glVertex2f (120,30)
    glVertex2f (120, 100)

# top
    glVertex2f (120, 100)
    glVertex2f (170, 100)

# right
    glVertex2f (170, 100)
    glVertex2f (170, 30)

 # bottom
    glVertex2f (120, 30)
    glVertex2f (170, 30)

          # glVertex2f (10, -50)


    # Triangle

    glColor3f(0.0,1.0,0.0) 
    glBegin(GL_POLYGON)
# bottom

    glVertex2f (20, 200)
    glVertex2f (320, 200)

          # top
    glVertex2f (200, 310)
    glVertex2f (320, 200)

        # left
    glVertex2f (20, 200)
    glVertex2f (200, 310)
    # glEnd()


          # glVertex2i (10, -50)


def iterate():
    glViewport(0, 0, 640, 480)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 400, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    print("screen")
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)
    draw_house()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(640, 480) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 1") #window name
glutDisplayFunc(show_screen)

glutMainLoop()