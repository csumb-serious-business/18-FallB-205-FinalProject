# === funcs in explain =======================================================#

def getColor(pixel):
    """
    pixel: the pixel you want to extract the color from
    returns: the color of the pixel Takes a Pixel and returns the Color object at that pixel.

    Example:
    def getDistanceFromRed(pixel):
        red = makeColor(255, 0, 0)
        col = getColor(pixel)
        return distance(red, col)

    This takes in a pixel and returns that pixel's color's distance from red.
    """


def setColor(pixel, color):
    """"
    pixel: the pixel you want to set the color of
    color: the color you want to set the pixel to

    Takes in a pixel and a color, and sets the pixel to the given color.

    Example:
    def makeMoreBlue(pixel):
        myBlue = getBlue(pixel) + 60
        newColor = makeColor(getRed(pixel), getGreen(pixel), myBlue)
        setColor(pixel, newColor)

    This will take in a pixel and increase its level of blue by 60.
    """


def getRed(pixel):
    """
    pixel: the pixel you want to get the amount of red from
    returns: the red value of the pixel Takes a Pixel object and
    returns the value (between 0 and 255) of the amount of redness
    in that pixel.

    Example:
    def getHalfRed(pixel):
        red = getRed(pixel)
        return red / 2

    This takes in a pixel and returns the amount of red in that pixel divided by two.
    """


def getGreen(pixel):
    """
    pixel: the pixel you want to get the amount of green from
    returns: the green value of the pixel Takes a Pixel object and
    returns the value (between 0 and 255) of the amount of greenness
    in that pixel.

    Example:
    def getHalfGreen(pixel):
        green = getGreen(pixel)
        return green / 2

    This takes in a pixel and returns the amount of green in that pixel divided by two.
    """


def getBlue(pixel):
    """
    pixel: the pixel you want to get the amount of blue from
    returns: the blue value of the pixel Takes a Pixel object and
    returns the value (between 0 and 255) of the amount of blueness
    in that pixel.

    Example:
    def getHalfBlue(pixel):
        blue = getBlue(pixel)
        return blue / 2

    This takes in a pixel and returns the amount of blue in that pixel divided by two.
    """


def setRed(pixel, redValue):
    """
    pixel: the pixel you want to set the red value of
    redValue: a number (0 - 255) for the new red value of the pixel
    Takes in a Pixel object and a value (between 0 and 255) and
    sets the redness of that pixel to the given value.

    Example:
        def zeroRed(pixel):
        setRed(pixel, 0)

    This will take in a pixel and set its amount of red to 0.
    """


def setGreen(pixel, greenValue):
    """
    pixel: the pixel you want to set the green value of
    greenValue: a number (0 - 255) for the new green value of the pixel
    Takes in a Pixel object and a value (between 0 and 255) and
    sets the greenness of that pixel to the given value.

    Example:
        def zeroGreen(pixel):
        setGreen(pixel, 0)

    This will take in a pixel and set its amount of green to 0.
    """


def setBlue(pixel, blueValue):
    """
    pixel: the pixel you want to set the blue value of
    blueValue: a number (0 - 255) for the new blue value of the pixel
    Takes in a Pixel object and a value (between 0 and 255) and
    sets the blueness of that pixel to the given value.

    Example:
        def zeroBlue(pixel):
        setBlue(pixel, 0)

    This will take in a pixel and set its amount of blue to 0.
    """


def getX(pixel):
    """
    pixel: the pixel you want to find the x-coordinate of
    returns: the x-coordinate of the pixel

    Takes in a pixel object and returns the x position of where that pixel is in the picture.

    Example:
    def getHalfX(pixel):
        pos = getX(pixel)
        return pos / 2

    This will take in a pixel and return half of its x-coordinate.
    """


def getY(pixel):
    """
    pixel: the pixel you want to find the x-coordinate of
    returns: the y-coordinate of the pixel

    Takes in a pixel object and returns the y position of where that pixel is in the picture.

    Example:
    def getHalfY(pixel):
        pos = getY(pixel)
        return pos / 2

    This will take in a pixel and return half of its y-coordinate.
    """


# === entities in globals but not explain ====================================#


class Pixel:  # TODO add all properties & methods
    def __init__(self):
        pass
