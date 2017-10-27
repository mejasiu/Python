'''
Created on Oct 25, 2017

@author: jaroszyn
'''
import sys
from star import Star


def createStarfeild(stars, screen, settings):
    """This will create a line of stars across the screen
    Will need to figure out how many stars can fit on the screen in one row
    """
    # Figure out the size of the star by creating it
    star = Star(settings, screen)
    star_width = star.rect.width
    star_height = star.rect.height

    # Using the screen size we can figure out how many stars can fit on the screen
    # settings.screen_height
    # settings.screen_width

    # Calculate X axis
    gapBetweenStarsX = star_width / 2
    number_of_StarsinRow = calcStarsInRow(
        gapBetweenStarsX, settings, star_width)

    # Calculate Y Axis
    gapBetweenStarsY = star_height / 2
    numberRowsOnScreen = calcStarsInColumn(
        gapBetweenStarsY, settings, star_height)

    for star_row_number in range(numberRowsOnScreen):
        for star_number in range(number_of_StarsinRow):
            # Create stars
            star = Star(settings, screen)
            # Set star Y axis
            star.y = calcStar_Y_Position(
                gapBetweenStarsY, star_height, star_row_number)
            # find the X location of the star
            # The first multiples the gap by the star width to find the position by multipling it to the star number.
            # Then the gap is added
            star.x = gapBetweenStarsX + \
                (gapBetweenStarsX + star_width) * star_number
            star.rect.x = star.x
            star.rect.y = star.y
            stars.add(star)


def calcStarsInRow(gapBetweenStarsX, settings, star_width):
    available_spaceX = settings.screen_width - (2 * gapBetweenStarsX)
    return int(available_spaceX / (gapBetweenStarsX + star_width))


def calcStarsInColumn(gapBetweenStarsY, settings, star_height):
    available_spaceY = settings.screen_height - (2 * gapBetweenStarsY)
    return int(available_spaceY / (gapBetweenStarsY + star_height))


def calcStar_Y_Position(gapBetweenStarsY, star_height, star_row_number):
    return gapBetweenStarsY + (gapBetweenStarsY + star_height) * star_row_number
