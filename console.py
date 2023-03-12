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
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
