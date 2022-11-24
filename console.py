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
                models.args[0]()
                if args[1]:
                    key = "{}.{}".format(args[0], args[1])
                    try:
                        print(models.storage.all()[key])
                    except Exception:
                            print("** no instance found **")
                else:
                    print("** instance id missing **")
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line:
            args = line.split()
            try:
                models.args[0]()
                if args[1]:
                    key = "{}.{}".format(args[0], args[1])
                    try:
                        del models.storage.all()[key]
                    except Exception:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        if line:
            try:
                models.line()
                
            except Exception:
                print("** class doesn't exist **")
        else:
            
            
    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if line:
            args = line.split()
            try:
                models.args[0]()
                if args[1]:
                    key = "{}.{}".format(args[0], args[1])
                    if key in models.storage.all():
                        if args[2]:
                            if args[3]:
                                setattr(models.storage.all()[key], args[2], args[3].strip('"'))
                                models.storage.all()[key].save()
                            else:
                                print("** value missing **")
                        else:
                            print("print ** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
