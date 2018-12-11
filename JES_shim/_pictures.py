from __root import black


# === funcs in explain =======================================================#
def addArc(picture, startX, startY, width, height, start, angle, color=black):
    """
    picture: the picture you want to draw the arc on
    startX: the x-coordinate of the center of the arc
    startY: the y-coordinate of the center of the arc width: the width of the arc
    height: the height of the arc
    start: the start angle of the arc in degrees
    angle: the angle of the arc relative to start in degrees
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, (x,y) coordinates, width, height, two integer angles, and (optionally) a color as input.
    Adds an outline of an arc starting at (x,y) at an initial angle of "start" with the given width and height.
    The angle of the arc itself is "angle", which is relative to "start."

    Examples:
    def addSemiCircle(picture, startX, startY, radius, start):
        addArc(picture, startX, startY, radius, radius, start, 180)

    This will take in a picture, start coordinates, a radius length, and a starting angle
    and call addArc to draw a black arc with equal width and height.

    def addBlueSemiCircle(picture, startX, startY, radius, start):
        addArc(picture, startX, startY, radius, radius, start, 180, blue)

    This will take in a picture, start coordinates, a radius length,
    and a starting angle and call addArc to draw a blue arc with equal width and height.
    """


def addArcFilled(picture, startX, startY, width, height, start, angle, color=black):
    """
    picture: the picture you want to draw the arc on
    startX: the x-coordinate of the center of the arc
    startY: the y-coordinate of the center of the arc width: the width of the arc
    height: the height of the arc
    start: the start angle of the arc in degrees
    angle: the angle of the arc relative to start in degrees
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, (x,y) coordinates, width, height, two integer angles, and (optionally) a color as input.
    Adds an outline of an arc starting at (x,y) at an initial angle of "start" with the given width and height.
    The angle of the arc itself is "angle", which is relative to "start."

    Examples:
    def addFilledSemiCircle(picture, startX, startY, radius, start):
        addArcFilled(picture, startX, startY, radius, radius, start, 180)

    This will take in a picture, start coordinates, a radius length, and a starting angle
    and call addArcFilled to draw a filled black arc with equal width and height.

    def addBlueFilledSemiCircle(picture, startX, startY, radius, start):
        addArcFilled(picture, startX, startY, radius, radius, start, 180, blue)

    This will take in a picture, start coordinates, a radius length,
    and a starting angle and call addArc to draw a filled blue arc with equal width and height.
    """


def addLine(picture, startX, startY, endX, endY, color=black):
    """
    picture: the picture you want to draw the line on
    startX: the x position you want the line to start
    startY: the y position you want the line to start
    endX: the x position you want the line to end
    endY: the y position you want the line to end
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, a starting (x, y) position (two numbers),
    and an ending (x, y) position (two more numbers, four total), and (optionally) a color as input.

    Adds a line from the starting point to the ending point in the picture.

    Examples:
    def drawVertical(picture):
        addLine(picture, 100, 20, 100, 250)

    This will take in a picture and draw a black vertical line on it from (100,20) to (100,250)

    def drawDiagonal(picture):
        addLine(picture, 0, 15, 100, 115, blue)

    This will take in a picture and draw a blue diagonal line on it from (0,15) to (100, 115).
    """


def addOval(picture, startX, startY, width, height, color=black):
    """
    picture: the picture you want to draw the oval on
    startX: the x-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    startY: the y-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    width: the width of the oval height: the height of the oval
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input.

    Adds a filled oval of the given dimensions using the (x,y)
    as the upper left corner of the bounding rectangle.

    Examples:
    def addCircleFilled(picture, startX, startY, radius):
        addOvalFilled(picture, startX, startY, radius, radius)

    This will take in a picture, start coordinates,
    and a radius length and call addOvalFilled
    to draw a solid oval with equal width and height.

    def addBlueCircleFilled(picture, startX, startY, radius):
        addOvalFilled(picture, startX, startY, radius, radius, blue)

    This will take in a picture, start coordinates, and a radius length
    and call addOvalFilled to draw a solid blue oval with equal width and height.
    """


