#!/usr/bin/python3
"""console.py that contains the entry point of the command interpreter"""

import cmd
import re
import shlex
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

objs = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Class inheritance of cmd"""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF methode for exit"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """free line"""
        pass

    def do_create(self, args):
        """
        creates a new instance of basemodel
        arg: Class name
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            if args in objs:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        prints the string representation of an instance
        arg 1: class name | arg 2: di
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            sp = args.split()
            if sp[0] in objs:
                if len(sp) < 2:
                    print("""** instance id missing **""")
                else:
                    Objcls = models.storage.all()
                    key = str(sp[0]) + "." + str(sp[1])
                    if key in Objcls:
                        print(Objcls[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name
        arg 1: class name | arg 2: id
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            sp = args.split()
            if sp[0] in objs:
                if len(sp) < 2:
                    print("""** instance id missing **""")
                else:
                    Objcls = models.storage.all()
                    key = str(sp[0]) + "." + str(sp[1])
                    if key in Objcls:
                        del(Objcls[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        argument (optional): class name
        """
        Objcls = models.storage.all()
        objects = []
        if args is "":
            for key in Objcls:
                objects.append(str(Objcls[key]))
            print(objects)
        else:
            try:
                sp = args.split()
                eval(sp[0])
                for obj in Objcls:
                    _dict = Objcls[obj].to_dict()
                    if _dict['__class__'] == sp[0]:
                        objects.append(str(Objcls[obj]))
                print(objects)
            except Exception:
                print("** class doesn't exist **")

    def do_update(self, args):
        """
        updates an instance based on name and  id
        arg 1: class name | arg 2: id
        """
        sp = shlex.split(args)
        if len(sp) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(sp[0]))
            except Exception:
                print("** class doesn't exist **")
                return
            if len(sp) == 1:
                print("** instance id missing **")
            else:
                Objcls = models.storage.all()
                attr = str(sp[0]) + "." + str(sp[1])
                if attr not in Objcls:
                    print("** no instance found **")
                else:
                    if len(sp) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(sp) == 3:
                            print("** value missing **")
                        else:
                            setattr(Objcls[attr], sp[2], sp[3])
                            models.storage.save()

    def do_count(self, args):
        """Count the number of instances of a class"""
        nb_objects = 0
        objects = models.storage.all()
        new = {}
        for obj in objects:
            new[obj] = objects[obj].to_dict()
        for n_obj in new:
            if (args == new[n_obj]['__class__']):
                nb_objects = nb_objects + 1
        print(nb_objects)

    def default(self, args):
        """
        creates a new instance of basemodel
        args: Class name + .all()
        """
        sp = args.split(".")
        if sp[0] in objs and sp[1] == "all()":
            self.do_all(sp[0])
        elif sp[0] in objs and sp[1] == "count()":
            self.do_count(sp[0])
        elif sp[0] in objs and sp[1].startswith('show'):
            sp2 = sp[1].split('"')
            if len(sp2) == 3:
                arg = sp[0] + " " + sp2[1]
                self.do_show(arg)
        elif sp[0] in objs and sp[1].startswith('destroy'):
            sp2 = sp[1].split('"')
            if len(sp2) == 3:
                arg = sp[0] + " " + sp2[1]
                self.do_destroy(arg)
        elif sp[0] in objs and sp[1].startswith('update'):
            start = 'update('
            end = ')'
            sp2 = re.findall(re.escape(start)+"(.*)"+re.escape(end), sp[1])[0]
            sp2 = sp2.replace('(', '').replace(')', '').replace(',', '')
            sp2 = sp2.replace('"', '')
            arg = sp[0] + " " + sp2
            self.do_update(arg)
        else:
            print("*** Unknown syntax: {}".format(args))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
