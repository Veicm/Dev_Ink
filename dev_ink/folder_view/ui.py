import customtkinter as ctk
from .storage import StorageManager
from dev_ink.palette_view.main import Palette_view

class FolderView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.manager = StorageManager()

        self.title("Dev Ink")
        self.geometry("500x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.build_ui()
        self.reload()

    def build_ui(self):
        '''This function builds the static part of the ui.'''
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(padx=10, pady=10, fill="x")

        self.top_frame.columnconfigure(0, weight=1)  # Entry should expand
        self.top_frame.columnconfigure(1, weight=0)

        self.name_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Folder name")
        self.name_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.save_button = ctk.CTkButton(self.top_frame, text="Save", command=lambda: self.save_folder())
        self.save_button.grid(row=0, column=1)


        self.list_frame = ctk.CTkScrollableFrame(self, label_text="Dev Ink")
        self.list_frame.pack(padx=10, pady=(0,10), fill="both", expand=True)


        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(padx=10, pady=(0, 10), fill="x")

        self.delete_button = ctk.CTkButton(self.bottom_frame, text="Delete", command=lambda: self.delete_folder())
        self.delete_button.pack(side="left", padx=5)

        self.load_button = ctk.CTkButton(self.bottom_frame, text="reload", command=lambda: self.reload())
        self.load_button.pack(side="right", padx=5)

    def reload(self):
        '''This function resets and build the dynamic part of the ui.'''
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        data = self.manager.list_palettes()
        for entry in data:
            folder = entry


            row = ctk.CTkFrame(self.list_frame, height=30)
            row.pack(pady=5, fill="x", padx=5)
            row.bind("<Button-1>", lambda e, f=folder: self.select_folder(f))
            row.bind("<Double-Button-1>", lambda e, f=folder: self.open_palette_view(f))

            box = ctk.CTkFrame(row, width=30, height=30, fg_color="#1F538D")# main button color
            box.pack(side="left", padx=(0,10))
            box.pack_propagate(False)
            box.bind("<Button-1>", lambda e, f=folder: self.select_folder(f))
            box.bind("<Double-Button-1>", lambda e, f=folder: self.open_palette_view(f))

            label = ctk.CTkLabel(row, text=f"{folder}")
            label.pack(side="left")
            label.bind("<Button-1>", lambda e, f=folder: self.select_folder(f))
            label.bind("<Double-Button-1>", lambda e, f=folder: self.open_palette_view(f))

        self.name_entry.delete(0, "end")

    def select_folder(self, folder:str):
        '''This function is used to select a folder in order execute father functions.'''
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, folder)

    def open_palette_view(self, folder:str):
        '''This function will rebuild the window in order to show the palettes inside a certain folder.'''
        self.destroy()
        Palette_view(folder)
    
    def save_folder(self):
        '''This function will pass on the name of a folder to the StorageManager class and saves the folder.'''
        folder = self.name_entry.get()
        if folder == "":
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, "please enter a name for your folder.")
        else:
            self.manager.add_folder(folder)
            self.reload()

    def delete_folder(self):
        '''This function will pass on the name of a folder to the StorageManager class and deletes the folder.'''
        folder = self.name_entry.get()
        if folder == "":
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, "please select the folder you want to delete.")
        else:
            self.manager.delete_folder(folder)
            self.reload()