def addOvalFilled(picture, startX, startY, width, height, color=black):
    """
    picture: the picture you want to draw the oval on
    startX: the x-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    startY: the y-coordinate of the upper left-hand corner of the bounding rectangle of the oval
    width: the width of the oval height: the height of the oval
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input.

    Adds a filled oval of the given dimensions using the (x,y)
    as the upper left corner of the bounding rectangle.

    Examples:
    def addCircleFilled(picture, startX, startY, radius):
        addOvalFilled(picture, startX, startY, radius, radius)

    This will take in a picture, start coordinates,
    and a radius length and call addOvalFilled
    to draw a solid oval with equal width and height.

    def addBlueCircleFilled(picture, startX, startY, radius):
        addOvalFilled(picture, startX, startY, radius, radius, blue)

    This will take in a picture, start coordinates, and a radius length
    and call addOvalFilled to draw a solid blue oval with equal width and height.
    """


def addRect(picture, startX, startY, width, height, color=black):
    """
    picture: the picture you want to draw the rectangle on
    startX: the x-coordinate of the upper left-hand corner of the rectangle
    startY: the y-coordinate of the upper left-hand corner of the rectangle
    width: the width of the rectangle height: the height of the rectangle
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total), and (optionally) a color as input.
    Adds a rectangular outline of the specified dimensions using the (x,y) as the upper left corner.

    Examples:
    def addSquare(picture, startX, startY, edge):
        addRect(picture, startX, startY, edge, edge)

    This will take in a picture, start coordinates,
    and an edge length and call addRect to draw a black rectangle with all sides the same length.

    def addBlueSquare(picture, startX, startY, edge):
        addRect(picture, startX, startY, edge, edge, blue)

    This will take in a picture, start coordinates,
    and an edge length and call addRect to draw a blue rectangle with all sides the same length.
    """


def addRectFilled(picture, startX, startY, width, height, color=black):
    """
    picture: the picture you want to draw the rectangle on
    startX: the x-coordinate of the upper left-hand corner of the rectangle
    startY: the y-coordinate of the upper left-hand corner of the rectangle
    width: the width of the rectangle height: the height of the rectangle
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, a starting (x, y) position (two numbers),
    a width and height (two more numbers, four total),
    and (optionally) a color as input.

    Adds a filled rectangle of the specified dimensions
    using the (x,y) as the upper left corner.

    Examples:
    def addSquareFilled(picture, startX, startY, edge):
        addRectFilled(picture, startX, startY, edge, edge)

    This will take in a picture, start coordinates,
    and an edge length and call addRectFilled to draw a solid black rectangle with all sides the same length.

    def addBlueSquareFilled(picture, startX, startY, edge):
        addRectFilled(picture, startX, startY, edge, edge, blue)

    This will take in a picture, start coordinates,
    and an edge length and call addRectFilled to draw a solid blue rectangle with all sides the same length.
    """


def addText(picture, xpos, ypos, text, color=black):
    """
    picture: the picture you want to add the text to
    xpos: the x-coordinate where you want to start writing the text
    ypos: the y-coordinate where you want to start writing the text
    text: a string containing the text you want written
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, an x position and a y position (two numbers),
    and some text as a string, which will get drawn into the picture,
    in the specified color.

    Examples:
    def addDate(picture):
        str = "Today is the first day of the rest of your life."
        addText(picture, 0, 0, str)

    This takes in a picture and adds a black date stamp to
    the upper left corner.

    def addHappyBirthday(picture):
        str = "Happy Birthday!!!"
        addText(picture, 0, 0, str, orange)

    This takes in a picture and adds an orange
    Happy Birthday message to the upper left corner.
    """


