import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Tuple
from threading import Thread
from .app import App
from pathlib import Path
from .color import Color



class Splash(Forms.Form):
    """
    Args:
        - image (Optional[Path]): The path to the image file to be displayed on the splash screen.
        - size (Tuple[int, int], optional): The desired size of the splash screen. If None, the size will be set to the dimensions of the image.
        - clean_color (Optional[Color]): A color that will be made transparent (if set).
        - location (Tuple[int, int], default (0, 0)): The location on the screen where the splash screen will be displayed if `center_screen` is False.
        - center_screen (bool, default False): If True, the splash screen will be centered on the screen. If False, it will be positioned based on `location`.
        - timing (Optional[int], default 5): The time (in seconds) the splash screen will be displayed before it closes. Defaults to 5 seconds if None.
    """
    def __init__(
        self,
        image: Optional[Path] = None,
        size: Tuple[int, int] = None,
        clean_color: Optional[Color] = None,
        location: Tuple[int, int] = (0, 0),
        center_screen: bool = False,
        timing: Optional[int] = 5
    ):
        """
        Args:
            - image (Optional[Path]): The path to the image file to be displayed on the splash screen.
            - size (Tuple[int, int], optional): The desired size of the splash screen. If None, the size will be set to the dimensions of the image.
            - clean_color (Optional[Color]): A color that will be made transparent (if set).
            - location (Tuple[int, int], default (0, 0)): The location on the screen where the splash screen will be displayed if `center_screen` is False.
            - center_screen (bool, default False): If True, the splash screen will be centered on the screen. If False, it will be positioned based on `location`.
            - timing (Optional[int], default 5): The time (in seconds) the splash screen will be displayed before it closes. Defaults to 5 seconds if None.
        """
        
        super().__init__()
        self._image = image
        self._size = size
        self._clean_color = clean_color
        self._location = location
        self._center_screen = center_screen
        self._timing = timing

        app_icon = App.get_icon()
        if app_icon:
            self.Icon = app_icon

        if center_screen:
            self.StartPosition = Forms.FormStartPosition.CenterScreen
        else:
            self.StartPosition = Forms.FormStartPosition.Manual
            self.Location = Drawing.Point(self._location[0], self._location[1])

        splash_image = Drawing.Image.FromFile(str(self._image))

        if not self._size:
            self._size = (splash_image.Width, splash_image.Height)

        self.BackgroundImage = splash_image
        self.ClientSize = Drawing.Size(self._size[0], self._size[1])

        self.FormBorderStyle = Forms.FormBorderStyle(0)

        if self._clean_color:
            self.TransparencyKey = self._clean_color

        self.BackgroundImageLayout = Forms.ImageLayout.Zoom

    
    def show(self):

        def show_splash():
            Forms.Application.Run(self)

        thread = Thread(target=show_splash)
        thread.start()

        thread.join(4)

        self.Close()