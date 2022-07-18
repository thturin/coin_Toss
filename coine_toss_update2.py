"""Project Coin Toss
Fox and coin appear on the screen. Use the arrow keys to move the fox toward the coin. If the fox touches coin, 10 points given.
Duration of game 7 seconds and total score is shown

hacks and tweaks
extra time
go faster


countdown clock
add seconds to the countdown clock when you get a coin
WHAT IS THE PROBLEM ONCE YOU DO THE COUNTDOWN CLOCK CORRECTLY? ---> THE GAME ENDS AT THE INITIAL TIME GIVEN FOR TIME_UP

have the coins move <--- with the countdown clock created, the game because very easy because everytime you get a coin,
the clock increases by 3 seconds. find a way to make it harder to get the coins. You can make the actor go slower
Maybe change up the functionality of the keyboard clicks (left if right and right is left etc.) or have the coin move?
"""

import pgzrun, random, pygame

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
time_left = 7
timer = 0
timer2_check = 0
timer2 = 0

fox = Actor("fox")
fox.pos = 100,100

coin = Actor("coin")
coin.pos = 200,200

def draw():
    global timer
    screen.fill("dark green")
    fox.draw()
    coin.draw()

    screen.draw.text("Score: "+ str(score), color="black", topleft=(10,10))

    #timer = int(pygame.time.get_ticks() / 1000) # gives you the time in ms since the program was started

    screen.draw.text("Time Remaining: {}".format(time_left), color="black", topright=(290, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time is up! Your final score is {}".format(score), color="black", topleft=(10,10))

def place_coin():
    coin.x = random.randint(0,WIDTH -20)
    coin.y = random.randint(0,HEIGHT-20)

def time_up():
    global game_over
    game_over = True

def update_time_left():
    global time_left
    if time_left:
        if coin_collected
        time_left -= 1
    else:
        time_up()

clock.schedule_interval(update_time_left,1.0)

def update(): #built in pygame zero function. Once you've defined it, pygame zero will run it automatically
    global score
    global time_left

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
        time_left +=3

"""
the clock.schedule(callback, delay) <- the delay variable will not be changed since when running this code, it will be called and put into memory initially with original time_up value. 
It will not be called again. This is why we put the clock.schedule() method into the update() function itself. PG Zero calls this function 60x every 1 second so what we do is unschedule and schedule it
each iteration which means the updated time_left variable is set as a parameter for the newly called clock.schedule() method
"""


#clock.schedule(time_up,time_left) #runs the function time_up() 7 seconds after the game starts


place_coin()
pgzrun.go()