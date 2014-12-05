# Armin and Alex T. 12/4/14
# 'Teemo Asteroids'
# This is a quick outline of what the project might look like. Feel free to add, modify whatever you like
# See the hashtag? This is how you comment. If it doesn't have the symbol then a syntax error will show.
# If you have any questions lemme know, especially since you haven't worked with Python that much.

import random, math 
try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# globals- constant variables
# 500 by 500 for now. We can change it if screen too big/small.
width = 500
height = 500 
lives = 3
score = 0
# False- game not started. True- game started. Good for when 0 lives and game resets.
started = False

class imageInfo:
    def __init__():
        pass

# SPRITES

# background image
# spaceship
# missiles
# teemo asteroids images
# explosion

# SOUNDS

# soundtrack
# missles
# explosion
# ship's engine sound

# Confusing math section for sprite groups colliding etc...

class Ship:
    def __init__():
        pass

class Sprite:
    def __init__():
        pass

# Ship movements...easy section

# Reset UI when ship colliedes with asteroids, but still have lives

# Asteroids spawning

# Initialize section- basically main control of it all. To start everything up and running.
frame = simplegui.create_frame("Teemo Asteroids", width, height)
frame.start()

