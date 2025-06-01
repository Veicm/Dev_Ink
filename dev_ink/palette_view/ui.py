import customtkinter as ctk
from .storage import StorageManager
from theme_view.main import Theme_view
# There is another import in "go back"

class PaletteView(ctk.CTk):
    def __init__(self, folder:str):
        super().__init__()

        self.manager = StorageManager(folder)

        self.folder = folder

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

        self.top_frame.columnconfigure(0, weight=1)  # Entry should extant
        self.top_frame.columnconfigure(1, weight=0)

        self.name_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Theme name")
        self.name_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))

        self.save_button = ctk.CTkButton(self.top_frame, text="Save", command=lambda: self.save_palette())
        self.save_button.grid(row=0, column=1)

        self.list_frame = ctk.CTkScrollableFrame(self, label_text=self.folder)
        self.list_frame.pack(padx=10, pady=(0,10), fill="both", expand=True)

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(padx=10, pady=(0, 10), fill="x")

        self.delete_button = ctk.CTkButton(self.bottom_frame, text="Delete", command=lambda: self.delete_palette())
        self.delete_button.pack(side="left", padx=5)

        self.load_button = ctk.CTkButton(self.bottom_frame, text="reload", command=lambda: self.reload())
        self.load_button.pack(side="right", padx=5)

        self.bottom_button = ctk.CTkButton(self.bottom_frame, text="<", command=lambda: self.go_back())
        self.bottom_button.pack(pady=10)

    def reload(self):
        '''This function is used to reset and build the dynamic part of the ui.'''
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        data = self.manager.list_palettes()
        for entry in data:
            palette = entry


            row = ctk.CTkFrame(self.list_frame, height=30)
            row.pack(pady=5, fill="x", padx=5)
            row.bind("<Button-1>", lambda e, p=palette: self.select_palette(p))
            row.bind("<Double-Button-1>", lambda e, p=palette: self.open_theme_view(p))

            box = ctk.CTkFrame(row, width=30, height=30, fg_color="#1F538D")# main button color
            box.pack(side="left", padx=(0,10))
            box.pack_propagate(False)
            box.bind("<Button-1>", lambda e, p=palette: self.select_palette(p))
            box.bind("<Double-Button-1>", lambda e, p=palette: self.open_theme_view(p))

            label = ctk.CTkLabel(row, text=f"{palette}")
            label.pack(side="left")
            label.bind("<Button-1>", lambda e, p=palette: self.select_palette(p))
            label.bind("<Double-Button-1>", lambda e, p=palette: self.open_theme_view(p))

        self.name_entry.delete(0, "end")

    def select_palette(self, palette:str):
        '''This function is used to select a palette in order execute father functions.'''
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, palette)

    def open_theme_view(self, palette:str):
        '''This function will rebuild the window in order to show the colors inside a certain palette.'''
        self.destroy()
        Theme_view(self.folder, palette)
    
    def save_palette(self):
        '''This function will pass on the name of a palette to the StorageManager class and saves the palette.'''
        palette = self.name_entry.get()
        if palette == "":
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, "please enter a name for your palette.")
        else:
            self.manager.add_palette(palette)
            self.reload()

    def delete_palette(self):
        '''This function will pass on the name of a palette to the StorageManager class and deletes the palette.'''
        palette = self.name_entry.get()
        if palette == "":
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, "Please select the palette you want to delete.")
        else:
            self.manager.delete_palette(palette)
            self.reload()

    def go_back(self):
        '''This function is used to go back to the last instance of the ui.'''
        from folder_view.main import Folder_view # lazy import
        self.destroy()
        Folder_view()