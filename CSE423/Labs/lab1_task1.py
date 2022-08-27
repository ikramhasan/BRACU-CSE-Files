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


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    print("screen")
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0.0, 1.0, 0.0)

    for i in range(50):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        draw_point(x, y)

    glColor3f(1.0, 0.0, 0.0)
    # x, y -> -x, y
    #draw_line(350, 350, -350, 350)
    # x, y, -> -x, -y
    #draw_line(350, 350, -350, -350)
    #draw_line(350, -350, 350, -350)
    #draw_line(350, -350, -350, 350)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Lab 1 Task 1") #window name
glutDisplayFunc(show_screen)

glutMainLoop()