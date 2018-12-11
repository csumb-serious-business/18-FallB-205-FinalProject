# === funcs in explain =======================================================#

def addFrameToMovie(frame, movie):
    """
    frame: the filename of the frame to be added to the movie
    movie: the movie object for the frame to be added to

    Takes a filename and a Movie object as input.
    Adds the file as a frame to the end of the movie.
    addFrameToMovie(movie, frame) is also acceptable.

    Example:
    def addFileToMovie(movie):
        picture = pickAFile()
        addFrameToMovie(picture, movie)

    This will allow the user to choose the filename of a picture,
    and add that picture as the last frame in the specified movie.
    """


# TODO -- functions with a movie param (not shimmed, might be Movie class methods
'''
playMovie
makeMovie
makeMovieFromInitialFile
writeFramesToDirectory
writeQuicktime
writeAVI
openFrameSequencerTool
'''


# === entities in globals but not explain ====================================#


# media.Movie
class Movie:  # TODO add all properties & methods
    def __init__(self):
        pass


class MoviePlayer:  # TODO add all properties & methods
    def __init__(self):
        pass


class MovieWriter:  # TODO add all properties & methods
    def __init__(self):
        pass


# jes.tools.framesequencer.FrameSequencerTool
class FrameSequencerTool:  # TODO add all properties & methods
    def __init__(self):
        pass
