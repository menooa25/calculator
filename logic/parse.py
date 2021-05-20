from exseptions import *


class Separate:
    def __init__(self, input_str):
        self.separated_input = input_str.split()
        self.__check_validation()

    def __check_validation(self):
        if len(self.separated_input) != 3:
            raise InvalidFormatException('You entered format is invalid')
        else:
            try:
                float(self.separated_input[0])
                float(self.separated_input[2])
            except:
                raise InvalidNumberException('Your one of the entered numbers in invalid')
            else:
                if self.separated_input[1] not in '+-*/':
                    raise InvalidOperatorException('You entered invalid operator')

    @property
    def operation1(self):
        return float(self.separated_input[0])

    @property
    def operation2(self):
        return float(self.separated_input[2])

    @property
    def operator(self):
        return self.separated_input[1]
