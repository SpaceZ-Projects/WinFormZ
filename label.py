import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Tuple
from .color import Color
from .font import Font, Style

class Label(Forms.Label):
    """
    A custom label control with additional features.

    Args:
        - text (str): The text to display.
        - font (Optional[Font]): The font of the text.
        - style (Optional[Style]): The style of the font.
        - text_color (Optional[Color]): The color of the text.
        - location (Tuple[int, int]): The (x, y) location of the label within the parent control.
        - size (Optional[int]): The font size. If None, a default size is used.
    """
    def __init__(
        self,
        text: str = "Hello, World!",
        font: Optional[any] = Font.SERIF,
        style: Optional[any] = Style.REGULAR,
        text_color: Optional[any] = Color.BLACK,
        location: Tuple[int, int] = (0, 0),
        size: Optional[int] = 12
    ):
        """
        A custom label control with additional features.

        Args:
            - text (str): The text to display.
            - font (Optional[Font]): The font of the text.
            - style (Optional[Style]): The style of the font.
            - text_color (Optional[Color]): The color of the text.
            - location (Tuple[int, int]): The (x, y) location of the label within the parent control.
            - size (Optional[int]): The font size. If None, a default size is used.
        """
        super().__init__()

        # Initialize properties
        self._text = text
        self._font = font
        self._style = style
        self._text_color = text_color
        self._location = location
        self._size = size

        # Create font object
        self._font_object = Drawing.Font(self._font, self._size, self._style)

        # Apply initial settings
        self.Text = self._text
        self.ForeColor = self._text_color
        self.Location = Drawing.Point(self._location[0], self._location[1])
        self.Font = self._font_object

        self._adjust_size()


    @property
    def text(self) -> str:
        """
        Gets or sets the text displayed by the label.
        """
        return self._text

    @text.setter
    def text(self, value: str):
        """
        Sets the text displayed by the label and updates the label.
        """
        self._text = value
        self.Text = value

    @property
    def font(self) -> Drawing.Font:
        """
        Gets or sets the font of the text.
        """
        return self._font

    @font.setter
    def font(self, value: Drawing.Font):
        """
        Sets the font of the text and updates the label.
        """
        self._font = value
        self.Font = value

    @property
    def style(self) -> Drawing.FontStyle:
        """
        Gets or sets the style of the font.
        """
        return self._style

    @style.setter
    def style(self, value: Drawing.FontStyle):
        """
        Sets the style of the font and updates the label.
        """
        self._style = value
        self._update_font()



    @property
    def text_color(self) -> Drawing.Color:
        """
        Gets or sets the color of the text.
        """
        return self._text_color

    @text_color.setter
    def text_color(self, value: Drawing.Color):
        """
        Sets the color of the text and updates the label.
        """
        self._text_color = value
        self.ForeColor = value

    @property
    def location(self) -> tuple[int, int]:
        """
        Gets or sets the (x, y) location of the label within the parent control.
        """
        return (self.Location.X, self.Location.Y)

    @location.setter
    def location(self, value: tuple[int, int]):
        """
        Sets the (x, y) location of the label within the parent control.
        """
        self._location = value
        self.Location = Drawing.Point(value[0], value[1])


    
    @property
    def size(self) -> int:
        """
        Gets or sets the font size of the text.
        """
        return self._size

    @size.setter
    def size(self, value: int):
        """
        Sets the font size of the text and updates the label.
        """
        self._size = value
        self._update_font()

    def _update_font(self):
        """
        Updates the font of the label and adjusts the size of the control.
        """
        self._font_object = Drawing.Font(self._font, self._size, self._style)
        self.Font = self._font_object
        self._adjust_size()


    def _adjust_size(self):
        """
        Adjust the size of the label to fit the text.
        """
        graphics = self.CreateGraphics()
        text_size = graphics.MeasureString(self.Text, self.Font)

        self.Size = Drawing.Size(int(text_size.Width) + 10, int(text_size.Height) + 10)
        graphics.Dispose()
