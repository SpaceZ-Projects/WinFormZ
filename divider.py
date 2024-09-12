import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional
from .color import Color

class Divider(Forms.Panel):
    """
    A class to represent a divider line (separator) with configurable properties.

    Args:
        - direction (str): The direction of the divider line ('horizontal' or 'vertical').
        - width (int): The width of the divider line in pixels.
        - color (Optional[Color]): The color of the divider line.
        - location (tuple[int, int]): The location of the divider line (x, y).
        - size (tuple[int, int]): The size of the divider line (width, height).
    """

    def __init__(
        self,
        direction: str = 'horizontal',
        width: int = 2,
        color: Optional[any] = Color.BLACK,
        location: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (100, 2)
    ):
        super().__init__()
        self._direction = direction
        self._width = width
        self._color = color
        self._location = location
        self._size = size

        self.Location = Drawing.Point(*self._location)
        self.Size = Drawing.Size(*self._size)
        self.BackColor = self._color

        self.Paint += self._on_paint

    @property
    def direction(self) -> str:
        """
        Gets or sets the direction of the divider line ('horizontal' or 'vertical').
        """
        return self._direction

    @direction.setter
    def direction(self, value: str):
        """
        Sets the direction of the divider line.
        
        Args:
            value (str): The direction of the divider line ('horizontal' or 'vertical').
        """
        if value not in ['horizontal', 'vertical']:
            raise ValueError("Direction must be either 'horizontal' or 'vertical'.")
        self._direction = value
        self.Invalidate()  # Redraw the divider line

    @property
    def width(self) -> int:
        """
        Gets or sets the width of the divider line in pixels.
        """
        return self._width

    @width.setter
    def width(self, value: int):
        """
        Sets the width of the divider line.
        
        Args:
            value (int): The width of the divider line in pixels.
        """
        self._width = value
        self.Invalidate()  # Redraw the divider line

    @property
    def color(self) -> Optional[any]:
        """
        Gets or sets the color of the divider line.
        """
        return self._color

    @color.setter
    def color(self, value: Optional[any]):
        """
        Sets the color of the divider line.
        
        Args:
            value (Optional[Color]): The color of the divider line.
        """
        self._color = value
        self.Invalidate()  # Redraw the divider line

    @property
    def location(self) -> tuple[int, int]:
        """
        Gets or sets the location of the divider line (x, y).
        """
        return self._location

    @location.setter
    def location(self, value: tuple[int, int]):
        """
        Sets the location of the divider line.
        
        Args:
            value (tuple[int, int]): The x and y coordinates of the divider line.
        """
        self._location = value
        self.Location = Drawing.Point(*value)

    @property
    def size(self) -> tuple[int, int]:
        """
        Gets or sets the size of the divider line (width, height).
        """
        return self._size

    @size.setter
    def size(self, value: tuple[int, int]):
        """
        Sets the size of the divider line.
        
        Args:
            value (tuple[int, int]): The width and height of the divider line.
        """
        self._size = value
        self.Size = Drawing.Size(*value)

    def _on_paint(self, sender, paint_args):
        """
        Handles the Paint event to draw the divider line.

        Args:
            sender: The source of the event.
            paint_args: The paint event arguments.
        """
        graphics = paint_args.Graphics
        if self._direction == 'horizontal':
            graphics.FillRectangle(Drawing.SolidBrush(self._color), 0, (self.Height - self._width) // 2, self.Width, self._width)
        elif self._direction == 'vertical':
            graphics.FillRectangle(Drawing.SolidBrush(self._color), (self.Width - self._width) // 2, 0, self._width, self.Height)
