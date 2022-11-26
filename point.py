import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def plot_points(x,y):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,1.0,0.0)
	glPointSize(10.0)
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("POINT")
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	print("Please enter value between -1 and 1 (eg: x=0.5 y=-0.4).")
	x=float(input("Enter the x coordinate:"))
	y=float(input("Enter the y coordinate:"))
	glutDisplayFunc(lambda: plot_points(x,y))
	clearScreen()
	glutMainLoop()
	
main()
