import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

start = 0
end = 0
total = 0


no_of_sats = 10
sats = []
lines = []
next = 0
for i in range(no_of_sats):
    satellite = Actor("satellite")
    satellite.x = randint(50, WIDTH-50)
    satellite.y = randint(50, HEIGHT - 50)
    sats.append(satellite)
start = time()
def draw():
    screen.blit("background",(0,0))
    number = 1
    for satellite in sats:
        satellite.draw()
        screen.draw.text(str(number),(satellite.x,satellite.y+20))
        number +=1
    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))
    #print(start)
    total = time() - start
    #print(total)
    #screen.draw.text(str(round(total,2)),(50,50))
    if next < no_of_sats:
        total = time() - start
        screen.draw.text(str(round(total,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total,1)), (10,10), fontsize=30)

def on_mouse_down(pos):
    global lines, next,sats

    if sats[next].collidepoint(pos):
        if next:
            lines.append((sats[next-1].pos,sats[next].pos))
            print(lines)
        next +=1
    else:
        lines = []
        next = 0





pgzrun.go()