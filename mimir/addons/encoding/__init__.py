import base64
# import mimir.addons.encoding.base91 as base91


class _Encoder:
    def __init__(self, name=None):
        self._name = name if name else "BaseEncoder"

    @property
    def name(self):
        return self._name

    @staticmethod
    def decode(data):
        raise NotImplementedError

    @staticmethod
    def encode(data):
        raise NotImplementedError


class Base64(_Encoder):
    def __init__(self):
        super().__init__("Base64")

    @staticmethod
    def decode(data):
        return base64.b64decode(data)

    @staticmethod
    def encode(data):
        return base64.b64encode(data)


class Base16(_Encoder):
    def __init__(self):
        super().__init__("Base16")

    @staticmethod
    def decode(data):
        return base64.b16decode(data)

    @staticmethod
    def encode(data):
        return base64.b16encode(data)


class Base32(_Encoder):
    def __init__(self):
        super(Base32, self).__init__("Base32")

    @staticmethod
    def decode(data):
        return base64.b32decode(data)

    @staticmethod
    def encode(data):
        return base64.b32encode(data)


class Base91(_Encoder):
    def __init__(self):
        super().__init__("Base91")

    @staticmethod
    def decode(data):
        # return base91.decode(data)
        pass

    @staticmethod
    def encode(data):
        # return base91.encode(data)
        pass


class Ascii85(_Encoder):
    def __init__(self):
        super().__init__("Ascii85")

    @staticmethod
    def decode(data, adobe=False):
        if data.startswith('<~') and data.endswith('~>'):
            adobe = True
        return base64.a85decode(data, adobe=adobe)

    @staticmethod
    def encode(data, adobe=False):
        return base64.a85encode(data, adobe=adobe)


# TODO
# Morse
# Braille
# Semaphore
# Tap Code
# ASL
# PigPen
# BetaMaze
# A1Z26

def get_algorithms():
    return [
        Base64,
        Base32,
        Base16,
        Base91,
        Ascii85
    ]
