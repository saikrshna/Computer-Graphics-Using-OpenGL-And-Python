import OpenGL.GL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import *

WINDOWSIZE=500

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def plot_points(x1,y1,x2,y2):
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5)
    glColor3f(1.0,0.0,0.0)
    deltax=x2-x1
    deltay=y2-y1
    m=deltay/deltax
    glBegin(GL_POINTS)
    glVertex2f(x1,y1)
    while y2!=y1 and x2!=x1:
        if(m<1):
          x1=x1+1
          y1=y1+m
          glVertex2f(round(x1),round(y1))
        elif(m>1):
          x1=x1+(1/m)
          y1=y1+1
          glVertex2f(round(x1),round(y1))
        elif(m==1):
          x1=x1+1
          y1=y1+1
          glVertex2f(round(x1),round(y1))
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    x1=int(input("Enter x1 value: "))
    y1=int(input("Enter y1 value: "))
    x2=int(input("Enter x2 value: "))
    y2=int(input("Enter y2 value: "))
    glutCreateWindow("DDA")
    glutInitWindowPosition(0,0)
    glutInitWindowPosition(WINDOWSIZE,WINDOWSIZE)
    glutDisplayFunc(lambda: plot_points(x1,y1,x2,y2))
    ClearScreen()
    glutMainLoop()

main()
