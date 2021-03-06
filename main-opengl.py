from OpenGL.GL.shaders import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import sys
import itertools
from random import choice

# x, y, z
position = [-2.75,2.25,-2.75]
orientation = [0,0,0]

angle = 0

name = 'opengl_with_python'
heights = []

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800,600)
    glutCreateWindow(name)
    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPos = [-10.,75.,100.,1.]
    lightZeroCol = [1.,1.,1.,1.] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroCol)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(specialKeyboard)
    glMatrixMode(GL_PROJECTION)
    dist = math.sqrt(1/3.0)
    for n in range(0,27):
        heights.append(choice([0.5,0.75,1]))
    gluPerspective(60.0,1.25,0.09,1000.0)
    glMatrixMode(GL_MODELVIEW);
    gluLookAt(-2.75, 2.25, -2.75, 0.0,  0.0,  0.0,  0.0,  1.0,  0.0);

    fs = glCreateShader(GL_FRAGMENT_SHADER)
    #fsource = open("bokeh.glsl").read()
    fsource = open("blur.glsl").read()
    glShaderSource(fs,fsource)
    glCompileShader(fs)
    log = glGetShaderInfoLog(fs)
    if log: print 'Fragment Shader: ', log
    pr = glCreateProgram()
    glAttachShader(pr,fs)
    glLinkProgram(pr)
 #   glUseProgram(pr)
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    #glMatrixMode(GL_MODELVIEW);
    #gluLookAt(position[0], position[1], position[2], 0.0,  0.0,  0.0,  0.0,  1.0,  0.0);
    #glMatrixMode(GL_PROJECTION)
    #glPushMatrix()
    #glRotated(orientation[0], 1.0, 0.0, 0.0);
    #glRotated(orientation[1], 0.0, 1.0, 0.0);
    #glRotated(orientation[2], 0.0, 0.0, 1.0);
    #glPopMatrix()

    #glTranslatef(position[0],position[1],position[2])

    color1 = [0., 1., 1., 1.]
    glMaterialfv(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE,color1)
    glPushMatrix()
    glBegin(GL_QUADS)
    glVertex3f(-1.,-1.,-1.)
    glVertex3f(-1.,-1.,3.)
    glVertex3f(3.,-1.,3.)
    glVertex3f(3.,-1.,-1.)
    glEnd()
    glPopMatrix()
    glFlush()

    #creates all permutations of -1,0,1 across three elements
    #use this to create a 3x3 grid of cubes
    n = 0
    for i in list(itertools.product(range(-1,2),repeat=3)):
        color = [(i[0]*i[0]),(i[1]*i[1]),(i[2]*i[2]),1.]
        glMaterialfv(GL_FRONT_AND_BACK,GL_DIFFUSE,color)
        glPushMatrix()
        glTranslatef(i[0],0,i[2])
        rect(0.5,heights[n])
        n = n + 1
        glPopMatrix()

    glutSwapBuffers()
    return

def keyboard(key,x,y):
    if (key == 'q'):
        quit()
    if (key == 'w'):
        position[1] = position[1] + 0.05
        print position[1]

def specialKeyboard(key,x,y):
    fraction = 0.1

def rect(width,height):
    glBegin(GL_QUADS)

    #bottom
    glNormal3d(0,0,0)
    glVertex3f((width/2),0.,(-width/2))
    glVertex3f((-width/2),0.,(-width/2))
    glVertex3f((-width/2),0.,(width/2))
    glVertex3f((width/2),0.,(width/2))

    #side far
    glNormal3d(0,0,0)
    glVertex3f((width/2),0.,(width/2))
    glVertex3f((width/2),height,(width/2))
    glVertex3f((width/2),height,(-width/2))
    glVertex3f((width/2),0.,(-width/2))

    #top
    glNormal3d(0,1,0)
    glVertex3f((width/2),height,(-width/2))
    glVertex3f((-width/2),height,(-width/2))
    glVertex3f((-width/2),height,(width/2))
    glVertex3f((width/2),height,(width/2))

    #side near
    glNormal3d(1,0,-1)
    glVertex3f((-width/2),0.,(width/2))
    glVertex3f((-width/2),height,(width/2))
    glVertex3f((-width/2),height,(-width/2))
    glVertex3f((-width/2),0.,(-width/2))

    #side front
    #leftmost side when looking in this perspective
    glNormal3d(0,0,-1)
    glVertex3f((width/2),0.,(-width/2))
    glVertex3f((width/2),height,(-width/2))
    glVertex3f((-width/2),height,(-width/2))
    glVertex3f((-width/2),0.,(-width/2))

    #side back
    glNormal3d(0,0,0)
    glVertex3f((width/2),0.,(width/2))
    glVertex3f((width/2),height,(width/2))
    glVertex3f((-width/2),height,(width/2))
    glVertex3f((-width/2),0.,(width/2))
    glEnd()

if __name__ == '__main__': main()
