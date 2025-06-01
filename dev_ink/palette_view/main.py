from .ui import PaletteView

def Palette_view(folder:str):
    app = PaletteView(folder)
    app.mainloop()

if __name__ == "__main__":
    PaletteView("place_holder")