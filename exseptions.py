class InvalidFormatException(Exception):
    def __init__(self, message=None):
        self.msg = message


class InvalidNumberException(Exception):
    def __init__(self, message=None):
        self.msg = message


class InvalidOperatorException(Exception):
    def __init__(self, message=None):
        self.msg = message
