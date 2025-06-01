import tkinter.colorchooser as cc

def select_color():
    '''This function opens the color picker and returns the hex value.'''
    color = cc.askcolor(title="Select a color")
    if color[1]:
        return color[1]
    return None