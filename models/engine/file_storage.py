#!/usr/bin/python3
"""This module defines the FileStorage class."""
import json

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                file_content = file.read()
                print("File content:", file_content)  # Add this line
                if file_content:
                    obj_dict = json.loads(file_content)
                    for key, obj_data in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        obj_class = globals()[class_name]
                        obj_instance = obj_class(**obj_data)
                        self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
