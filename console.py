#!/usr/bin/python3
'''
HBNB Command Interpreter
'''

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''
    HBNB Command Interpreter definition
    '''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        '''
        Leaves the command interpreter
        '''
        return True

    def do_EOF(self, arg):
        '''
        Leaves the command interpreter
        '''
        return True

    def emptyline(self):
        '''
        Prints prompts if the line is empty when pressing Enter for example
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
