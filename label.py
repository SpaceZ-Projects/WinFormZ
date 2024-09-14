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
    Args:
        - text (str): The text to display.
        - font (Optional[Font]): The font of the text.
        - style (Optional[Style]): The style of the font.
        - text_color (Optional[Color]): The color of the text.
        - background_color (Optional[Color]): The background color of the label.
        - location (Tuple[int, int]): The (x, y) location of the label within the parent control.
        - size (Optional[int]): The font size. If None, a default size is used.
    """
    def __init__(
        self,
        text: str = "Hello, World!",
        font: Optional[Font] = Font.SERIF,
        style: Optional[Style] = Style.REGULAR,
        text_color: Optional[Color] = Color.BLACK,
        background_color: Optional[Color] = Color.TRANSPARENT,
        location: Tuple[int, int] = (0, 0),
        size: Optional[int] = 12
    ):
        """
        Args:
            - text (str): The text to display.
            - font (Optional[Font]): The font of the text.
            - style (Optional[Style]): The style of the font.
            - text_color (Optional[Color]): The color of the text.
            - background_color (Optional[Color]): The background color of the label.
            - location (Tuple[int, int]): The (x, y) location of the label within the parent control.
            - size (Optional[int]): The font size. If None, a default size is used.
        """
        super().__init__()

        # Initialize properties
        self._text = text
        self._font = font
        self._style = style
        self._text_color = text_color
        self._background_color = background_color
        self._location = location
        self._size = size

        # Create font object
        self._font_object = Drawing.Font(self._font, self._size, self._style)

        # Apply initial settings
        self.Text = self._text
        self.ForeColor = self._text_color
        self.BackColor = self._background_color
        self.Location = Drawing.Point(self._location[0], self._location[1])
        self.TextAlign = Drawing.ContentAlignment.MiddleCenter
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
    def font(self) -> Font:
        """
        Gets or sets the font of the text.
        """
        return self._font

    @font.setter
    def font(self, value: Font):
        """
        Sets the font of the text and updates the label.
        """
        self._font = value
        self.Font = value

    @property
    def style(self) -> Style:
        """
        Gets or sets the style of the font.
        """
        return self._style

    @style.setter
    def style(self, value: Style):
        """
        Sets the style of the font and updates the label.
        """
        self._style = value
        self._update_font()



    @property
    def text_color(self) -> Color:
        """
        Gets or sets the color of the text.
        """
        return self._text_color
    


    @text_color.setter
    def text_color(self, value: Color):
        """
        Sets the color of the text and updates the label.
        """
        self._text_color = value
        self.ForeColor = value


    @property
    def background_color(self) -> Color:
        """
        Gets or sets the background color of the label.
        """
        return self._background_color
    


    @background_color.setter
    def background_color(self, value: Color):
        """
        Sets the background color of the label and updates the label.
        """
        self._background_color = value
        self.BackColor = value




    @property
    def location(self) -> Tuple[int, int]:
        """
        Gets or sets the (x, y) location of the label within the parent control.
        """
        return (self.Location.X, self.Location.Y)
    


    @location.setter
    def location(self, value: Tuple[int, int]):
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
        if value <= 0:
            raise ValueError("Font size must be a positive integer.")
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
        Adjust the size of the label to fit the text precisely with a small padding.
        """
        graphics = self.CreateGraphics()
        text_size = graphics.MeasureString(self.Text, self.Font)

        padding = 0
        self.Size = Drawing.Size(
            int(text_size.Width) + padding,
            int(text_size.Height) + padding
        )

        graphics.Dispose()