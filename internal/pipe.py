from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
WINDOWSIZE=500
import math
b1,b2,b3,b4=300,200,100,10
len=0

def Init():
    glClearColor(0.0,0.0,0.0,0.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def pipe():
   
    glColor3f(0.5,0.2,0.9)
    glBegin(GL_POLYGON)
    glVertex2f(500,400)
    glVertex2f(0,400)
    glVertex2f(0,350)
    glVertex2f(500,350)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(100,350)
    glVertex2f(50,350)
    glVertex2f(50,300)
    glVertex2f(100,300)
    glEnd()
    glBegin(GL_TRIANGLES)
    glVertex2f(20,450)
    glVertex2f(130,450)
    glVertex2f(75,350)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(500,350)
    glVertex2f(400,350)
    glVertex2f(400,-500)
    glVertex2f(500,-500)
    glEnd()


def bowl():
    glColor3f(0.5,0.5,0.5)
    glLineWidth(7)
    glBegin(GL_LINES)
    glVertex2f(0,-300)
    glVertex2f(0,-500)
    glVertex2f(150,-300)
    glVertex2f(150,-500)
    glVertex2f(0,-500)
    glVertex2f(150,-500)
    glEnd()

def water():
    glColor3f(0.2,0.5,1.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b1)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b1
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b2)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b2
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b3)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b3
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()
    glBegin(GL_LINES)
    theta=0
    while theta<360:
        glVertex(75,b4)
        x1=10*math.cos(math.radians(theta))+75
        y1=10*math.sin(math.radians(theta))+b4
        glVertex2f(x1,y1)
        theta=theta+0.1
    glEnd()

def fill():
    glColor3f(0.2,0.5,1.0)
    glLineWidth(1)
    glBegin(GL_QUADS)
    glVertex2f(145,-490+len)
    glVertex2f(5,-490+len)
    glVertex2f(5,-490)
    glVertex2f(145,-490)
    glEnd()

def drawWaterPipe():
    glClear(GL_COLOR_BUFFER_BIT)
    pipe()
    bowl()
    water()
    fill()
    glutSwapBuffers()

def animate(temp):
    global b1,b2,b3,b4,len
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))
    
    if len<190:
        b1=b1-10
        b2=b2-10
        b3=b3-10
        b4=b4-10
        len=len+1
    if b1==-400:
        b1=40
    if b2==-400:
        b2=40
    if b3==-400:
        b3=40
    if b4==-400:
        b4=40

def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("Water filling")
    glutDisplayFunc(drawWaterPipe)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawWaterPipe)
    Init()
    glutMainLoop()

main()
