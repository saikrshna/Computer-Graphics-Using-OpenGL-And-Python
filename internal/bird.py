from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
WINDOWSIZE=500
tx=-350
ty=0
x=0
y=90
angle=0
dir=0

def Init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def head():
    glColor3f(1.0,0.9,0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(100+tx,30+ty)
    glVertex2f(100+tx,-30+ty)
    glVertex2f(200+tx,0+ty)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(-200+tx,30+ty)
    glVertex2f(-200+tx,-30+ty)
    glVertex2f(-100+tx,1+ty)
    glEnd()

def eyes():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    theta=0
    while(theta<6.28):
        glVertex2f(100+tx,50+ty)
        x1=10*math.cos(theta)
        y1=10*math.sin(theta)
        glVertex2f(100+x1+tx,50+y1+ty)
        theta=theta+0.01
    glEnd()
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_LINES)
    theta=0
    while(theta<6.28):
        glVertex2f(100+tx,50+ty)
        x1=5*math.cos(theta)
        y1=5*math.sin(theta)
        glVertex2f(100+x1+tx,50+y1+ty)
        theta=theta+0.01
    glEnd()


def body():
    glColor3f(0.8,0.3,0.1)
    glBegin(GL_LINES)
    theta=0
    while(theta<6.28):
        glVertex2f(tx,ty)
        x1=150*math.cos(theta)
        y1=100*math.sin(theta)
        glVertex2f(x1+tx,y1+ty)
        theta=theta+0.01
    glEnd()

def wings():
    glColor3f(1.0,0.9,0.1)
    glBegin(GL_TRIANGLES)
    glVertex2f(40+tx,ty)
    glVertex2f(-40+tx,ty)
    glVertex2f(0+tx,-y+ty)
    glEnd()

def drawBird():
    glClear(GL_COLOR_BUFFER_BIT)
    head()
    body()
    eyes()
    wings()
    glFlush()
    glutSwapBuffers()
    
def animate(temp):
    global x,y,tx,ty,angle,dir
    glutPostRedisplay()
    glutTimerFunc(int(5000/30),animate,int(0))
    y=-y
    if tx<350:
        tx=tx+5
    else:
        tx=-350
    ty=200*(math.sin(angle))
    angle+=0.1
    

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Bird")
    glutDisplayFunc(drawBird)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawBird)
    Init()
    glutMainLoop()

main()
