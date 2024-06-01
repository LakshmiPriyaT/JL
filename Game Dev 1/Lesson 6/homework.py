import pgzrun
from random import randint

RADIUS = 30



def draw():
    r = 255
    g = 0
    b = randint(120, 255)

    radius = RADIUS

    for i in range(20):
        
        
        screen.draw.circle((300,300), radius, (r, g, b))

        r -= 10
        g += 10

        radius +=10


pgzrun.go()