#!/usr/bin/env python3
import cmd
import json
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None
    class_name = ['BaseModel']

    def do_create(self, line):
        'Creates a new instance from class_name[]'
        if not line:
            print("** class name missing **")
        elif line not in self.class_name:
            print("** class doesn't exist **")
        else:
            base = eval(f'{line}()')
            base.save()
            print(base.id)

    def do_show(self, line):
        'Prints the string rep. of an instance based on the class name and id'
        arg = line.split()
        if not line:
            print('** class name missing **')
        elif not arg[0] in self.class_name:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print('** instance id missing **')
        else:
            id_ = arg[0] + '.' + arg[1]
            try:
                with open('file.json', 'r')as f:
                    objs = json.loads(f.read())
                if id_ in objs:
                    max_ = objs[id_]
                    name = max_['__class__']
                    base = eval(f"{name}(**max_)")
                    print(base)
                else:
                    print('** no instance found **')
            except Exception:
                print('** no instance found **')

    def do_destroy(self, line):
        'Deletes an instance base on class name and id'
        arg = line.split()
        if not line:
            print('** class name missing **')
        elif not arg[0] in self.class_name:
            print("** class doesn't exist **")
        elif len(arg) != 2:
            print('** instance id missing **')
        else:
            id_ = arg[0] + '.' + arg[1]
            try:
                with open('file.json', 'r')as f:
                    objs = json.loads(f.read())
                if id_ in objs:
                    del objs[id_]
                    with open('file.json', 'w')as f:
                        json.dump(objs, f, indent=4)
                else:
                    print('** no instance found **')
            except Exception:
                print('** no instance found **')
    def do_all(self, line):
        'Prints all string rep. of all instances based or not on the class name'
        obj_list = []
        objs = {}
        try:
            with open('file.json', 'r') as f:
                objs = json.loads(f.read())
        except Exception:
            pass
        if not line:
            for obj in objs.values():
                name = obj['__class__']
                base = eval(f"{name}(**obj)")
                obj_list.append(str(base))
            print(obj_list)
        elif line not in self.class_name:
            print("** class doesn't exist **")
        else:
            for obj in objs.values():
                name = obj['__class__']
                if name == line:
                    base = eval(f"{name}(**obj)")
                    obj_list.append(str(base))
            print(obj_list)

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'Exits the program'
        return True

    def emptyline(self):
        pass

    def default(self, line):
        print(line, "is not a valid command")
        print("Type 'help' to see list of available commands\n")


if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
