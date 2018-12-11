# === funcs in explain =======================================================#
def playNote(note, duration, intensity=64):
    """
    note: the MIDI note number, from 0 to 127 (60 = Middle C) you want to be played
    duration: the duration you want the note to be played in milliseconds
    intensity: the intensity (a number between 0 and 127) you want the note to be played (optional)
    Default intensity is 64.

    Plays the given note.
    No return value.

    Example:
    def playScale():
        intensity = 64
        dur = 1000
        playNote(60, dur, intensity)
        playNote(62, dur, intensity)
        playNote(64, dur, intensity)
        playNote(65, dur, intensity)
        playNote(67, dur, intensity)
        playNote(69, dur, intensity)
        playNote(71, dur, intensity)
        playNote(72, dur, intensity)

    This will play a scale with one second notes and default intensity.
    """


def blockingPlay(sound):
    """
    sound: the sound that you want to play

    Plays the sound provided as input,
    and makes sure that no other sound plays at the exact same time.
    (Try two play's right after each other.)

    Example:
    def playSoundTwice():
        sound = makeSound(r"C:\My Sounds\preamble.wav")
        blockingPlay(sound)
        blockingPlay(sound)

    This will play the preamble.wav twice, back-to-back.
    """


def duplicateSound(sound):
    """
    sound: the sound you want to duplicate
    returns: a new Sound object with the same Sample values
    as the original

    Takes a sound as input and returns a new Sound object
    with the same Sample values as the original.

    Example:
    file = pickAFile()
        mysound = makeSound(file)
        copyofmysound = duplicateSound(mysound)

    This opens up a file chooser, makes a Sound object using the chosen file,
    and then creates a second Sound object by copying the first one.
    """


def getDuration(sound):
    """
    sound: the sound you want to find the length of (in seconds)
    returns: the number of seconds the sound lasts

    Takes a sound as input and returns the number of seconds that sound lasts.

    Example:
    def songLength():
        sound = makeSound(r"C:\My Sounds\2secondsong.wav")
        print getDuration(sound)

    This will print out the number of seconds in the sound.
    For a song with 88000 samples at 44kHz, it will print out "2.0"
    """


def getLength(sound):
    """
    sound: the sound you want to find the length of (how many samples it has)
    returns: the number of samples in sound

    Takes a sound as input and returns the number of samples in that sound.

    Example:
    def songLength():
        sound = makeSound(r"C:\My Sounds\2secondsong.wav")
        print getLength(sound)

    This will print out the number of samples in the sound.
    For a 2 second song at 44kHz, it will print out 88000.
    """


def getNumSamples(sound):
    """
    sound: the sound you want to find the length of (how many samples it has)
    returns: the number of samples in sound

    Takes a sound as input and returns the number of samples in that sound.

    Example:
    def songLength():
        sound = makeSound(r"C:\My Sounds\2secondsong.wav")
        print getNumSamples(sound)

    This will print out the number of samples in the sound.
    For a 2 second song at 44kHz, it will print out 88000.
    """


def getSampleObjectAt(sound, index):
    """
    sound: the sound you want to get the sample from
    index: the index of the sample you want to get
    returns: the sample object at that index

    Takes a sound and an index (an integer value), and returns the Sample object at that index.

    Example:
    def getTenthSample(sound):
        samp = getSampleObjectAt(sound, 9)
        return samp

    This takes a sound, and returns the 10th sample in the sound.
    """


def getSamples(sound):
    """
    sound: A Sound, the sound you want to extract the samples from
    returns: A collection of all the samples in the sound

    Takes a sound as input and returns the Samples in that sound.

    Example:
    def printFirstTen(sound):
        samps = getSamples(sound)
        for num in range(0, 10):
            print samps[num]

    This will take in a sound and print the first 10 samples in that sound
    """


def getSampleValue(sample):
    """
    sample: a sample of a sound
    returns: the integer value of that sample

    Takes a Sample object and returns its value (between -32768 and 32767).
    (Formerly getSample)

    Example:
    def sampleToInt(sample):
        return getSampleValue(sample)

    This will convert a sample object into an integer.
    """


######
def getSampleValueAt(sound, index):
    """
    sound: the sound you want to get the sample from index: the index of the sample you want to get the value of Takes a sound and an index (an integer value), and returns the value of the sample (between -32768 and 32767) for that object. Example:
def getTenthSampleValue(sound):
  num = getSampleValueAt(sound, 9)
  return num
This will take in a sound and return the integer value of the tenth sample
    """


