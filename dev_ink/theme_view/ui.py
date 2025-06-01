import customtkinter as ctk
from .storage import StorageManager
from .color_picker import select_color
from dev_ink.color_view.main import Color_view
# There is another import in "go back"

class ThemeView(ctk.CTk):
    def __init__(self, folder:str, palette:str):
        super().__init__()

        self.folder = folder
        self.palette = palette

        self.title("Dev Ink")
        self.geometry("500x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.manager = StorageManager(folder, palette)

        self.build_ui()
        self.reload()

    def build_ui(self):
        '''This function builds the static part of the ui.'''
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(padx=10, pady=10, fill="x")

        self.color_button = ctk.CTkButton(self.top_frame, text="Select a color", command=self.color_selector)
        self.color_button.pack(side="left", padx=(0, 10))

        self.color_entry = ctk.CTkEntry(self.top_frame, placeholder_text="Color (Hex value)")
        self.color_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Color name")
        self.name_entry.pack(padx=10, pady=(0, 10), fill="x")

        self.save_button = ctk.CTkButton(self.top_frame, text="Save", command=lambda: self.save_color())
        self.save_button.pack(side="left")

        self.list_frame = ctk.CTkScrollableFrame(self, label_text=self.palette)
        self.list_frame.pack(padx=10, pady=(0,10), fill="both", expand=True)

        self.bottom_frame = ctk.CTkFrame(self)
        self.bottom_frame.pack(padx=10, pady=(0, 10), fill="x")

        self.delete_button = ctk.CTkButton(self.bottom_frame, text="Delete", command=lambda: self.delete_color())
        self.delete_button.pack(side="left", padx=5)

        self.load_button = ctk.CTkButton(self.bottom_frame, text="reload", command=self.reload)
        self.load_button.pack(side="right", padx=5)

        self.bottom_button = ctk.CTkButton(self.bottom_frame, text="<", command=lambda: self.go_back())
        self.bottom_button.pack(pady=10)

    def reload(self):
        '''This function is used to reset and build the dynamic part of the ui.'''
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        data = self.manager.list_colors()
        for entry in data:
            name = entry["name"]
            color = entry["color"]

            row = ctk.CTkFrame(self.list_frame, height=30)
            row.pack(pady=5, fill="x", padx=5)
            row.bind("<Button-1>", lambda e, n=name, c=color: self.select_color(n, c))
            row.bind("<Double-Button-1>", lambda e, n=name, c=color: self.open_color_view(n, c))

            box = ctk.CTkFrame(row, width=30, height=30, fg_color=color)
            box.pack(side="left", padx=(0,10))
            box.pack_propagate(False)
            box.bind("<Button-1>", lambda e, n=name, c=color: self.select_color(n, c))
            box.bind("<Double-Button-1>", lambda e, n=name, c=color: self.open_color_view(n, c))

            label = ctk.CTkLabel(row, text=f"{name} ({color})")
            label.pack(side="left")
            label.bind("<Button-1>", lambda e, n=name, c=color: self.select_color(n, c))
            label.bind("<Double-Button-1>", lambda e, n=name, c=color: self.open_color_view(n, c))

        self.name_entry.delete(0, "end")
        self.color_entry.delete(0, "end")

    def select_color(self, name, color):
        '''This function is used to select a color in order execute father functions.'''
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, name)

        self.color_entry.delete(0, "end")
        self.color_entry.insert(0, color)

    def open_color_view(self, name, color):
        '''This function will rebuild the window in order to show a more detailed version of a certain color.'''
        self.destroy()
        Color_view(self.folder, self.palette, name, color)

    def save_color(self):
        '''This function will pass on the name and value of a color to the StorageManager class and saves the color.'''
        name = self.name_entry.get()
        color = self.color_entry.get()
        if color == "" or not color.startswith("#"):
            self.color_entry.delete(0, "end")
            self.color_entry.insert(0, "Please select a color in hex value.")
        elif name == "":
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, "Please enter a name for your color.")
        else:
            self.manager.add_color(name, color)
            self.reload()

    def delete_color(self):
        '''This function will pass on the name and value of a color to the StorageManager class and deletes the color.'''
        name = self.name_entry.get()
        color = self.color_entry.get()
        if color == "" or name == "":
            self.name_entry.delete(0, "end")
            self.color_entry.delete(0, "end")

            self.name_entry.insert(0, "Please select the color you want to delete")
            self.color_entry.insert(0, "Please select the color you want to delete")
        else:
            self.manager.delete_color(name, color)
            self.reload()

    def color_selector(self):
        '''This function opens the color picker.'''
        color = select_color()
        if color:
            self.color_entry.delete(0, "end")
            self.color_entry.insert(0, color)

    def go_back(self):
        '''This function is used to go back to the last instance of the ui.'''
        from dev_ink.palette_view.main import Palette_view # lazy import
        self.destroy()
        Palette_view(self.folder)