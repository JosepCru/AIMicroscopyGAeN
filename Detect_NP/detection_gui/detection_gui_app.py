import customtkinter as ctk
import os
import sys

sys.path.append(os.path.abspath('.'))

from settings import Frame_settings

class Detection_gui(ctk.CTk):
    def __init__(self, project_path = os.path.abspath('detection_gui'), *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.project_path = project_path
        print(self.project_path)
        # Window theme
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        # Inizialicing window
        self.geometry('1300x800+50+50')
        self.title('Labeling app')

        # Window icon
        icon_path = os.path.join(self.project_path, "assets", "icons", "Group_icon.ico")
        self.iconbitmap(icon_path)
        
        # Frames set up
        self.frame_acquisition = ctk.CTkFrame(self)
        self.frame_images = ctk.CTkFrame(self)
        self.frame_settings = Frame_settings(self, self.project_path)

        self.frame_settings.pack(side = 'right', fill = 'both', padx = 5, pady = 5)
        self.frame_acquisition.pack( expand = True, fill = 'both', padx = 5, pady = 5)
        self.frame_images.pack(expand = True, fill = 'both', padx = 5, pady = 5)


if __name__ == '__main__':
    app = Detection_gui()
    app.mainloop()