# === funcs in explain =======================================================#
def distance(color1, color2):
    """
    color1: the first color you want compared
    color2: the second color you want compared
    returns: a floating point number representing the Cartesian distance between the colors

    Takes two Color objects and returns a single number representing the distance between the colors.
    The red, green, and blue values of the colors are taken as a point in (x, y, z) space,
    and the Cartesian distance is computed.

    Example:
    def showDistRedAndBlue():
        red = makeColor(255, 0, 0)
        blue = makeColor(0, 0, 255)
        print distance(red, blue)

    This will print the distance between red and blue, 360.62445840513925.
    """


def makeColor(*colors):
    """
    red: the amount of red you want in the color (or a Color object you want to duplicate)
    green: the amount of green you want in the color (optional)
    blue: the amount of blue you want in the picture (optional)
    returns: the color made from the inputs
    Takes three integer inputs for the red, green, and blue components (in order) and returns a color object.
    If green and blue are omitted, the red value is used as the intensity of a gray color.
    Also it works with only a color as input and returns a new color object with the same RGB values as the original.

    Examples:
    def makeCyan():
        return makeColor(0, 255, 255)

    This will return the color cyan.

    def makeGrey(amount):
        return makeColor(amount, amount, amount)

    This will take in an amount and make a grey color based on that.

    def duplicateColor(color):
    return makeColor(amount, amount, amount)

    This will take in a color and return a duplicate color object.
    """


def makeDarker(color):
    """
    color: the color you want to darken
    returns: the new, darker color

    Takes a color and returns a slightly darker version of the original color.

    Example:
    def makeMuchDarker(color):
        return makeDarker(makeDarker(makeDarker(color)))

    Takes in a color and returns a much darker version of it by calling makeDarker three times.
    """


def makeLighter(color):
    """
    color: the color you want to lighten
    returns: the new, lighter color Takes a color and returns a slightly lighter version of the original color.
    This does the same thing as makeBrighter(color).

    Example:
    def makeMuchLighter(color):
        return makeLighter(makeLighter(makeLighter(color)))

    Takes in a color and returns a much lighter version of it by calling makeLighter three times.
    """


def pickAColor():
    """
    returns: the color chosen in the dialog box
    Opens a color chooser to let the user pick a color and returns it.
    Takes no input.

    Example:
    def makeColoredPicture():
        color = pickAColor()
        return makeEmptyPicture(100, 100, color)

    This opens up a color selector dialog, then the user picks a color,
    and the function returns a 100x100 picture of the chosen color.
    """


def getColorWrapAround():
    """
    returns: a boolean (1/true or 0/false) for the current value of ColorWrapAround
    Takes no input, and returns the current value of ColorWrapAround.
    If it is true, color values will wrap-around (356 mod 256 = 100);
    if false, color values lower than 0 will be forced to 0 and higher than 255 forced to 255.
    Default is false.
    If setColorWrapAround has not been used since re-saving options or restarting JES,
    This will return the value in the JES options menu.
    Otherwise, it will return the last flag specified in setColorWrapAround(flag).

    Example:
    def setColorWithoutWrap(pixel, r, g, b):
        oldWrapVal = getColorWrapAround()
        setColorWrapAround(0)
        setColor( pixel, makeColor(r, g, b) )
        setColorWrapAround(oldWrapVal)

    This will temporarily disable colorWrapAround (if enabled), change the pixel's color,
    and then restore the colorWrapAround to the initial value.
    """


def setColorWrapAround(flag):
    """
    flag: a boolean (1/true or 0/false) for the new ColorWrapAround value
    Default is false.

    Takes a boolean as input.
    If flag is true, color values will wrap-around (356 mod 256 = 100);
    if false, color values lower than 0 will be forced to 0 and higher than 255 forced to 255.
    This only temporarily changes the value.
    ColorWrapAround will be restored to its value defined in the JES options menu by:
    Running setColorWrapAround(bool) where bool is the default value, re-saving options,
    or by restarting JES.

    Example:
    def setColorWithoutWrap(pixel, r, g, b):
        oldWrapVal = getColorWrapAround()
        setColorWrapAround(0)
        setColor( pixel, makeColor(r, g, b) )
        setColorWrapAround(oldWrapVal)

    This will temporarily disable colorWrapAround (if enabled), change the pixel's color,
    and then restore the colorWrapAround to the initial value.
    """


# === entities in globals but not explain ====================================#
def makeBrighter(color):
    """
    color: the color you want to lighten
    returns: the new, lighter color Takes a color and returns a slightly lighter version of the original color.
    (Same as makeLighter)

    Example:
    def makeMuchBrighter(color):
        return makeBrighter(makeBrighter(makeBrighter(color)))

    Takes in a color and returns a much lighter version of it by calling makeBrighter three times.
    """


# media.color
class Color:  # TODO add all properties & methods
    def __init__(self, red, green, blue):
        """
        create a new color
        :param red: red component (between 0-255)
        :param green: green component (between 0-255)
        :param blue: blue component (between 0-255)
        """
