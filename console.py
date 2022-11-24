#!/usr/bin/python3
"""console.py that contains the entry point of the command interpreter"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Class inheritance of cmd"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF methode for exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line:
            args = line.split()
            try:
                base_cls = models.args[0]()
                base_cls.save()
                print(base_cls.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        if line:
            args = line.split()
            try:
                temp = models.args[0]()
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
