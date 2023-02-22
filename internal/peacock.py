from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOWSIZE=500
xr=250
yr=50
xl=-250
yl=50
angle1=0
angle2=0
dir=0

def Init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def body():
    glColor3f(0.2,0.8,0.3)
    theta=0
    glPointSize(3)
    glBegin(GL_POINTS)
    while theta<6.28:
        x1=150*math.cos(theta)
        y1=100*math.sin(theta)
        glVertex2f(x1,y1)
        theta=theta+0.01
    glEnd()

    glColor3f(0.8,0.2,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-70,-80)
    glVertex2f(0,-30)
    glVertex2f(70,-80)
    glVertex2f(0,-200)
    glEnd()

    glColor3f(1.0,1.0,1.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(60,20)
    glVertex2f(-60,20)
    glEnd()

def wings():
    glLineWidth(2)
    glColor3f(0.5,0.8,0.9)
    glBegin(GL_LINES)
    glVertex2f(0,100)
    glVertex2f(xr*math.cos(math.radians(angle1))-yr*math.sin(math.radians(angle1)),xr*math.sin(math.radians(angle1))+yr*math.cos(math.radians(angle1)))
    glVertex2f(0,100)
    glVertex2f(xl*math.cos(math.radians(angle2))+yl*math.sin(math.radians(angle2)),-xl*math.sin(math.radians(angle2))+yl*math.cos(math.radians(angle2)))
    glEnd()

def drawPeacock():
    body()
    wings()
    glutSwapBuffers()

def animate(temp):
    global angle1,angle2,dir
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    if dir==0:
        angle1=angle1+1
        angle2=angle2+1
        if angle1==angle2==90:
            dir=1
            glClear(GL_COLOR_BUFFER_BIT)
    elif dir==1:
        angle1=angle1-1
        angle2=angle2-1
        if angle1==angle2==0:
            dir=0
            glClear(GL_COLOR_BUFFER_BIT)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Peacock")
    glutDisplayFunc(drawPeacock)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawPeacock)
    Init()
    glutMainLoop()

main()
