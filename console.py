#!/usr/bin/python3
'''
HBNB Command Interpreter
'''
import models
import cmd
import sys
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''
    HBNB Command Interpreter definition
    '''
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    __classes = {'Amenity': Amenity,
                 'BaseModel': BaseModel,
                 'City': City,
                 'Place': Place,
                 'Review': Review,
                 'State': State,
                 'User': User}

    def do_quit(self, arg):
        '''
        Quit command to exit the program
        '''
        return True

    def do_EOF(self, arg):
        '''
        EOF command to exit the program when EOF is triggered
        '''
        return True

    def do_help(self, arg):
        '''
        help command to display docstring of a command passed to `arg`
        '''
        return super().do_help(arg)

    def emptyline(self):
        '''
        emptyline command is triggered when the line is empty when pressing
        Enter for example
        '''
        pass

    def do_create(self, line):
        '''
        create command to initializes an instance
        '''
        cls_name = line
        if not cls_name:
            print('** class name missing **')
            return

        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        obj = HBNBCommand.__classes[cls_name]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        '''
        show command to print an instance based on its class and id
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        id = args[1]
        key = cls_name + '.' + id
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

    def do_destroy(self, line):
        '''
        destroy command to delete an instance based on the class name and id.
        Changes are saved in the JSON file too.
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        id = args[1]
        key = cls_name + '.' + id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, line):
        '''
        all command to prints all string representation of instances based
        or not on the class name
        '''
        args = line.split()
        cls_name = args[0] if len(args) != 0 else None
        list_objs = []
        if cls_name is None:
            for v in models.storage.all().values():
                list_objs.append(str(v))
        else:
            if cls_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                for v in models.storage.all().values():
                    if cls_name == v.__class__.__name__:
                        list_objs.append(str(v))
        print(list_objs)

    def do_update(self, line):
        '''
        update command to update an instance based on the class name and id by
        adding or updating attributes.
        All changes are automatically save in the JSON file
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        id = args[1]
        key = cls_name + '.' + id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        obj = models.storage.all()[key]

        if len(args) == 2:
            print("** attribute name missing **")
            return

        att = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        if att in ['id', 'created_at', 'updated_at']:
            return

        val = args[3]
        try:
            if val[0] == '"' and val[-1] == '"':
                val = str(val[1:-1])
            elif '.' not in val:
                val = int(val)
            else:
                val = float(val)
        except Exception:
            return

        setattr(obj, att, val)
        obj.save()

    def default(self, line):
        '''
        Handles unrecognized commands syntax
        '''
        cmd_funcs = {
                'all': self.do_all
                }

        cleaned_line = rmtrchr(line)
        if '.' not in line:
            print("*** Unknown syntax:", line)
            return

        dot_idx = cleaned_line.find('.')  # Finding the first dot
        if dot_idx == - 1:
            print("*** Unknown syntax:", line)
            return
        if dot_idx + 1 >= len(line):
            print("*** Unknown syntax:", line)
            return

        cmd_cls = cleaned_line[:dot_idx]
        if cmd_cls not in HBNBCommand.__classes:
            print("*** Unknown syntax:", line)
            return

        remain = cleaned_line[dot_idx + 1:]

        if '(' not in remain or ')' not in remain\
                or ('(' in remain and remain[len(remain) - 1] != ')'):
            print("*** Unknown syntax:", line)
            return

        op_idx = remain.find('(')  # Finding the opening parenthesis
        cmd_func = remain[:op_idx]
        if cmd_func not in cmd_funcs:
            print("*** Unknown syntax:", line)
            return

        if remain.find('(', op_idx + 1) != -1:
            print("*** Unknown syntax:", line)
            return

        if cmd_func in ['all']:
            cp_idx = remain.find(')', op_idx + 1)
            if cp_idx != - 1 and remain.find(')', cp_idx + 1) != -1:
                print("*** Unknown syntax:", line)
                return
            # At this stage, the line is perfected
            cmd_funcs[cmd_func](cmd_cls)
            return

    def do_clear(self, line):
        '''
        clear command to clear the interpreter interface
        '''
        from os import system
        system('clear')


def rmtrchr(line):
    '''
    Removes Trailing characters of a line
    '''
    chars = [chr(32), chr(8), chr(9), chr(10), chr(11), chr(12), chr(13)]
    clean_line = ''
    for char in chars:
        clean_line = line.replace(char, '')
    return clean_line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
