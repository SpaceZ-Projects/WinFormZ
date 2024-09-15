import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Tuple, Callable
from pathlib import Path
from .color import Color

class ImageBox(Forms.PictureBox):
    """
    Args:
        - image (Path): The path to the image file (.jpg, .png, .bmp), absolute path.
        - size (Tuple[int, int]): The size of the image control (width, height).
        - background_color (Optional[Color]): The background color of the image control.
        - location (Optional[Tuple[int, int]]): The location of the image control (x, y).
        - on_click (Optional[Callable[[], None]]): The callback function to be executed when the image is clicked.
    """

    def __init__(
        self,
        image: Path = None,
        size: Tuple[int, int] = None,
        background_color: Optional[Color] = Color.TRANSPARENT,
        location: Optional[Tuple[int, int]] = (0, 0),
        on_click: Optional[Callable[[], None]] = None
    ):
        """
        Args:
            - image (Path): The path to the image file (.jpg, .png, .bmp), absolute path.
            - size (Tuple[int, int]): The size of the image control (width, height).
            - background_color (Optional[Color]): The background color of the image control.
            - location (Optional[Tuple[int, int]]): The location of the image control (x, y).
            - on_click (Optional[Callable[[], None]]): The callback function to be executed when the image is clicked.
        """
        super().__init__()
        self._image_path = image
        self._size = size
        self._background_color = background_color
        self._location = location
        self._on_click = on_click

        self.BackColor = self._background_color

        if self._location:
            self.Location = Drawing.Point(*self._location)

        if self._image_path:
            self._set_image(self._image_path)


        if self._on_click:
            self.Click += self._handle_click


    def _set_image(self, image_path: Path):
        """Sets the image for the PictureBox from the provided path and adjusts size if necessary."""
        try:
            image = Drawing.Image.FromFile(str(image_path))
            self.Image = image
            
            if self._size is None:
                self._size = (image.Width, image.Height)
                self.Size = Drawing.Size(*self._size)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.Image = None



    @property
    def image_path(self) -> Path:
        return self._image_path
    


    @image_path.setter
    def image_path(self, value: Path):
        self._image_path = value
        if value:
            self._set_image(value)
        else:
            self.Image = None



    @property
    def size(self) -> Tuple[int, int]:
        return self._size
    


    @size.setter
    def size(self, value: Optional[Tuple[int, int]]):
        if value:
            self._size = value
            self.Size = Drawing.Size(*value)
        else:
            if self.Image:
                self._size = (self.Image.Width, self.Image.Height)
                self.Size = Drawing.Size(*self._size)



    @property
    def background_color(self) -> Optional[Color]:
        return self._background_color
    


    @background_color.setter
    def background_color(self, value: Optional[Color]):
        self._background_color = value
        if value:
            self.BackColor = value


    
    @property
    def location(self) -> Tuple[int, int]:
        return self._location
    

    @location.setter
    def location(self, value: Tuple[int, int]):
        self._location = value
        self.Location = Drawing.Point(*value)



    @property
    def on_click(self) -> Optional[Callable[[], None]]:
        return self._on_click
    



    @on_click.setter
    def on_click(self, value: Optional[Callable[[], None]]):
        if self._on_click:
            self.Click -= self._handle_click
        self._on_click = value
        if self._on_click:
            self.Click += self._handle_click



    def _handle_click(self, sender, event):
        """Handles the click event and executes the on_click callback if defined."""
        if self._on_click:
            self._on_click()
