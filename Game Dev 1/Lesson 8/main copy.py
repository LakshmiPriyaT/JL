import pgzrun
import random

WIDTH = 600
HEIGHT = 500

alien = Actor("alien")
#alien.pos = 50,50
alien.x = 50
alien.y = 50

cat = Actor("cat")
cat.pos = WIDTH/2,HEIGHT/2


speed = 5
score = 0
game_over = False

def draw():
   #screen.fill("red")
   screen.blit("background",(0,0))
   
   cat.draw()
   alien.draw()
   #screen.draw.text(ms,(300,50))
   screen.draw.text(f"Score: {score}",(100,50))

   if game_over:
       screen.fill("red")
       screen.draw.text("Game Over",(250,200))
       screen.draw.text(f"Score: {score}",(250,250))

def update():
    global score
    if keyboard.up:
        alien.y -= speed
    if keyboard.down:
        alien.y += speed
    if keyboard.left:
        alien.x -= speed
    if keyboard.right:
        alien.x += speed
    if alien.colliderect(cat):
        cat.x = random.randint(50,WIDTH-50)
        cat.y = random.randint(50,HEIGHT-50)
        score +=1

def exit():
    global game_over
    game_over = True

clock.schedule(exit,20)

pgzrun.go()
