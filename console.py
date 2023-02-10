#!/usr/bin/env python3
import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None
    class_name = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                  'Review']

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
        'Prints all str rep. of all instances based or not on the class name'
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

    def do_update(self, line):
        'Updates an instance based on the class name and id by adding \
        or updating attributes'
        arg = line.split(maxsplit=3)
        arg_list = {"int": int, "float": float, "str": str}
        try:
            if not line:
                print('** class name missing **')
            elif arg[0] not in self.class_name:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print('** instance id missing **')
            elif arg[0] + '.' + arg[1] not in storage.all():
                print("** no instance found **")
            elif len(arg) < 3:
                print("** attribute name missing **")
            elif len(arg) < 4:
                print("** value missing **")
            else:
                with open('file.json', 'r') as f:
                    objs = json.loads(f.read())
                base = eval(f'{arg[0]}()')
                k, val = arg[2], arg[3].replace('"', '').replace("'", "")
                key = arg[0] + '.' + arg[1]
                typ = type(getattr(base, k, None))
                if typ:
                    if typ.__name__ in arg_list:
                        func = arg_list[typ.__name__]
                        val = func(val)
                obj = objs[key]
                obj[k] = val
                with open('file.json', 'w') as f:
                    json.dump(objs, f, indent=4)
        except Exception as err:
            print(err)

    def do_quit(self, line):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, line):
        'EOF or ctrl^D command to exit the program'
        return True

    def emptyline(self):
        """Do nothing when empty line and enter is receive."""
        pass

    def default(self, line):
        """Find the right cmd and execute it"""
        cmd = {
                'all': self.do_all,
                'count': self.count,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
            }

        if '{' in line and '}' in line:
            #self.update_dict(line)
            pass
        else:
            arg = line.replace('.', ' ').replace('(', " ").replace(')', "")
            arg = arg.replace("'", '"').replace('"', "", 4)
            arg = arg.replace(',', "").split()

            if len(arg) < 2:
                return super().default(line)

            if arg[1] in cmd:
                func = cmd[arg[1]]
                if arg[1] == 'show':
                    arg[0] = arg[0] + ' ' + arg[2]
                if arg[1] == 'destroy':
                    arg[0] = arg[0] + ' ' + arg[2]
                if arg[1] == 'update':
                    arg[0] = arg[0] + ' ' + arg[2] + ' ' + arg[3] + ' ' + arg[4]
                func(arg[0])
            else:
                return super().default(line)

    def count(self, line):
        """Retrieves the number of instances of a class"""
        if line not in self.class_name:
            print("** class doesn't exist **")
            return
        try:
            with open('file.json', 'r') as f:
                objs = json.loads(f.read())
        except Exception:
            pass
        count = 0
        for obj in objs.values():
            name = obj['__class__']
            if name == line:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
