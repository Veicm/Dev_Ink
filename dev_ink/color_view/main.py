from .ui import ColorView

def Color_view(folder, palette,name, color):
    app = ColorView(folder, palette,name, color)
    app.mainloop()

if __name__ == "__main__":
    Color_view("Place holder", "Place holder", "example", "#0000ff")