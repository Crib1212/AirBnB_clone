#!/usr/bin/python3

import cmd
import re
import sys
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}
    
    class_mapping = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def emptyline(self):
        pass

    def do_create(self, arg):
        argl = self.parse(arg)
        if not argl:
            sys.stderr.write("** class name missing **\n")
        elif argl[0] not in self.__classes:
            sys.stderr.write("** class doesn't exist **\n")
        else:
            instance = self.class_mapping[argl[0]]()
            print(instance.id)
            storage.save()

    def parse(self, arg):
        return re.findall(r"\{.*?\}|\[.*?\]|[^,]+", arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
