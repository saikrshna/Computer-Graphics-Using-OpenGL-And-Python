from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOWSIZE=500
xc=-400
yc=0
GLOBAL_ANGLE=0

def Init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def Ball():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3f(1.0,0.0,1.0)
    theta=0
    while theta<6.28:
        glVertex2f(xc,yc)
        x=100*math.cos(theta)+xc
        y=100*math.sin(theta)+yc
        theta=theta+0.01
        glVertex2f(x,y)
    glEnd()
    glBegin(GL_LINES)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(xc,yc)
    x1=100*math.sin(GLOBAL_ANGLE)+xc
    y1=100*math.cos(GLOBAL_ANGLE)+yc
    glVertex2f(x1,y1)
    glEnd()

def drawBall():
    Ball()
    glutSwapBuffers()

def animate(temp):
    global xc,yc,GLOBAL_ANGLE
    glutPostRedisplay()
    glutTimerFunc(int(500/60),animate,int(0))
    if xc<400 :
        xc=xc+1
        GLOBAL_ANGLE=GLOBAL_ANGLE+0.01
    else:
        xc=-400
        yc=0


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Ball")
    glutDisplayFunc(drawBall)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawBall)
    Init()
    glutMainLoop()

main()
