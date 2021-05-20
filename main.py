import sys
from exseptions import *
from logic import parse, calc


class MyIo:
    def __init__(self, text):
        self.text = text
        self.__log(self.text)

    def write(self):
        print(self.text)

    def read(self):
        input_text = input(self.text)
        self.__log(input_text)
        return input_text

    def __log(self, text):
        with open('history.txt', 'a') as history:
            history.write(str(text) + '\n')


command = ''
while True:
    command = MyIo('>> ').read()
    if command:
        if command == 'exit':
            break
        else:
            try:
                separated_input = parse.Separate(command)
            except InvalidFormatException as ex:
                MyIo(ex.msg).write()
            except InvalidOperatorException as ex:
                MyIo(ex.msg).write()
            except InvalidNumberException as ex:
                MyIo(ex.msg).write()
            else:
                MyIo(calc.calculate(separated_input.operation1,
                                    separated_input.operator,
                                    separated_input.operation2)).write()
