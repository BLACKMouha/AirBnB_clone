#!/usr/bin/python3
'''
HBNB Command Interpreter
'''
import cmd
from models.base_model import BaseModel
import models

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

    def do_create(self, line):
        '''
        Create an instance
        '''
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        cls_name = args[0]
        if cls_name != 'BaseModel':
            print("** class doesn't exist **")
            return
        obj = eval(cls_name)()
        obj.save()
        print(obj.id)
        return

    def do_show(self, line):
        '''
        Prints an instance based on its class and id
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name != 'BaseModel':
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
        return

    def do_destroy(self, line):
        '''
        Deletes an instance based on the class name and id.
        Changes are saved in the JSON file too.
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name != 'BaseModel':
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
        return

    def do_all(self, line):
        '''
        Prints all string representation of all instances based or not on the
        class name
        '''
        args = line.split()
        cls_name = args[0] if len(args) != 0 else None
        list_objs = []
        if cls_name is None:
            for v in models.storage.all().values():
                list_objs.append(str(v))
        else:
            if cls_name != 'BaseModel':
                print("** class doesn't exist **")
                return
            else:
                for v in models.storage.all().values():
                    if cls_name == v.__class__.__name__:
                        list_objs.append(str(v))
        print(list_objs)
        return

    def do_update(self, line):
        '''
        Updates an instance based on the class name and id by adding or
        updating attributes.
        All changes are automatically save in the JSON file
        '''
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name != 'BaseModel':
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
        return

    def do_clear(self, line):
        '''
        Clear command interpreter
        '''
        from os import system
        system('clear')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
