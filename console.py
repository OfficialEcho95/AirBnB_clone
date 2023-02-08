#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None
    class_name = ['BaseModel']

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in self.class_name:
            print("** class doesn't exist **")
        else:
            base = eval(f'{line}()')
            base.save()
            print(base.id)


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
