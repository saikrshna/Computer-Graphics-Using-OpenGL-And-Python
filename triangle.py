import OpenGL
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def ClearScreen():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-1.0,1.0,-1.0,1.0)
	
x1=float(input("Enter x1 coordinate(value between -1 and 1): "))
y1=float(input("Enter y1 coordinate(value between -1 and 1): "))
x2=float(input("Enter x2 coordinate(value between -1 and 1): "))
y2=float(input("Enter y2 coordinate(value between -1 and 1): "))
x3=float(input("Enter x3 coordinate(value between -1 and 1): "))
y3=float(input("Enter y3 coordinate(value between -1 and 1): "))
	
def plot_points():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,1.0,1.0)
	glPointSize(10.0)
	glBegin(GL_TRIANGLES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glEnd()
	glFlush()
	
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(50,50)
glutCreateWindow("Triangle")
glutDisplayFunc(plot_points)
glutMainLoop()
