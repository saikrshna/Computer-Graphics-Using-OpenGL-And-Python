import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0,-1.0,1.0)# left, right, bottom, top

def plot_rectangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POLYGON)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.7,0.5)
    glVertex2f(-0.7,-0.5)
    glVertex2f(0.5,-0.5)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Polygon - Rectangle")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutDisplayFunc(plot_rectangle)
    clearScreen()
    glutMainLoop()

main()
