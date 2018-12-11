# Final Project: Morse Code Player & Trainer

### authors ###################################################################
# J Asato
# M Robertson
# R Talmage
###############################################################################

import random

# use shim in non-JES environment, otherwise ignore
try:
    from JES_shim import showInformation, requestString, \
        makeSound, blockingPlay, pickAFolder
except ImportError:
    pass


class Environment(object):
    """the application's operating environment (JES or elsewhere)"""
    JES, OTHER = range(2)
    current = OTHER

    @staticmethod
    def discover():
        """
        discover whether the application is running in JES by inspecting __doc__
        :return:
        """
        if __doc__ and "JES" in __doc__:
            Environment.current = Environment.JES


class UserInterface(object):
    """
    models a user interface -- allowing this to be run in
    either JES or a python interpreter
    """

    JES_UI, CONSOLE = range(2)  # the known interface environments

    def __init__(self, interface_type=JES_UI):
        """
        create a interface
        :param interface_type: the target environment
        (default JES)
        """
        self.interface_type = interface_type

    def show(self, message):
        """
        tells the user interface to display a message
        :param message: the message to display
        :return: None
        """
        if self.interface_type == UserInterface.JES_UI:
            showInformation(message)
        else:
            print(message)

    def ask(self, message):
        """
        tells the user interface to retrieve a string from the user
        :param message: the message to display when asking for input
        :return: the input string from the user
        """
        if self.interface_type == UserInterface.JES_UI:
            return requestString(message)
        else:
            return raw_input(message)


class Util(object):
    """
    common utility functions
    """

    @staticmethod
    def flatten(list_1, list_2=None):
        """
        flattens a list of nested list into a single list
        :param list_1: the list to flatten
        :param list_2: the list to prepend (optional)
        :return:
        """
        if list_2 is None:
            list_2 = []
        for item in list_1:
            if isinstance(item, list):
                Util.flatten(item, list_2)
            else:
                list_2.append(item)
        return list_2

    @staticmethod
    def file_as_string(file_path):
        """
        reads a file's contents into a string
        :param file_path: the file's path
        :return: a string holding the file's contents
        """
        file_in = open(file_path, 'rt')  # open file for reading
        result = file_in.read().strip()
        file_in.close()
        return result

    @staticmethod
    def file_as_list(file_path):
        """
        reads a file's lines into a list of strings
        :param file_path: the file's path
        :return: a list of strings holding the file's contents (line separated)
        """
        return Util.file_as_string(file_path).splitlines()

    @staticmethod
    def file_as_wav(file_path):
        """
        loads a wav file
        :param file_path: the file's path
        :return: the loaded (playable) wav file
        """
        return makeSound(file_path)

    @staticmethod
    def play_sound(sound):
        """
        plays a loaded wav file
        :param sound: the sound (wav file) to play
        :return: None
        """
        # todo impl for non-JES environments
        blockingPlay(sound)


class Sound(object):
    PAUSE, SHORT, LONG = range(3)  # beep types (and pause)


class MorseCodes(object):
    S = Sound.SHORT
    L = Sound.LONG
    P = Sound.PAUSE

    # mapping between Letters/Numbers & Morse Codes
    LETTERS = {
        'A': [S, L],
        'B': [L, S, S, S],
        'C': [L, S, L, S],
        'D': [L, S, S],
        'E': [S],
        'F': [S, S, L, S],
        'G': [L, L, S],
        'H': [S, S, S, S],
        'I': [S, S],
        'J': [S, L, L, L],
        'K': [L, S, L],
        'L': [S, L, S, S],
        'M': [L, L],
        'N': [L, S],
        'O': [L, L, L],
        'P': [S, L, L, S],
        'Q': [L, L, S, L],
        'R': [S, L, S],
        'S': [S, S, S],
        'T': [L],
        'U': [S, S, L],
        'V': [S, S, S, L],
        'W': [S, L, L],
        'X': [L, S, S, L],
        'Y': [L, S, L, L],
        'Z': [L, L, S, S],
        '1': [S, L, L, L, L],
        '2': [S, S, L, L, L],
        '3': [S, S, S, L, L],
        '4': [S, S, S, S, L],
        '5': [S, S, S, S, S],
        '6': [L, S, S, S, S],
        '7': [L, L, S, S, S],
        '8': [L, L, L, S, S],
        '9': [L, L, L, L, S],
        '0': [L, L, L, L, L],
    }

    LETTER_BREAK = [P, P, P]  # pause between letters
    WORD_BREAK = [P, P, P, P, P, P]  # pause between words

    @staticmethod
    def _get_letter(char):
        """
        gets the corresponding Morse Code sequence for a given letter
        :param char: the character to get the code for
        :return: the character's corresponding Morse Code sequence or None
        """

        char = char.upper()

        # a space -> use WORD_BREAK
        if char == ' ':
            # print("char -- space: '%s', will return %s" % (char, MorseCodes.WORD_BREAK))
            return MorseCodes.WORD_BREAK

        # not in LETTERS -> empty list
        if char not in MorseCodes.LETTERS:
            # print("char -- invalid: '%s', will return empty list")
            return list()

        # in LETTERS -> look it up, intersperse spaces, add letter space
        result = [MorseCodes.P, MorseCodes.LETTERS[char], MorseCodes.LETTER_BREAK]
        # print("char -- ok: '%s', will return %s" % (char, result))
        return Util.flatten(result)

    @staticmethod
    def encode(string):
        """
        encodes a string into a Morse Code sequence
        :param string: the string to encode
        :return: the Morse Code sequence
        """
        sounds = []
        for letter in string:
            sounds.append(MorseCodes._get_letter(letter))
        return Util.flatten(sounds)


