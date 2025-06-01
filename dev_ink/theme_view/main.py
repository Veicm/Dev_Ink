from .ui import ThemeView

def Theme_view(folder:str, palette:str):
    app = ThemeView(folder, palette)
    app.mainloop()

if __name__ == "__main__":
    Theme_view("Place holder", "Place holder")