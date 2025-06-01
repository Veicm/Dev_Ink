import customtkinter as ctk
from .utils import hex_to_hsl, hex_to_rgb, hex_to_hwb, hex_to_lab, hex_to_lch, copy_to_clipboard
# There is another import in "go back"

class ColorView(ctk.CTk):
    def __init__(self, folder, palette, name, hex_color):
        super().__init__()

        self.folder = folder
        self.palette = palette

        self.name = name

        self.hex = hex_color
        self.rgb = hex_to_rgb(hex_color)
        self.hsl = hex_to_hsl(hex_color)
        self.hwb = hex_to_hwb(hex_color)
        self.lab = hex_to_lab(hex_color)
        self.lch = hex_to_lch(hex_color)

        self.title("Dev Ink")
        self.geometry("500x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.build_ui()

    def build_ui(self):
        '''this function is used to build the ui.'''
        self.headline = ctk.CTkLabel(self, text=self.name, font=("Arial", 24, "bold"))
        self.headline.pack(pady=(10, 0))

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.main_frame.columnconfigure(0, weight=3)
        self.main_frame.columnconfigure(1, weight=2)
        self.main_frame.rowconfigure(0, weight=1)

        self.color_frame = ctk.CTkFrame(self.main_frame, fg_color=self.hex)
        self.color_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))


        self.info_frame = ctk.CTkFrame(self.main_frame)
        self.info_frame.grid(row=0, column=1, sticky="nsew")

        self.info_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.label_hex = ctk.CTkLabel(self.info_frame, text=f"{self.hex} (click to copy)")
        self.label_hex.grid(row=0, column=0, pady=10)
        self.label_hex.bind("<Button-1>", lambda e: copy_to_clipboard(f"{self.hex}"))

        self.label_rgb = ctk.CTkLabel(self.info_frame, text=f"rgb{self.rgb} (click to copy)")
        self.label_rgb.grid(row=1, column=0, pady=10)
        self.label_rgb.bind("<Button-1>", lambda e: copy_to_clipboard(f"rgb{self.rgb}"))

        self.label_hsl = ctk.CTkLabel(self.info_frame, text=f"hsl{self.hsl} (click to copy)")
        self.label_hsl.grid(row=2, column=0, pady=10)
        self.label_hsl.bind("<Button-1>", lambda e: copy_to_clipboard(f"hsl{self.hsl}"))

        self.label_hwb = ctk.CTkLabel(self.info_frame, text=f"hwb{self.hwb} (click to copy)")
        self.label_hwb.grid(row=3, column=0, pady=10)
        self.label_hwb.bind("<Button-1>", lambda e: copy_to_clipboard(f"hwb{self.hwb}"))

        self.label_lab = ctk.CTkLabel(self.info_frame, text=f"lab{self.lab} (click to copy)")
        self.label_lab.grid(row=4, column=0, pady=10)
        self.label_lab.bind("<Button-1>", lambda e: copy_to_clipboard(f"lab{self.lab}"))

        self.label_lch = ctk.CTkLabel(self.info_frame, text=f"lch{self.lch} (click to copy)")
        self.label_lch.grid(row=5, column=0, pady=10)
        self.label_lch.bind("<Button-1>", lambda e: copy_to_clipboard(f"lch{self.lch}"))


        self.bottom_frame = ctk.CTkFrame(self, height=50)
        self.bottom_frame.pack(fill="x", padx=10, pady=(10, 20))

        self.bottom_button = ctk.CTkButton(self.bottom_frame, text="<", command=lambda: self.go_back())
        self.bottom_button.pack(pady=10)  # center button

    def go_back(self):
        '''This function is used to go back to the last instance of the ui.'''
        from theme_view.main import Theme_view # lazy import
        self.destroy()
        Theme_view(self.folder, self.palette)