def addTextWithStyle(picture, xpos, ypos, text, style, color=black):
    """
    picture: the picture you want to add the text to
    xpos: the x-coordinate where you want to start writing the text
    ypos: the y-coordinate where you want to start writing the text
    text: a string containing the text you want written
    style: a font created using makeStyle()
    color: the color you want to draw in (optional)
    Default color is black.

    Takes a picture, an x position and a y position (two numbers),
    and some text as a string, which will get drawn into the picture,
    in the given font style and specified color.

    Examples:
    def addDate(picture):
        import java.awt.Font as Font
        str = "Today is the first day of the rest of your life."
        myFont = makeStyle("Comic Sans", Font.BOLD, 96)
        addTextWithStyle(picture, 0, 0, str, myFont)

    This takes in a picture and adds a black date stamp to
    the upper left corner in Size 96 bold Comic Sans.

    def addHappyBirthday(picture):
        import java.awt.Font as Font
        str = "Happy Birthday!!!"
        myFont = makeStyle("Wingdings", Font.ITALICS, 24)
        addText(picture, 0, 0, str, orange)

    This takes in a picture and adds an orange
    Happy Birthday message to the upper left corner
    in Size 24 italcized Wingdings.
    """


def copyInto(smallPicture, bigPicture, startX, startY):
    """
    smallPicture: the picture to paste into the big picture
    bigPicture: the picture to be modified
    startX: the X coordinate of where to place the small picture on the big one
    startY: the Y coordinate of where to place the small picture on the big one

    Takes two pictures, a x position and a y position as input,
    and modifies bigPicture by copying into it as much of smallPicture as will fit,
    starting at the x,y position in the destination picture.

    Example:
    def addBorder(picture, borderWidth, borderHeight, borderColor):
        canvas = makeEmptyPicture( getWidth(picture) + 2*borderWidth, getHeight(picture) + 2*borderHeight, borderColor )
        copyInto(picture, canvas, borderWidth, borderHeight)
        return canvas

    This will take in a picture, and return a new picture which is the original plus a border of specified size and color.
    """


def duplicatePicture(pic):
    """
    pic: the picture that you want to duplicate
    returns: a new picture object with the same image as the original

    Takes a picture as input and returns a new picture object with the same image as the original.

    Example:
    file = pickAFile()
    mypic = makePicture(file)
    copyofmypic = duplicatePicture(mypic)

    This opens up a file chooser, makes a Picture object using the chosen file,
    and then creates a second Picture object by copying the first one.
    """


def getHeight(picture):
    """
    picture: the picture you want to get the height of
    returns: the height of the picture Takes a picture as input and returns its length
    in the number of pixels top-to-bottom in the picture.

    Example:
    def howTall(picture)
        height = getHeight(picture)
        print "The picture is " + str(height) + " pixels tall."

    This takes in a picture and prints a descriptive message about its height.
    """


def getWidth(picture):
    """
    picture: the picture you want to get the width of
    returns: the width of the picture Takes a picture as input and returns its length
    in the number of pixels left-to-right in the picture.

    Example:
    def howWide(picture)
        width = getWidth(picture)
        print "The picture is " + str(width) + " pixels wide."

    This takes in a picture and prints a descriptive message about its width.
    """


def getPixel(picture, xpos, ypos):
    """
    picture: the picture you want to get the pixel from
    xpos: the x-coordinate of the pixel you want
    ypos: the y-coordinate of the pixel you want

    Takes a picture, an x position and a y position (two numbers),
    and returns the Pixel object at that point in the picture. (Same as getPixelAt)

    Example:
        def getUpperLeftPixel(picture)
        return getPixel(picture, 0, 0)

    This will take in a picture and return the pixel in the upper left-hand corner, (0, 0).
    """


