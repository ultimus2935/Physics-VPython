from vpython import *

scale = 1/1.7171875 # Some wierd scaling issue

scene.title = "4 Spring System"
scene.height = int(897*scale)
scene.width = int(1887*scale)
scene.background = vector(0.436, 0.436, 0.436)

t = 0
dt = 0.01

block = box(
    mass = 5, pos = vector(2.5, 2.5, 2.5),
    size = vector(0.5, 0.5, 0.5), 
    texture = 'block.jpg', shininess = 0,
    make_trail=True, trail_radius = 0.02,
    trail_color = color.blue
    )

block.vel = vector(0, 0, 0)
block.acc = vector(0, 0, 0)

def createBase(position, size):
    base = box(
        pos = position, size = size,
        texture = 'base.jpg', shininess = 0
    )
    
    return base

springs = []

springLen = 5
baseLen = 0.5
springConst = 50

# Base for attachment of springs
topBase = createBase(vector(0, springLen + baseLen, 0), vector(2, 2*baseLen, 2))
rightBase = createBase(vector(springLen + baseLen, 0, 0), vector(2*baseLen, 2, 2))
bottomBase = createBase(vector(0, -(springLen + baseLen), 0), vector(2, 2*baseLen, 2))
leftBase = createBase(vector(-(springLen + baseLen), 0, 0), vector(2*baseLen, 2, 2))

springs.append(topBase)
springs.append(rightBase)
springs.append(bottomBase)
springs.append(leftBase)

# Points where spring are attached
topBase.attach = vector(0, springLen, 0) 
rightBase.attach = vector(springLen, 0, 0)
bottomBase.attach = vector(0, -springLen, 0)
leftBase.attach = vector(-springLen, 0, 0)

for spring in springs: 
    spring.helix = helix(
        pos = spring.attach,
        axis = block.pos - spring.attach,
        radius = 0.2, thickness = 0.05,
        coils = 10, color = color.red
    )

def blockAcc():
    acc = vector(0, 0, 0)
    for spring in springs:
        radius = block.pos - spring.attach
        acc += (springLen - mag(radius))*norm(radius)
        
    acc *= springConst/block.mass
    return acc

while True:
    rate(1/dt)
    
    block.acc = blockAcc()
    block.vel += block.acc*dt
    block.pos += block.vel*dt
    
    for spring in springs: spring.helix.axis = block.pos - spring.attach
    
    t += dt