from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import*
import sys
import math
import time

WINDOWSIZE=500
x1,y1=0,400
x2,y2=100,100
x3,y3=400,0
x4,y4=100,-100
x5,y5=0,-400
x6,y6=-100,-100
x7,y7=-400,0
x8,y8=-100,100
dir=0
scale=1

def ClearScreen():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def star(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8):
    global scale
    glBegin(GL_LINES)
    glVertex2f(x1*scale,y1*scale)
    glVertex2f(x2*scale,y2*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2*scale,y2*scale)
    glVertex2f(x3*scale,y3*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3*scale,y3*scale)
    glVertex2f(x4*scale,y4*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x4*scale,y4*scale)
    glVertex2f(x5*scale,y5*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x5*scale,y5*scale)
    glVertex2f(x6*scale,y6*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x6*scale,y6*scale)
    glVertex2f(x7*scale,y7*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x7*scale,y7*scale)
    glVertex2f(x8*scale,y8*scale)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x8*scale,y8*scale)
    glVertex2f(x1*scale,y1*scale)
    glEnd()


def drawstar():
    global x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10)
    star(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8)
    glFlush()
    glutSwapBuffers()

def animate(temp):
    global scale,dir
    glutPostRedisplay()
    if(dir==0):
        scale-=0.1
        if(scale<=0):
            dir=1
    elif(dir==1):
        scale+=0.1
        if(scale>=1):
            dir=0
    glutTimerFunc(int(5000/60),animate,int(0))


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Blinking Star")
    glutDisplayFunc(drawstar)
    glutTimerFunc(0,animate,0)
    ClearScreen()
    glutMainLoop()

main()
