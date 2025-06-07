import json
import os
import shutil

def get_db_path():
    user_path = os.path.join(os.path.expanduser('~'), '.config', 'dev_ink', 'db.json')
    system_path = '/usr/share/dev_ink/db.json'

    # Sicherstellen, dass ~/.config/dev_ink existiert
    os.makedirs(os.path.dirname(user_path), exist_ok=True)

    # Falls keine nutzerdefinierte db.json existiert → kopieren
    if not os.path.isfile(user_path):
        shutil.copyfile(system_path, user_path)

    return user_path

class StorageManager:
    '''This class handles the interaction with the storage, it is optimized for folder handling.'''
    def __init__(self, path=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.path = path or os.path.join(base_dir, "..", "db.json") or get_db_path()
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
        '''This function returns a alphabetical sorted list of all folders.'''
        data = self._read_data()
        return sorted(data.keys())

    def add_folder(self, folder_name:str):
        '''This function adds a new empty folder with a given name to the json file.'''
        data = self._read_data()
        if folder_name not in data:
            data[folder_name] = {}
            self._write_data(data)

    def delete_folder(self, folder_name:str):
        '''This function is used to delete a folder.'''
        data = self._read_data()
        if folder_name in data:
            del data[folder_name]
            self._write_data(data)