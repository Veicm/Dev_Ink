import json
import os
from pathlib import Path
import colorsys
from dev_ink.color_view.utils import hex_to_rgb

def hue_sort_key(entry):
    '''This function generates a key which is needed to sort the colors.'''
    r, g, b = [v / 255 for v in hex_to_rgb(entry["color"])]
    h, _, _ = colorsys.rgb_to_hls(r, g, b)
    return h  # returns the required key

def get_db_path():
    try:
        default_path = Path(__file__).resolve().parent.parent / "db.json"
        
        with open(default_path, "r"):
            pass
        
        return default_path
    
    except (PermissionError, FileNotFoundError):
        return Path.home() / ".config" / "dev_ink" / "db.json"

class StorageManager:
    '''This class handles the interaction with the storage, it is optimized for color handling.'''
    def __init__(self, folder:str, palette:str, path=None):
        self.folder = folder
        self.palette = palette
        self.path = path or get_db_path()
        self._ensure_file()

    def _ensure_file(self):
        '''This function ensures that the given file exits.'''
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _read_data(self):
        '''This function reads and returns the data from the json file.'''
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    def _write_data(self, data):
        '''This function is used to write data to the json file.'''
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def list_colors(self):
        '''This function returns a list of all colors in the palette, sorted by their color value.'''
        data = self._read_data()
        return sorted(data[self.folder][self.palette], key=hue_sort_key)
    
    def add_color(self, name:str, color:str):
        '''This function adds a new color to the palette.'''
        data = self._read_data()
        for entry in data[self.folder][self.palette]:
            if entry["name"] == name or entry["color"].lower() == color.lower():
                print("The color already exists.")
                return  # aport without saving
        data[self.folder][self.palette].append({"name": name, "color": color})
        self._write_data(data)

    def delete_color(self, name:str, color:str):
        '''This function is used to delete a color.'''
        data = self._read_data()

        # Deletes the given color
        data[self.folder][self.palette] = [
            entry for entry in data[self.folder][self.palette]
            if not (entry["name"] == name and entry["color"] == color)
        ]
        self._write_data(data)