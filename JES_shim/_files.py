# === funcs in explain =======================================================#
def pickAFile():
    """
    returns: the string path to the file chosen in the dialog box
    Opens a file chooser to let the user pick a file and
    returns the complete path name as a string. Takes no input.

    Example:
    def openAnySound():
        file = pickAFile()
        return makeSound(file)

    This opens up a file selector dialog, then the user picks a file, and
    the function returns it as a sound.
    """


def pickAFolder():
    """
    returns: the string path to the folder chosen in the dialog box

    Opens a file chooser to let the user pick a folder and returns the complete path name as a string.
    Takes no input.

    Example:
    def showFolderContents():
        folder = pickAFolder()
        import os
        print os.listdir(folder)

    This opens up a file selector dialog, then the user picks a folder,
    and the function prints the contents of that folder.
    """


def setMediaPath(directory=None):
    """
    directory: The directory you want to set as the media folder. Takes a directory as input.
    JES then will look for files in that directory
    unless given a full path, i.e. one that starts with "c:\".
    You can leave out the directory.
    If you do, JES will open up a file chooser to let you select a directory.

    Examples:
    def openBobsSong():
        setMediaPath()
        song = makeSound("BobsSong.wav")
        return song

    This will let the user set a folder to look for files in,
    and then open the file "BobsSong.wav" in that folder.

    def openMarysSong():
        setMediaPath("C:\\music")
        song = makeSound("MarysSong.wav")
        return song

    This sets the folder to look in to "C:\music",
    and then open the file "MarysSong.wav" in that folder.
    """


def setMediaFolder(directory=None):
    """
    directory: The directory you want to set as the media folder. Takes a directory as input.
    JES then will look for files in that directory
    unless given a full path, i.e. one that starts with "c:\".
    You can leave out the directory.
    If you do, JES will open up a file chooser to let you select a directory.

    Examples:
    def openBobsSong():
        setMediaFolder()
        song = makeSound("BobsSong.wav")
        return song

    This will let the user set a folder to look for files in,
    and then open the file "BobsSong.wav" in that folder.

    def openMarysSong():
        setMediaFolder("C:\\music")
        song = makeSound("MarysSong.wav")
        return song

    This sets the folder to look in to "C:\music",
    and then open the file "MarysSong.wav" in that folder.
    """


def getMediaPath(fileName=None):
    """
    filename: the name of the file you want (optional)
    returns: the complete path to the file specified

    This function builds the whole path to the file you specify,
    as long as you've already used setMediaFolder() or setMediaPath() to pick out the place where you keep your media.
    If no filename is given, only the MediaPath will be returned.
    (Same as getMediaFolder)

     Example:
    def getFullPathToMarysSong():
        setMediaPath("C:\\")
        return getMediaPath("MarysSong.wav")

    This set the MediaPath to C:\ and will return the full path of MarysSong.wav ('C:\\MarysSong.wav').

    def getAndSetMediaPath():
        setMediaPath("C:\\")
        return getMediaPath()

    This set the MediaPath to C:\ and will then return it ('C:\\').
    """


def getMediaFolder(fileName=None):
    """
    filename: the name of the file you want (optional)
    returns: the complete path to the file specified

    This function builds the whole path to the file you specify,
    as long as you've already used setMediaFolder() or setMediaPath() to pick out the place where you keep your media.
    If no filename is given, only the MediaFolder will be returned.

    Example:
    def getFullPathToMarysSong():
        setMediaFolder("C:\\")
        return getMediaFolder("MarysSong.wav")

    This set the MediaFolder to C:\ and will return the full path of MarysSong.wav ('C:\\MarysSong.wav').

    def getAndSetMediaFolder():
        setMediaFolder("C:\\")
        return getMediaFolder()

    This set the MediaFolder to C:\ and will then return it ('C:\\').
    """


def getShortPath(path):
    """
    path: a path to a file, as a string
    returns: a shorter, non-absolute version of that path

    Takes a file path as input and returns the short version of that path.

    Example:
    print getShortPath("c:\\images\\kittens\\fluffy.jpg")

    This will print the short path of "c:\images\kittens\fluffy.jpg" which is "kittens\fluffy.jpg".
    """


def setLibPath(directory=None):
    """
    directory: a string path to a directory. (optional)
    If you leave this out, JES will open up a file chooser for you to select a directory yourself.

    Adds a directory where JES will look for modules that you want to be able to import.

    Example:
    def addMediaPathAsLibPath():
        addLibPath(getMediaPath())

    This will allow you to import .py files in the current media path.
    """


# === entities in globals but not explain ====================================#
# TODO -- functions with a file/dir param (not shimmed)
'''
showMediaFolder
'''


def addLibPath(directory=None):
    """
    directory: a string path to a directory. (optional)
    If you leave this out, JES will open up a file chooser for you to select a directory yourself.
    Adds a directory where JES will look for modules that you want to be able to import.
    (This function used to be called setLibPath.)

    Example:
    def addMediaPathAsLibPath():
        addLibPath(getMediaPath())

    This will allow you to import .py files in the current media path.
    """


class FileChooser:  # TODO add all properties & methods
    def __init__(self):
        pass


# java.io.File
class File:  # TODO add all properties & methods
    def __init__(self):
        pass
