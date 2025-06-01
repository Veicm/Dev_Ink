import json
import os

class StorageManager:
    '''This class handles the interaction with the storage, it is optimized for palette handling.'''
    def __init__(self, folder:str, path=None):
        self.folder = folder
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.path = path or os.path.join(base_dir, "..", "db.json")
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

    def list_palettes(self):
        '''This function returns a alphabetical sorted list of all palette in the folder.'''
        data = self._read_data()
        return sorted(data[self.folder].keys())

    def add_palette(self, palette_name: str):
        '''This function adds a new empty palette with a given name to the folder.'''
        data = self._read_data()
        if palette_name not in data[self.folder]:
            data[self.folder][palette_name] = []
            self._write_data(data)

    def delete_palette(self, palette_name: str):
        '''This function is used to delete a palette.'''
        data = self._read_data()
        if self.folder in data and palette_name in data[self.folder]:
            del data[self.folder][palette_name]
            self._write_data(data)