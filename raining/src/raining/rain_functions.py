'''
Created on Oct 31, 2017

@author: jaroszyn
'''
import sys

from random import randint
from rain_drop import Drop
from rain_settings import Settings


def makeItRain(settings, screen, raining_drops, drop_color, drop_speed):
    """This function will create rain that fall from the sky"""
    # This will have to be a function outside of Rain_drop because I would have to have a
    # Rain drop object to be able to make it rain, but since the make_it_rain object already
    # Creates droplets than it does not need to be here.
    # I will set the X value randomly.  I will also set the Y value randomly as well so that
    # all the rain comes down at a different moment
    rain_drop_count = countRainDrops(raining_drops)
    print("count " + str(rain_drop_count))
    if (rain_drop_count < settings.drop_count):
        sum = settings.drop_count - rain_drop_count
        print(sum)
        for drops in range(sum):
            # make the droplet
            droplet = Drop(settings, screen, drop_color, drop_speed)
            # Set the position
            droplet.position_x = randint(0, settings.screen_width)
            droplet.position_y = randint(-settings.screen_height, 0)
            droplet.draw_rain_drop()
            raining_drops.add(droplet)
            print("Added a drop")


def drawDroppetMoveDownScreen(raining_drops):
    for droplets in raining_drops:
        droplets.move_droplet()
        droplets.draw_rain_drop()


def removeDroppletsFromMemory(raining_drops, settings):
    for droplets in raining_drops:
        if droplets.position_y > settings.screen_height:
            raining_drops.remove(droplets)
            print("Removed droplet from memory")


def countRainDrops(raining_drops):
    count = 0
    for droplets in raining_drops:
        count += 1
    return count
