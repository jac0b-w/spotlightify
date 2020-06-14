from copy import deepcopy
from typing import overload

from definitions import ASSETS_DIR, CACHE_DIR
from os import sep

class BaseCommand:
    def __init__(self, title: str, description: str, icon_name: str, function: classmethod, parameter: str, prefix: str, setting: str):
        self._command_dict = {"title": "str", "description": "str", "icon": "path_str", "function": classmethod,
                              "parameter": "traceback._some_str", "prefix": "str", "setting": "fill/exe/fill"}  # command in dictionary form
        self.prefix = prefix
        self._populate_command_dict(title, description, icon_name, function, parameter, prefix, setting)

    def _populate_command_dict(self, title: str, description: str, icon_name: str, function: classmethod, parameter: str, prefix: str, setting: str):
        self._command_dict["title"] = title
        self._command_dict["description"] = description
        if not len(icon_name) > 20:
            self._command_dict["icon"] = f"{ASSETS_DIR}svg{sep}{icon_name}.svg"
        else:
            self._command_dict["icon"] = f"{CACHE_DIR}art{sep}{icon_name}.jpg"
        self._command_dict["function"] = function
        self._command_dict["parameter"] = parameter
        self._command_dict["prefix"] = prefix
        self._command_dict["setting"] = setting
    
    def _populate_new_dict(self, title: str, description: str, icon_name: str, parameter: str, setting: str) -> dict:
        """Populates and returns a command dictionary with custom attributes

        Args:
            title (str): Title of command
            description (str): [description]
            icon_name (str): icon name or name of album art in cache (this is a 20+ char ID)
            parameter (str): parameter associated with the command, usually left as  ""
            setting (str): setting of the command either: fill, exe, list or none

        Returns:
            dict: a custom command dictionary based on the _command_dict of the current object
        """
        new_dict = deepcopy(self._command_dict)
        new_dict["title"] = title
        new_dict["description"] = description
        if not len(icon_name) > 20:
            new_dict["icon"] = f"{ASSETS_DIR}svg{sep}{icon_name}.svg"
        else:
            new_dict["icon"] = f"{CACHE_DIR}art{sep}{icon_name}.jpg"
        new_dict["parameter"] = parameter
        new_dict["setting"] = setting
        return new_dict

    def get_dicts(self, parameter: str) -> list:
        """

        Args:
            parameter (str): parameter is used on other child classes to add more command dictionaries to the list

        Returns:
            list: returns the commands dictionaries associated with the current class
        """
        return [self._command_dict]