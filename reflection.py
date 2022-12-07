import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def call_function(x1,y1,x2,y2,x3,y3):
    plot_triangle(x1,y1,x2,y2,x3,y3)
    reflection(x1,y1,x2,y2,x3,y3)

def plot_triangle(x1,y1,x2,y2,x3,y3):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glFlush()

def reflection(x1,y1,x2,y2,x3,y3):
    c=int(input("Enter 1 for Refelction about x axis\nEnter 2 for Refelction about y axis\nEnter 3 for Refelction about origin\nEnter 4 for Refelction about x=y:"))
    if c==1:
        glColor3f(0.0,0.0,1.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,-y1)
        glVertex2f(x2,-y2)
        glVertex2f(x3,-y3)
        glEnd()
        glFlush()

    elif c==2:
        glColor3f(0.0,0.0,1.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,y1)
        glVertex2f(-x2,y2)
        glVertex2f(-x3,y3)
        glEnd()
        glFlush()

    elif c==3:
        glColor3f(0.0,0.0,1.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,-y1)
        glVertex2f(-x2,-y2)
        glVertex2f(-x3,-y3)
        glEnd()
        glFlush()

    elif c==4:
        glColor3f(0.0,0.0,1.0)
        glPointSize(10)
        x1,y1=y1,x1
        x2,y2=y2,x2
        x3,y3=y3,x3
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glVertex2f(x3,y3)
        glEnd()
        glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    x1=float(input("Enter x1 coordinate: "))
    y1=float(input("Enter y1 coordinate: "))
    x2=float(input("Enter x2 coordinate: "))
    y2=float(input("Enter y2 coordinate: "))
    x3=float(input("Enter x3 coordinate: "))
    y3=float(input("Enter y3 coordinate: "))
    glutCreateWindow("Reflection - Triangle")
    glutInitWindowSize(500, 500)
    glutDisplayFunc(lambda: call_function(x1,y1,x2,y2,x3,y3))
    ClearScreen()
    glutMainLoop()

main()
