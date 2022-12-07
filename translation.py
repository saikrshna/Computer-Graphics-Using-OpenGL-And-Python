import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def call_function(x1,y1,x2,y2,x3,y3):
    plot_triangle(x1,y1,x2,y2,x3,y3)
    translation(x1,y1,x2,y2,x3,y3)

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

def translation(x1,y1,x2,y2,x3,y3):
    tx=float(input("Enter change in x: "))
    ty=float(input("Enter change in y: "))
    glColor3f(0.0,0.0,1.0)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1+tx,y1+ty)
    glVertex2f(x2+tx,y2+ty)
    glVertex2f(x3+tx,y3+ty)
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
    glutCreateWindow("Translation - Triangle")
    glutInitWindowSize(500, 500)
    glutDisplayFunc(lambda: call_function(x1,y1,x2,y2,x3,y3))
    ClearScreen()
    glutMainLoop()

main()
