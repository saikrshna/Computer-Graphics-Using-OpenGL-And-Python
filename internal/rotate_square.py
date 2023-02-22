from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import*
import sys
import math
WINDOWSIZE=500
angle=0.0

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def square(angle):
    glBegin(GL_QUADS)
    glVertex2f(100*math.cos(math.radians(angle))+100*math.sin(math.radians(angle)),-100*math.sin(math.radians(angle))+100*math.cos(math.radians(angle)))
    glVertex2f(-100*math.cos(math.radians(angle))+100*math.sin(math.radians(angle)),-(-100)*math.sin(math.radians(angle))+100*math.cos(math.radians(angle)))
    glVertex2f(-100*math.cos(math.radians(angle))+-100*math.sin(math.radians(angle)),-(-100)*math.sin(math.radians(angle))+(-100)*math.cos(math.radians(angle)))
    glVertex2f(100*math.cos(math.radians(angle))+-100*math.sin(math.radians(angle)),-100*math.sin(math.radians(angle))+(-100)*math.cos(math.radians(angle)))
    glEnd()

def drawSquare():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.9,0.5,1.0)
    square(angle)
    glutSwapBuffers()

def animate(temp):
    global angle
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if angle>359:
        angle=0.0
    else:
        angle=angle+1

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Rotation of Square")
    glutDisplayFunc(drawSquare)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawSquare)
    ClearScreen()
    glutMainLoop()

main()
