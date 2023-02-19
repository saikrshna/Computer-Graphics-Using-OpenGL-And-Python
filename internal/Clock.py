from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOWSIZE=700
X1=0
Y1=200
BOB_RADIUS=300
angle1=0.0
X2=0
Y2=270
angle2=0.0

def Init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def drawCircle():
    global BOB_RADIUS
    i=0.0
    glColor3f(0.0,0.0,0.0)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)
    for i in range(0,361,1):
        glVertex2f(BOB_RADIUS*math.cos(math.radians(i)),BOB_RADIUS*math.sin(math.radians(i)))
    glEnd()
    glFlush()

def second_hand():
    glColor3f(0.5,0.5,0.7)
    global X1
    global Y1
    global angle1
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(X1*math.cos(math.radians(angle1))+Y1*math.sin(math.radians(angle1)),-X1*math.sin(math.radians(angle1))+Y1*math.cos(math.radians(angle1)))
    glEnd()

def minute_hand():
    glColor3f(0.7,0.4,0.8)
    global X2
    global Y2
    global angle2
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(X2*math.cos(math.radians(angle2))+Y2*math.sin(math.radians(angle2)),-X2*math.sin(math.radians(angle2))+Y2*math.cos(math.radians(angle2)))
    glEnd()

def drawClock():
    glClear(GL_COLOR_BUFFER_BIT)
    drawCircle()
    second_hand()
    minute_hand()
    glutSwapBuffers()

def animate(temp):
    global X1
    global Y1
    global angle1
    global X2
    global Y2
    global angle2
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    if angle1<360:
        angle1+=0.1
    else:
        angle1=0
    if angle2<360:
        angle2+=1
    else:
        angle2=0
    


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Clock")
    glutDisplayFunc(drawClock)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawClock)
    Init()
    glutMainLoop()
    

main()
