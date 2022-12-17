import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
window_size=700

def call_function(x1,y1,x2,y2,x3,y3):
    plot_triangle(x1,y1,x2,y2,x3,y3)
    choice=int(input("Enter 1 for translation\nEnter 2 for rotation\nEnter 3 for Scaling\nEnter 4 for Reflection\nEnter 5 for Shearing:"))
    if choice==1:
        translation(x1,y1,x2,y2,x3,y3)
    elif choice==2:
        rotation(x1,y1,x2,y2,x3,y3)
    elif choice==3:
        scaling(x1,y1,x2,y2,x3,y3)
    elif choice==4:
        reflection(x1,y1,x2,y2,x3,y3)
    elif choice==5:
        shearing(x1,y1,x2,y2,x3,y3)
    
def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-100,100,-100,100)

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

def rotation(x1,y1,x2,y2,x3,y3):
    theta=int(input("Enter angle of rotation: "))
    angle=((math.pi/180)*theta)
    x11=x1*math.cos(angle)-y1*math.sin(angle)
    y11=x1*math.sin(angle)+y1*math.cos(angle)
    x22=x2*math.cos(angle)-y2*math.sin(angle)
    y22=x2*math.sin(angle)+y2*math.cos(angle)
    x33=x3*math.cos(angle)-y3*math.sin(angle)
    y33=x3*math.sin(angle)+y3*math.cos(angle)
    glColor3f(0.0,1.0,0.1)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x11,y11)
    glVertex2f(x22,y22)
    glVertex2f(x33,y33)
    glEnd()
    glFlush()

def translation(x1,y1,x2,y2,x3,y3):
    tx=float(input("Enter change in x:"))
    ty=float(input("Enter change in y:"))
    glColor3f(0.0,0.0,1.0)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1+tx,y1+ty)
    glVertex2f(x2+tx,y2+ty)
    glVertex2f(x3+tx,y3+ty)
    glEnd()
    glFlush()

def scaling(x1,y1,x2,y2,x3,y3):
    sx=float(input("Enter scaling in x:"))
    sy=float(input("Enter scaling in y:"))
    glColor3f(0.0,1.0,0.0)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1*sx,y1*sy)
    glVertex2f(x2*sx,y2*sy)
    glVertex2f(x3*sx,y3*sy)
    glEnd()
    glFlush()

def reflection(x1,y1,x2,y2,x3,y3):
    c=int(input("Enter 1 for Refelction about x axis \nEnter 2 for Refelction about y axis \nEnter 3 for Refelction about origin\n Enter 4 for Refelction about x=y:"))
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

def shearing(x1,y1,x2,y2,x3,y3):
    c=int(input("Enter 1 for x shearing\nEnter 2 for y shearing\nEnter 3 for x-y shearing:"))
    if c==1:
        shx=int(input("Enter shear for x:"))
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1+shx*y1,y1)
        glVertex2f(x2+shx*y2,y2)
        glVertex2f(x3+shx*y3,y3)
        glEnd()
        glFlush()
    elif c==2:
        shy=int(input("Enter shear for y:"))
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,y1+shy*x1)
        glVertex2f(x2,y2+shy*x2)
        glVertex2f(x3,y3+shy*x3)
        glEnd()
        glFlush()
    elif c==3:
        shx=int(input("Enter shear for x:"))
        shy=int(input("Enter shear for y:"))
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1+shx*y1,y1+shy*x1)
        glVertex2f(x2+shx*y2,y2+shy*x2)
        glVertex2f(x3+shx*y3,y3+shy*x3)
        glEnd()
        glFlush()
        

def main():
    glutInit()
    x1=float(input("Enter x1 coordinate:"))
    y1=float(input("Enter y1 coordinate:"))
    x2=float(input("Enter x2 coordinate:"))
    y2=float(input("Enter y2 coordinate:"))
    x3=float(input("Enter x3 coordinate:"))
    y3=float(input("Enter y3 coordinate:"))
    glutCreateWindow("2D-TRANSFROMATIONS")
    glutInitWindowSize(window_size,window_size)
    glutDisplayFunc(lambda: call_function(x1,y1,x2,y2,x3,y3))
    ClearScreen()
    glutMainLoop()

main()
