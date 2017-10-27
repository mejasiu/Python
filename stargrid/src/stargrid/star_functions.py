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
    #print("Star Width " + str(star_width))

    # Using the screen size we can figure out how many stars can fit on the screen
    # settings.screen_height
    # settings.screen_width

    # Calculate X axis
    gapBetweenStarsX = star_width / 2
    #print("Gap between stars " + str(gapBetweenStars))
    # have to subtract the edges from the full screen
    available_spaceX = settings.screen_width - (2 * gapBetweenStarsX)
    number_of_StarsinRow = int(
        available_spaceX / (gapBetweenStarsX + star_width))
    #print("available_spaceX " + str(available_spaceX))
    #print("number_of_StarsinRow " + str(number_of_StarsinRow))

    # Calculate Y Axis
    gapBetweenStarsY = star_height / 2
    available_spaceY = settings.screen_height - (2 * gapBetweenStarsY)
    numberRowsOnScreen = int(
        available_spaceY / (gapBetweenStarsY + star_height))
    for star_row_number in range(numberRowsOnScreen):
        star_y_position = gapBetweenStarsY + \
            (gapBetweenStarsY + star_height) * star_row_number
        for star_number in range(number_of_StarsinRow):
            # Create stars
            star = Star(settings, screen)
            # Set star Y axis
            star.y = star_y_position
            # find the X location of the star
            # The first multiples the gap by the star width to find the position by multipling it to the star number.
            # Then the gap is added
            star.x = gapBetweenStarsX + \
                (gapBetweenStarsX + star_width) * star_number
            #print(str(star_number) + " star.x " + str(star.x))
            star.rect.x = star.x
            star.rect.y = star.y
            stars.add(star)
