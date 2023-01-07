import OpenGL.GL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

WINDOWSIZE=500

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOWSIZE,WINDOWSIZE,-WINDOWSIZE,WINDOWSIZE)

def bresenham(x1,y1,x2,y2):
    deltay=y2-y1
    deltax=x2-x1
    glPointSize(5)
    glColor3f(0.7,0.5,0.2)
    glBegin(GL_POINTS)
    glVertex2f(x1,y1)
    if deltax>deltay:
      p = 2*deltay - deltax
      while y2!=y1 and x2!=x1:
        if p>0:
            x1=x1+1
            y1=y1+1
            p=p+2*deltay-2*deltax
            glVertex2f(x1,y1)
        elif p<0:
            x1=x1+1
            y1=y1
            p=p+2*deltay
            glVertex2f(x1,y1)
    else:
      p = 2*deltax - deltay
      while y2!=y1 and x2!=x1:
        if p>0:
            x1=x1+1
            y1=y1+1
            p=p+2*deltax-2*deltay
            glVertex2f(x1,y1)
        elif p<0:
            x1=x1
            y1=y1+1
            p=p+2*deltax
            glVertex2f(x1,y1)
    glEnd()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    x1=int(input("Enter x1 value: "))
    y1=int(input("Enter y1 value: "))
    x2=int(input("Enter x2 value: "))
    y2=int(input("Enter y2 value: "))
    glutCreateWindow("Bresenham Line Drawing")
    glutInitWindowPosition(0,0)
    glutInitWindowSize(WINDOWSIZE,WINDOWSIZE)
    glutDisplayFunc(lambda: bresenham(x1,y1,x2,y2))
    ClearScreen()
    glutMainLoop()

main()