def getPixels(picture):
    """
    picture: the picture you want to get the pixels from
    returns: a list of all the pixels in the picture

    Takes a picture as input and returns the sequence of Pixel objects in the picture.

    Example:
    def getTenthPixel(picture):
        pixels = getPixels(picture)
        return pixels[9]

    This takes in a picture and returns the 10th pixel in that picture.
    """


def getPixelAt(picture, xpos, ypos):
    """
    picture: the picture you want to get the pixel from
    xpos: the x-coordinate of the pixel you want
    ypos: the y-coordinate of the pixel you want

    Takes a picture, an x position and a y position (two numbers),
    and returns the Pixel object at that point in the picture.

    Example:
    def getUpperLeftPixel(picture)
        return getPixelAt(picture, 0, 0)

    This will take in a picture and return the pixel in the upper left-hand corner, (0, 0).
    """


def makePicture(path):
    """
    path: the name of the file you want to open as a picture
    returns: a picture object made from the file Takes a filename as input,
    reads the file, and creates a picture from it. Returns the picture.

    Example:
    def makePictureSelector():
        file = pickAFile()
        return makePicture(file)

    This function will open a file selector box and then
    return the picture object made from that file.
    """


def makeEmptyPicture(width, height, color='white'):
    """
    width: the width of the empty picture
    height: height of the empty picture
    color: background color of the empty picture (optional)
    returns: a new picture object with all the pixels set to the specified color

    Makes a new "empty" picture and returns it to you.
    The width and height must be between 0 and 10000. Default color is white.

    Examples:
    def makeEmptySquare(edge):
        return makeEmptyPicture(edge, edge)

    This will take in an edge length and call makeEmptyPicture to
    return an empty white picture all sides the same length.

    def makeEmptyBlueSquare(edge):
        return makeEmptyPicture(edge, edge, blue)

    This will take in an edge length and call makeEmptyPicture to
    return an empty blue picture all sides the same length.
    """


# Note JES puts this in the wrong place
def makeStyle(fontName, emphasis, size):
    """
    fontName: the name of the font you want in the style
    (sansSerif, serif, mono)
    emphasis: the type of emphasis you want in the style
    (italic, bold, italic + bold, plain)
    size: the size of the font you want in the style

    returns: the style made from the inputs Takes a font name, emphasis,
     and size in points as input.
     Returns a Font object with the given parameters.

    Example:
    def makeBold12ptSerifFont():
        return makeStyle(sansSerif, bold, 12)

    This takes no input and will return a Font that is
    san-serif, bold, and of size 12pt.
    """


def show(picture):
    """
    picture: the picture you want to see Shows the picture provided as input.

    Example:
    def openShow():
        file = pickAFile()
        pic = makePicture(file)
        show(pic)

    This will let the user choose which file to be shown and show it.
    """


def repaint(picture):
    """
    picture: the picture you want to repaint
    Repaints the picture if it has been opened in a window from show(picture),
    otherwise a new window will be opened.

    Example:
    def openShowAddOval():
        file = pickAFile()
        pic = makePicture(file)
        show(pic)
        addOval(pic, 0, 0, getWidth(pic), getHeight(pic))
        repaint(pic)

    This will let the user choose which file to be shown.
    Then a black oval will be drawn over the image, and it will be repainted.
    """


def writePictureTo(picture, path):
    """
    picture: the picture you want to be written out to a file
    path: the path to the file you want the picture written to

    Takes a picture and a file name (string) as input, then writes the picture to
    the file as a JPEG, PNG, or BMP.
    (Be sure to end the filename in ".jpg" or ".png" or ".bmp"
    for the operating system to understand it well.)

    Example:
    def writeTempPic(picture):
        file = r"C:\Temp\temp.jpg"
        writePictureTo(picture, file)

    This takes in a picture and writes it to C:\Temp\temp.jpg.
    """


def openPictureTool(picture):
    """
    picture: the picture that you want to examine
    Opens the Picture Tool explorer, which lets you examine the pixels of an image.

    Example:
    def openFileInPictureTool():
    file = pickAFile()
    pic = makePicture(file)
    openPictureTool(pic)

    This opens up a file selector dialog.
    The user picks an image file, and it is loaded into the Picture Tool.
    """


