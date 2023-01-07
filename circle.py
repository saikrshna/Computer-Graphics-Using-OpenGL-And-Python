from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOWSIZE=700

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def circle(xc,yc,radius):
    x=0
    y=radius
    p=(1-radius)
    glPointSize(2)
    glColor3f(1.0,1.0,0.0)
    glBegin(GL_POINTS)
    glVertex2f(x+xc,y+yc)
    while x<y:
        if (p<0):
            x=x+1
            glVertex2f(x+xc,y+yc)
            p=p+2*x+1
        elif (p>=0):
            x=x+1
            y=y-1
            glVertex2f(x+xc,y+yc)
            p=p+2*x+1-2*y
        symmetry(x,y,xc,yc)
    glEnd()
    glFlush()

def symmetry(x,y,xc,yc):
    glVertex2f(-x+xc,y+yc)
    glVertex2f(x+xc,-y+yc)
    glVertex2f(-x+xc,-y+yc)
    glVertex2f(y+xc,x+yc)
    glVertex2f(-y+xc,x+yc)
    glVertex2f(y+xc,-x+yc)
    glVertex2f(-y+xc,-x+yc)

def main():
    glutInit()
    xc=int(input("Enter centre x coordinate of circle: "))
    yc=int(input("Enter centre y coordinate of circle: "))
    radius=int(input("Enter radius of circle: "))
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Mid-Point Circle")
    glutDisplayFunc(lambda: circle(xc,yc,radius))
    ClearScreen()
    glutMainLoop()

main()
