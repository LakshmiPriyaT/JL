import pgzrun
import random

WIDTH = 500
HEIGHT = 500


def draw():
        screen.fill((0,0,0))
        #w = 100
        #h = 400
        ra = 20
        for i in range(20):
                r = random.randint(0,255)
                g = random.randint(0,255)
                b = random.randint(0,255)
                #r1 = Rect((0,0),(w,h))
                #r1.center = WIDTH/2,HEIGHT/2
                #screen.draw.rect(r1,(r,g,b))
                screen.draw.circle((WIDTH/2,HEIGHT/2),ra,(r,g,b))
                ra += 20
                #w += 10
                #h -= 10
   


pgzrun.go()