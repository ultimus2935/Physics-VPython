from vpython import *

scale = 1/1.7171875 # Some wierd scaling issue

scene.title = "Pendulum"
scene.height = int(897*scale)
scene.width = int(1887*scale)
scene.background = vector(0.436, 0.436, 0.436)

t = 0
dt = 0.01

g = vector(0, -9.81, 0)

pendLen = 15 # Defualt length of pendulum string
pendConst = mag(g)/pendLen # Pendulum constant
baseLen = 0.3 

bob = sphere(
    mass = 2, radius = 0.75, pos = vector(0, 0, 0),
    texture = 'bob.jpg', shininess = 0,
    make_trail = False, trail_radius = 0.02,
    trail_color = color.blue
)

bob.angle = pi/6
bob.pos = rotate(vector(0, -pendLen, 0), bob.angle)
bob.angacc = 0
bob.angvel = 0

bob.make_trail = True

base = box(
    pos = vector(0, baseLen, 0), size = vector(3, 2*baseLen, 3),
    texture = 'base.jpg', shininess = 0
)

string = cylinder(
    mass = 0, pos = vector(0, 0, 0),
    axis = bob.pos, radius = 0.05,
    color = color.red, shininess = 0
)

scene.camera.follow(box(pos = vector(0, -pendLen/2, 0), visible = False))

while True:
    rate(1/dt)
    
    bob.angacc = -pendConst*sin(bob.angle)
    bob.angvel += bob.angacc*dt
    bob.angle += bob.angvel*dt
    bob.pos = rotate(vector(0, -pendLen, 0), bob.angle)
    
    string.axis = bob.pos
    
    t += dt