def getSamplingRate(sound):
    """
    sound: the sound you want to get the sampling rate from returns: the integer value representing the number of samples per second Takes a sound as input and returns the number representing the number of samples in each second for the sound. Example:
def getDoubleSamplingRate(sound):
  rate = getSamplingRate(sound)
  return (rate * 2)
This will take in a sound an return the sampling rate multiplied by 2.
    """


def getSound(sample):
    """
    sample: a sample belonging to a sound return: the sound the sample belongs to Takes a Sample object and returns the Sound that it belongs to. Example:
def getSamplesFromAnySample(sample):
  sound = getSound(sample)
  return getSamples(sound)
This will take in a sample and return the list of samples from the original sound.
    """


def makeEmptySound(numSamples, samplingRate=22050):
    """
    numSamples: the number of samples in the sound samplingRate: the integer value representing the number of samples per second (optional) returns: an empty sound with the given number of samples and sampling rate Takes one or two integers as input. Returns an empty Sound object with the given number of samples and (optionally) the given sampling rate. Default rate is 22050 bits/second. The resulting sound must not be longer than 600 seconds. Prints an error statement if numSamples or samplingRate are less than 0, or if (numSamples/samplingRate) > 600. Examples:
def make10SecondSound():
  return makeEmptySound(10 * 22050)
This will return an empty sound lasting 10 seconds long, using the default sampling rate (22050 bits/second).
def make10SecondSoundWithSamplingRate(samplingRate):
  return makeEmptySound(10 * samplingRate, samplingRate)
This will return an empty sound lasting 10 seconds long, using the given sampling rate.
    """


def makeEmptySoundBySeconds(duration, samplingRate=22050):
    """
    duration: the time in seconds for the duration of the sound samplingRate: the integer value representing the number of samples per second of sound (optional) returns: An Empty Sound. Takes a floating point number and optionally an integer as input. Returns an empty Sound object of the given duration and (optionally) the given sampling rate. Default rate is 22050 bits/second. If the given arguments do not multiply to an integer, the number of samples is rounded up. Prints an error statement if duration or samplingRate are less than 0, or if duration > 600. Examples:
def make10SecondSound():
  return makeEmptySoundBySeconds(10)
This will return an empty sound lasting 10 seconds long, using the default sampling rate (22050 bits/second).
def make10SecondSoundWithSamplingRate(samplingRate):
  return makeEmptySoundBySecons(10, samplingRate)
This will return an empty sound lasting 10 seconds long, using the given sampling rate.
    """


def makeSound(path):
    """
    path: a string path of a wav file returns: the sound created from the file at the given path Takes a filename as input, reads the file, and creates a sound from it. Returns the sound. Example:
def openAnySound():
  file = pickAFile()
  return makeSound(file)
This opens up a file selector dialog. The user picks a file, and the function returns it as a sound.
    """


def play(sound):
    """
    sound: the sound you want to be played Plays a sound provided as input. No return value. Example:
def playAnySound():
  file = pickAFile()
  sound = makeSound(file)
  play(sound)
This will open up a file selector box, make a sound from the chosen file, and then play that sound back.
    """


def setSampleValue(sample, value):
    """
    setSampleValue(sample, value): sample: the sound sample you want to change the value of value: the value you want to set the sample to Takes a Sample object and a value (should be between -32768 and 32767), and sets the sample to that value. Example:
def setTenthSample(sound, value):
  samp = getSampleObjectAt(sound, 9)
  setSampleValue(samp, value)
This takes a sound and an integer, and then sets the value of the 10th sample in the sound to the passed in value.
    """


def setSampleValueAt(sound, index, value):
    """
    sound: the sound you want to change a sample in index: the index of the sample you want to set value: the value you want to set the sample to Takes a sound, an index, and a value (should be between -32768 and 32767), and sets the value of the sample at the given index in the given sound to the given value. Example:
def setTenthToTen(sound):
  setSampleValueAt(sound, 9, 10)
This takes in a sound and sets the value of the 10th sample to 10.
    """


