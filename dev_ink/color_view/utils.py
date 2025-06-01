import colorsys
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_objects import sRGBColor, LCHabColor
import pyperclip

def copy_to_clipboard(text:str):
    '''This function is used to copy a given text into the system clipboard.'''
    pyperclip.copy(text)


def hex_to_rgb(hex_color):
    '''This function converts hex values to rgb values.'''
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def hex_to_hsl(hex_color):
    '''This function converts hex values to hsl values.'''
    r, g, b = [x / 255.0 for x in hex_to_rgb(hex_color)]
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2

    if max_c == min_c:
        h = s = 0
    else:
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        elif max_c == b:
            h = (r - g) / d + 4
        h /= 6

    return f"({round(h*360)}, {round(s*100)}%, {round(l*100)}%)"

def hex_to_hwb(hex_color):
    '''This function converts hex values to hwb values.'''
    r, g, b = [x / 255.0 for x in hex_to_rgb(hex_color)]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    w = min(r, g, b)
    b = 1 - max(r, g, b)
    return f"({round(h*360)}, {round(w*100)}%, {round(b*100)}%)"

def hex_to_lab(hex_color):
    '''This function converts hex values to lab values.'''
    r, g, b = hex_to_rgb(hex_color)
    rgb = sRGBColor(r, g, b, is_upscaled=True)
    lab = convert_color(rgb, LabColor)
    return f"({round(lab.lab_l, 2)}, {round(lab.lab_a, 2)}, {round(lab.lab_b, 2)})"

def hex_to_lch(hex_color):
    '''This function converts hex values to lch values.'''
    r, g, b = hex_to_rgb(hex_color)
    rgb = sRGBColor(r, g, b, is_upscaled=True)
    lch = convert_color(rgb, LCHabColor)
    return f"({round(lch.lch_l, 2)}, {round(lch.lch_c, 2)}, {round(lch.lch_h, 2)})"