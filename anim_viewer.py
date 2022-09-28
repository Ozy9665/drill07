from pico2d import *
from random import *
open_canvas()
character = load_image('ataho_motion.png')


def handshake():
    frame = 0
    for x in range(30, 770+1, 10):
        clear_canvas()
        character.clip_draw(frame * 50, 192, 50, 64, x, 150, 150, 150)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.05)
        get_events()


def motion_drink():
    frame = 0
    for x in range(770, 30-1, -10):
        clear_canvas()
        character.clip_draw(frame*50, 128, 50, 64, x, 150, 120, 120)
        update_canvas()
        frame = (frame+1) % 4
        delay(0.05)
        get_events()


def surprise():
    frame = 0
    for x in range(30, 770+1, 10):
        clear_canvas()
        character.clip_draw(frame*50, 64, 50, 64, x, 150, 150, 150)
        update_canvas()
        frame = (frame+1) % 4
        delay(0.05)
        if((frame%4)==0):
            delay(0.3)
        get_events()


def take_off():
    frame = 1
    for x in range(0, 20+1, 1):
        clear_canvas()
        rx = randint(100, 500)
        ry = randint(100,300)
        character.clip_draw(frame*50, 0, 50, 64, rx, ry, 150, 150)
        update_canvas()
        frame = (frame + 1) % 2
        delay(0.25)
        get_events()


handshake()
motion_drink()
surprise()
take_off()


close_canvas()