def stopPlaying(sound):
    """
    sound: the sound that you want to stop playing Stops a sound that is currently playing. Example:
def playAndStop():
  sound = makeSound(r"C:\My Sounds\preamble.wav")
  play(sound)
  stopPlaying(sound)
This will start playing preamble.wav and stop it immediately after it starts.
    """


def writeSoundTo(sound, path):
    """
    sound: the sound you want to write out to a file path: the path to the file you want the picture written to Takes a sound and a filename (a string) and writes the sound to that file as a WAV file. (Make sure that the filename ends in '.wav' if you want the operating system to treat it right.) Example:
def writeTempSound(sound):
  writeSoundTo(sound, 'C:\\temp\\temp.wav')
This takes in a sound and writes it out to a file called temp.wav in C:\temp\.
    """


def openSoundTool(sound):
    """
    sound : the sound that you want to examine Opens the Sound Tool explorer, which lets you examine the waveform of a sound. Example:
def openFileInSoundTool():
  file = pickAFile()
  sound = makeSound(file)
  openSoundTool(sound)
This opens up a file selector dialog. The user picks a sound file, and it is loaded into the Sound Tool.
    """


# === entities in globals but not explain ====================================#

class Sample:  # TODO add all properties & methods
    sound = None
    value = None

    def __init__(self):
        pass

    def getClass(self):
        pass

    def getSound(self):
        pass

    def getValue(self):
        pass

    def setValue(self):
        pass


class Samples:  # TODO add all properties & methods
    sound = None

    def __init__(self):
        pass

    def getSample(self):
        pass

    def getSamples(self):
        pass

    def getSound(self):
        pass

    def setSample(self):
        pass


class Sound:  # TODO add all properties & methods
    MAX_NEG = -32768  # ---------
    MAX_POS = 32767  # ----------
    SAMPLE_RATE = 22050  # ------

    _SoundIndexOffset = None  # -

    audioFileFormat = None  # ---
    buffer = None  # ------------
    channels = None  # ----------
    fileName = None  # ---------- full file path | String
    length = None  # ------------
    lengthInBytes = None  # -----
    lengthInFrames = None  # ----
    numSamples = None  # --------
    playbacks = None  # ---------
    samples = None  # -----------
    samplingRate = None  # ------
    soundExplorer = None  # -----
    stereo = None  # ------------

    def __init__(self):
        pass

    def asArray(self):
        pass

    def blockingPlay(self):
        pass

    def blockingPlayAtRateDur(self):
        pass

    def blockingPlayAtRateInRange(self):
        pass

    def blockingPlayOld(self):
        pass

    def convert(self):
        pass

    def copySoundInto(self):
        pass

    def cropSound(self):
        pass

    def explore(self):
        pass

    def getAudioFileFormat(self):
        pass

    def getBuffer(self):
        pass

    def getChannels(self):
        pass

    def getClass(self):
        pass

    def getFileName(self):
        pass

    def getFrame(self):
        pass

    def getLeftSample(self):
        pass

    def getLength(self):
        pass

    def getLengthInBytes(self):
        pass

    def getLengthInFrames(self):
        pass

    def getNumSamples(self):
        pass

    def getPlaybacks(self):
        pass

    def getRightSample(self):
        pass

    def getSample(self):
        pass

    def getSampleValue(self):
        pass

    def getSampleValueAt(self):
        pass

    def getSamples(self):
        pass

    def getSamplingRate(self):
        pass

    def getSoundExplorer(self):
        pass

    def hashCode(self):
        pass

    def isStereo(self):
        pass

    def loadFromFile(self):
        pass

    def makeAIS(self):
        pass

    def notify(self):
        pass

    def notifyAll(self):
        pass

    def play(self):
        pass

    def playAtRateDur(self):
        pass

    def playAtRateInRange(self):
        pass

    def playNote(self):
        pass

    def printError(self):
        pass

    def removePlayback(self):
        pass

    def setAudioFileFormat(self):
        pass

    def setBuffer(self):
        pass

    def setFrame(self):
        pass

    def setLeftSample(self):
        pass

    def setRightSample(self):
        pass

    def setSampleValue(self):
        pass

    def setSampleValueAt(self):
        pass

    def setSoundExplorer(self):
        pass

    def stopPlaying(self):
        pass

    def toString(self):
        pass

    def wait(self):
        pass

    def write(self):
        pass

    def writeToFile(self):
        pass