def setAllPixelsToAColor(picture, color):
    """
    picture: the picture to change the pixels of
    color: the color to set each pixel to

    Modifies the whole image so that every pixel in that image is the given color.

    Example:
    def makeColoredPicture():
        pic = makeEmptyPicture(100, 100)
        color = pickAColor()
        setAllPixelsToAColor(pic, color)
        return pic

    This opens up a color selector dialog, then the user picks a color,
    and the function returns a 100x100 picture of the chosen color.
    """


# === entities in globals but not explain ====================================#


def getAllPixels(picture):
    """
    picture: the picture you want to get the pixels from
    returns: a list of all the pixels in the picture

    Takes a picture as input and returns the sequence of Pixel objects in the picture.
    (Same as getPixels)

    Example:
    def getTenthPixel(picture):
        pixels = getAllPixels(picture)
        return pixels[9]

    This takes in a picture and returns the 10th pixel in that picture.
    """


class Picture(object):  # TODO add all properties & methods

    bufferedImage = None  # ----- many details   | BufferedImage
    image = bufferedImage  # ---- ^^^            | ^^^
    extension = None  # --------- extension      | String
    fileName = None  # ---------- full file path | String
    title = fileName  # --------- title          | String | initially same as name
    graphics = None  # ---------- many details   | sun.java2d.SunGraphics2D
    height = None  # ------------ height         | int
    width = None  # ------------- width          | int
    pictureFrame = None  # ------ ???            | ???
    pixels = None  # ------------ DON'T USE      | DON'T USE
    visible = None  # ----------- DNE            |
    allPixelsToAColor = None  # - DNE            |

    def __init__(self):
        pass

    # --- getters ------------------------------------------------------------#
    def createGraphics(self):
        return self.bufferedImage

    def getBufferedImage(self):
        return self.bufferedImage

    def getClass(self):
        return self.__class__

    def getExtension(self):
        return self.extension

    def getFileName(self):
        return self.fileName

    def getGraphics(self):
        return self.graphics

    def getHeight(self):
        return self.height

    def getImage(self):
        return self.image

    def getTitle(self):
        return self.title

    def getWidth(self):
        getWidth(self)

    # --- setters ------------------------------------------------------------#
    def setFileName(self, fileName):
        self.fileName = fileName

    def setTitle(self, title):
        self.title = title

    # --- drawing ------------------------------------------------------------#
    def addArc(self, color, startX, startY, width, height, start, angle):
        addArc(self, startX, startY, width, height, start, angle, color)

    def addArcFilled(self, color, startX, startY, width, height, start, angle):
        addArcFilled(self, startX, startY, width, height, start, angle, color)

    def addLine(self, color, startX, startY, endX, endY):
        addLine(self, startX, startY, endX, endY, color)

    def addOval(self, color, startX, startY, width, height):
        addOval(self, startX, startY, width, height, color)

    def addOvalFilled(self, color, startX, startY, width, height):
        addOvalFilled(self, startX, startY, width, height, color)

    def addRect(self, color, startX, startY, width, height):
        addRect(self, startX, startY, width, height, color)

    def addRectFilled(self, color, startX, startY, width, height):
        addRectFilled(self, startX, startY, width, height, color)

    # --- text ---------------------------------------------------------------#
    def addText(self, color, xpos, ypos, text):
        """todo: add desc """

    def addMessage(self, text, xpos, ypos):
        """todo: add desc"""

    def drawString(self, text, xpos, ypos):  # ???
        """todo: add desc"""

    def addTextWithStyle(self, color, xpos, ypos, text, style):
        addTextWithStyle(self, xpos, ypos, text, style, color)

    # --- pictures -----------------------------------------------------------#
    def copyInto(self, other_picture, xpos, ypos):
        copyInto(self, other_picture, xpos, ypos)

    def copyPicture(self, other_picture):
        """
        overwrites this pictures contents with the contents of other picture
        :param other_picture: the picture to copy into this picture
        :return: void/Unit
        """

    def scale(self, width_scale, height_scale):
        """
        makes a copy of this image with another scale applied to its width & height
        :param width_scale: multiplier for the width (can be decimal)
        :param height_scale: multiplier for the height (can be decimal)
        :return: a rescaled copy of this picture
        """

    def crop(self, xpos, ypos, width, height):
        """
        removes the frame around an image
        :param xpos: x coordinate of the new pic's top-left corner in respect to the original
        :param ypos: y coordinate of the new pic's top-left corner in respect to the original
        :param width:  the height of the copy
        :param height: the height of the copy
        :return: a cropped copy of the picture
        """

    def explore(self):
        from __root import explore
        explore(self)

    def getPictureWithHeight(self, size):
        """
        makes a new (green) square picture with width & height equal to height
        :param size: the width & height for the new picture
        :return: a new picture
        """

    def getPictureWithWidth(self, size):
        """
        SEE: getPictureWithHeight
        :param size: the width & height for the new picture
        :return: a new Picture
        """

    def repaint(self):
        repaint(self)

    # --- pixels -------------------------------------------------------------#
    def getBasicPixel(self, xpos, ypos):
        """
        gets the color value from the pixel as an int
        :param xpos: the x coordinate of the pixel
        :param ypos: the y coordinate of the pixel
        :return: the signed-integer color value of that pixel
        """

    def setBasicPixel(self, xpos, ypos, value):
        """
        sets the color from the pixel from an signed int value
        :param xpos: pixel's x coordinate
        :param ypos: pixel's y coordinate
        :param value: the singned integer value for the new color
        :return: void/Unit
        """

    def getPixel(self, xpos, ypos):
        getPixel(self, xpos, ypos)

    def getPixels(self):
        getPixels(self)

    def getTransformEnclosingRect(self):  # ???
        pass

    def setVisible(self, boolean):
        """
        shows or hides an image based on boolean (T show, F hide)
        :param boolean: whether to show of hide the image
        :return: void/Unit
        """

    def show(self):
        """ shows the image if hidden """

    def hide(self):
        """ hides the image if shown """

    def write(self, path):
        """
        writes (or overwrites) the image to a new file at path
        :param path: the location & name of the file to write
        :return: boolean True if success, false if fail
        """

    def writeOrFail(self):
        """
        writes (or overwrites) the image to a new file at path
        :param path: the location & name of the file to write
        :return: void/Unit if success, exception if fail
        """

    def getPictureFrame(self):
        """ todo: needs testing to understand its functionality """
        return self.pictureFrame

    def setPictureFrame(self, pictureFrame):
        """ todo: needs testing to understand its functionality """
        self.pictureFrame = pictureFrame

    def load(self, path):
        """ todo: needs testing to understand its functionality """

    def loadImage(self, path):
        """ todo: needs testing to understand its functionality """

    def loadOrFail(self, path):
        """ todo: needs testing to understand its functionality """

    def loadPictureAndShowIt(self, path):
        """ todo: needs testing to understand its functionality """

    def setAllPixelsToAColor(self, color):
        """ todo: needs testing to understand its functionality """

    # --- don't use ----------------------------------------------------------#
    def getMediaPath(self, path):
        """
        DON'T USE -- gets global media path
        use the global getMediaPath(path) instead
        """

    def notify(self):
        """ DON'T USE, for internal use """

    def notifyAll(self):
        """ DON'T USE, for internal use """

    def setMediaPath(self, path):
        """
        DON'T USE -- sets global media path
        use the global setMediaPath(path) instead
        """

    def wait(self):  # ???
        """ DON'T USE, for internal use """
