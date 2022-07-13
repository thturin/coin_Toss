"""Project Coin Toss
Fox and coin appear on the screen. Use the arrow keys to move the fox toward the coin. If the fox touches coin, 10 points given.
Duration of game 7 seconds and total score is shown

hacks and tweaks
extra time
go faster

have the coins move

"""

import pgzrun
import random

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100,100

coin = Actor("coin")
coin.pos = 200,200

def draw():
    screen.fill("dark green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time is up! Your final score is {}".format(score), color="black", topleft=(10,10))

def place_coin():
    coin.x = random.randint(0,WIDTH -20)
    coin.y = random.randint(0,HEIGHT-20)

def time_up():
    global game_over
    game_over = True

def update(): #built in pygame zero function. Once you've defined it, pygame zero will run it automatically
    global score

    if keyboard.left:
        fox.x -= 2
    elif keyboard.right:
        fox.x +=2
    elif keyboard.up:
        fox.y-=2
    elif keyboard.down:
        fox.y+=2

    coin_collected = fox.colliderect(coin) #if the fox touches the coin, return  true

    if coin_collected: #if the fox reaches the coin, add a point
        score+=10
        place_coin() #place coin somwhere



clock.schedule(time_up, 7.0) #runs the function time_up() 7 seconds after the game starts


place_coin()
pgzrun.go()