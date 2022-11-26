import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def clearScreen():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	gluOrtho2D(-1.0, 1.0,-1.0,1.0)

def plot_lines(x1,y1,x2,y2):
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(0.0,1.0,0.0)
	glPointSize(7.0)
	glBegin(GL_LINES)
	glVertex2f(x1, y1)
	glVertex2f(x2, y2) 
	glEnd()
	glFlush()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("LINE")
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	print("Please enter value between -1 and 1 (eg: x=0.5 y=-0.4).")
	x1=float(input("Enter the x1 coordinate:"))
	y1=float(input("Enter the y1 coordinate:"))
	x2=float(input("Enter the x2 coordinate:"))
	y2=float(input("Enter the y2 coordinate:"))
	glutDisplayFunc(lambda: plot_lines(x1,y1,x2,y2))
	clearScreen()
	glutMainLoop()
	
	
main()
