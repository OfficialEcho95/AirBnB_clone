#!/usr/bin/env python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Exits the program'
        return True

    def emptyline(self):
        pass

    def default(self, arg):
        print(arg, "is not a valid command")
        print("Type 'help' to see list of available commands\n")


if __name__=='__main__':
    import sys
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
