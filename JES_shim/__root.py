from _colors import Color

# --- Color constants --------------------------------------------------------#
black = Color(0, 0, 0)
blue = Color(0, 0, 255)
cyan = Color(0, 255, 255)
darkGray = Color(64, 64, 64)
gray = Color(128, 128, 128)
green = Color(0, 255, 0)
lightGray = Color(192, 192, 192)
magenta = Color(255, 0, 255)
orange = Color(255, 200, 0)
pink = Color(255, 175, 175)
red = Color(255, 0, 0)
white = Color(255, 255, 255)
yellow = Color(255, 255, 0)


# --- present in JES Movies, Pictures & Sound --------------------------------#
def explore(someMedia):
    """
    someMedia: A Picture, Sound, or Movie that you want to view using Media Tools.

    Example:
    def exploreAPicture():
        file = pickAFile()
        pic = makePicture(file)
        explore(pic)

    This creates a Picture object from a file and opens it in the Media Tools.
    """
