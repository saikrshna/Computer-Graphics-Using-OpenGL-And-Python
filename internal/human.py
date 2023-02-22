from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOWSIZE=500
GLOBAL_Y=0
dir=0

def Init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def human():
    glColor3f(0.8,0.3,0.1)
    glBegin(GL_LINES)
    theta=0
    xc=0
    yc=250
    while theta<6.28:
        glVertex2f(xc,yc)
        x1=100*math.cos(theta)+xc
        y1=100*math.sin(theta)+yc
        glVertex(x1,y1)
        theta+=0.01
    glEnd()

    glLineWidth(20)
    glBegin(GL_LINES)
    glVertex2f(0,250)
    glVertex2f(0,-100)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,-100)
    glVertex2f(-150,-200)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0,-100)
    glVertex2f(150,-200)
    glEnd()

    glColor3f(1.0,1.0,1.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(23,260)
    glVertex2f(-23,260)
    glVertex2f(0,200)
    glVertex2f(20,200)
    glVertex2f(-20,200)
    glEnd()

def hand():
    glColor3f(0.8,0.3,0.1)
    glLineWidth(20)
    glBegin(GL_LINES)
    glVertex2f(0,100)
    glVertex2f(-150,GLOBAL_Y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0,100)
    glVertex2f(150,GLOBAL_Y)
    glEnd()

def drawHuman():
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    human()
    hand()
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_Y,dir
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    if dir==0:
        GLOBAL_Y=GLOBAL_Y+1
        if GLOBAL_Y>150:
            dir=1
    elif dir==1:
        GLOBAL_Y=GLOBAL_Y-1
        if GLOBAL_Y==0:
            dir=0

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Human")
    glutDisplayFunc(drawHuman)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawHuman)
    Init()
    glutMainLoop()

main()
