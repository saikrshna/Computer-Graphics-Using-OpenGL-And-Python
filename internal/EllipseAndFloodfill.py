from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys

# for setting window size
window_size = 800
point_size = 5
sys.setrecursionlimit(1000000)


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
   
    gluOrtho2D(0,window_size,window_size,0)

def get_pixel(x, y):
    pixel = glReadPixels(x,window_size- y, 1, 1, GL_RGB, GL_FLOAT)
    return pixel[0][0]


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()

def translate_origin(x,y):
    return x+window_size/2,y+window_size/2

def draw_ellipse(xc,yc,xr,yr):
    x=0
    y=yr
    p=((yr*yr)-(xr*xr*yr)+(0.25*xr*xr))
    dx=(2*yr*yr*x)
    dy=(2*xr*xr*y)
    glColor3f(1.0,0.0,0.0)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    while dx<dy:
        plot_symmetric(x,y,xc,yc)
        if (p<0):
            x=x+1
            #glVertex2f(*translate_origin(xc+x,yc+y))
            dx=dx+(2*yr*yr)
            p=p+dx+(yr*yr)
        else:
            x=x+1
            y=y-1
            #glVertex2f(*translate_origin(xc+x,yc+y))
            dx=dx+(2*yr*yr)
            dy=dy-(2*xr*xr)
            p=p+dx-dy+(yr*yr)

    p2=((yr*yr)*(x+0.5)*(x+0.5))+((xr*xr)*(y -1)*(y-1))-((xr*xr*yr*yr))

    while y>0:
        plot_symmetric(x,y,xc,yc)
        if p2>0:
            y=y-1
            #glVertex2f(*translate_origin(xc+x,yc+y))
            dy=dy-(2*xr*xr)
            p2=p2+(xr*xr)-dy
        else:
            y=y-1
            x=x+1
            #glVertex2f(*translate_origin(xc+x,yc+y))
            dx=dx+(2*yr*yr)
            dy=dy-(2*xr*xr)
            p2=p2+dx-dy+(xr*xr)

    glEnd()
    glFlush()

def plot_symmetric(x,y,xc,yc):
    glVertex2f(*translate_origin(xc+x,yc+y))
    glVertex2f(*translate_origin(xc+x,yc-y))
    glVertex2f(*translate_origin(xc-x,yc+y))
    glVertex2f(*translate_origin(xc-x,yc-y))

def flood_fill(x, y, new_color, old_color):
    color = get_pixel(x, y)
    if all(color == old_color):
        set_pixel(x, y, new_color)
        flood_fill(x + point_size, y, new_color, old_color)
        flood_fill(x, y + point_size, new_color, old_color)
        flood_fill(x - point_size, y, new_color, old_color)
        flood_fill(x, y - point_size, new_color, old_color)


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(x,y)
        flood_fill(x, y, [0, 1, .5], get_pixel(x, y))


def main():
    glutInit()
    xc=int(input("Enter centre x coordinate of circle: "))
    yc=int(input("Enter centre y coordinate of circle: "))
    xr=int(input("Enter x radius of circle: "))
    yr=int(input("Enter y radius of circle: "))
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("Bresenham circle with floodfill")
    glutDisplayFunc(lambda: draw_ellipse(xc,yc,xr,yr))
    init()
    glutMouseFunc(mouse_click)
    glutMainLoop()

main()
