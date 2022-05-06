"""
Rotor is the primary part of an 'Enigma Machine'.
It undertakes the main coding and decoding tasks.
An Enigma Machine, theoretically, can contain as many rotors.
In this task, we aim to implement classical 3 rotors machine.
"""


class Rotor(object):
    def __init__(self, index):
        self.pos = 'A'  # pos means the rotor's state of rotation. It can be reset when the key is given.
        self.index = index  # index means the rotor's position in an Enigma Machine.
        # It should be fixed when the machine is created.
        self.encode_offset = 0  # per character encoding offset which can be calculated by pos.

    def init(self, key: chr):
        """
        :param key: single capital letter used to initiate rotor's state of rotation
        :return: None
        """
        self.pos = key
        self.reset_encode_offset()

    def reset_encode_offset(self):
        """
        :return: None
        """
        self.encode_offset = ord(self.pos) - 65

    def encoding_single_character(self, x):
        """
        :param x: the english char need to be encoded.
        :return: encoded char.
        """
        tmp = ord(x) - ord('a') + self.encode_offset
        e_char = chr(tmp % 26 + ord('a'))
        return e_char

    def progression(self, flag=True):
        """
        Detects if this rotor needs to be rotated.
        :param flag: signal from former rotor(index == 0 will always get 'True' signal).
        :return: signal passed to next rotor.
        """
        if flag:
            self.pos = chr(((ord(self.pos) - 65 + 1) % 26) + 65)
            self.reset_encode_offset()
            return self.pos == 'A'  # omit True signal
        return False


if __name__ == '__main__':
    R = Rotor(0)
    R.init('M')
    print(R.encoding_single_character('a'))
    R.progression()
    print(R.encoding_single_character('a'))