class AudioHolder(object):
    """
    holds and plays Morse Code audio files
    """

    def __init__(self, media_dir='.'):
        """
        create an AudioHolder
        :param media_dir: the directory containing the audio files
        """
        self.sounds = {
            Sound.PAUSE: Util.file_as_wav(media_dir + '/m_pause.wav'),
            Sound.SHORT: Util.file_as_wav(media_dir + '/m_short.wav'),
            Sound.LONG: Util.file_as_wav(media_dir + '/m_long.wav')
        }

    def play(self, code_sequence):
        """
        plays a Morse Code sequence
        :param code_sequence: the sequence to play
        :return: None
        """
        print(code_sequence)
        for to_play in code_sequence:
            print("playing sound for: %s" % to_play)
            sound = self.sounds[to_play]

            Util.play_sound(sound)


class App(object):
    """
    the Morse Code Trainer Application
    """

    ENCODE, TRAIN, EXIT = range(3)  # commands

    def __init__(self, ui, training_file='training.txt'):
        """
        creates a Morse Code Trainer
        :param ui: the user interface to use
        :param training_file: the name of training file to use
        (should be placed in the media_dir)
        """
        self.ui = ui
        Environment.discover()
        if Environment.current is Environment.JES:
            media_dir = pickAFolder()
        else:
            media_dir = '.'
        self.audio_holder = AudioHolder(media_dir)
        self.training_messages = Util.file_as_list(media_dir + "/" + training_file)

    def run(self):
        """
        runs the Morse Code Application
        :return: None
        """
        # ask user for mode: listen / training
        self.ui.show("Welcome to the morse code trainer")

        while True:
            mode = self._ask_for_mode()

            if mode is App.ENCODE:
                self._run_listen_mode()

            if mode is App.TRAIN:
                self._run_train_mode()

            if mode is App.EXIT:
                break

        pass

    def _ask_for_mode(self, error_mess=None):
        message = "Choose a mode:\n" \
                  "  1: Encode messages and listen to Morse Code\n" \
                  "  2: Morse Code training\n" \
                  "  3: exit\n"

        if error_mess:
            message = error_mess + '\n' + message

        mode = self.ui.ask(message)

        if mode in ['1', '2', '3']:
            return int(mode) - 1

        return self._ask_for_mode("The option you entered '%s' is invalid." % mode)

    def _run_listen_mode(self, article='a'):
        # listen mode -> ask for message to encode & play it

        message = "Type %s message to playback in Morse Code.\n" \
                  "Submit an empty message to go back to mode selection.\n" % article

        to_play = self.ui.ask(message)
        if to_play:
            to_play_encoded = MorseCodes.encode(to_play)
            self.audio_holder.play(to_play_encoded)
            self._run_listen_mode('another')

    def _run_train_mode(self, continuing=False):
        # train mode -> play a random message from trainer messages
        message = "Type the played Morse Code message.\n" \
                  "If you guess wrong, the message will be replayed.\n" \
                  "Submit an empty message to go back to mode selection.\n"

        if not continuing:
            self.ui.show(message)

        answer = random.choice(self.training_messages)

        answer_encoded = MorseCodes.encode(answer)

        while True:
            self.audio_holder.play(answer_encoded)
            print("answer: %s" % answer)

            to_ask = "What message was just played?\n" \
                     "Submit an empty answer to go back to mode selection.\n"

            user_guess = self.ui.ask(to_ask)
            if not user_guess:
                return
            if MorseCodes.encode(user_guess) == answer_encoded:
                self.ui.show("Correct! The message was '%s'." % answer)
                break
            else:
                self.ui.show("Your guess '%s' was incorrect. Try again." % user_guess)
        self._run_train_mode(continuing=True)


def main():
    ui = UserInterface(UserInterface.CONSOLE)
    App(ui).run()


def test():
    Environment.discover()
    print Environment.current

    app = App(UserInterface(UserInterface.CONSOLE))
    # mode = app._ask_for_mode()
    # app._run_listen_mode()
    # app._run_train_mode()
    app.run()

    message = MorseCodes.encode("good message")
    print("message: %s" % message)
