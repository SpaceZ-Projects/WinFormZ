import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Tuple
from .color import Color
from .font import Font, Style

class TextInput(Forms.TextBox):
    """
    Args:
        - value (str): The initial value to display.
        - font (Optional[Font]): The font of the text.
        - style (Optional[Style]): The style of the font.
        - text_color (Optional[Color]): The color of the text.
        - location (Tuple[int, int]): The (x, y) location of the text input within the parent control.
        - size (Optional[int]): The font size. If None, a default size is used.
        - multiline (bool): Whether the text input should support multiple lines.
    """
    def __init__(
        self,
        value: str = "",
        font: Optional[Font] = Font.SERIF,
        style: Optional[Style] = Style.REGULAR,
        text_color: Optional[Color] = Color.BLACK,
        location: Tuple[int, int] = (0, 0),
        size: Optional[int] = 12,
        multiline: bool = False
    ):
        """
        Args:
            - value (str): The initial value to display.
            - font (Optional[Font]): The font of the text.
            - style (Optional[Style]): The style of the font.
            - text_color (Optional[Color]): The color of the text.
            - location (Tuple[int, int]): The (x, y) location of the text input within the parent control.
            - size (Optional[int]): The font size. If None, a default size is used.
            - multiline (bool): Whether the text input should support multiple lines.
        """
        super().__init__()

        self._value = value
        self._font = font
        self._style = style
        self._text_color = text_color
        self._location = location
        self._size = size
        self._multiline = multiline

        self._font_object = Drawing.Font(self._font, self._size, self._style)

        self.Text = self._value
        self.ForeColor = self._text_color
        self.Location = Drawing.Point(self._location[0], self._location[1])
        self.Font = self._font_object
        self.Multiline = self._multiline

        self._adjust_size()

    @property
    def value(self) -> str:
        """
        Gets or sets the value displayed in the text input control.
        """
        return self._value
    


    @value.setter
    def value(self, value: str):
        """
        Sets the value displayed in the text input control.
        """
        self._value = value
        self.Text = value



    @property
    def font(self) -> Font:
        """
        Gets or sets the font of the text displayed in the text input control.
        """
        return self._font
    


    @font.setter
    def font(self, value: Font):
        """
        Sets the font of the text displayed in the text input control.
        """
        self._font = value
        self._update_font()



    @property
    def style(self) -> Style:
        """
        Gets or sets the style of the font used in the text input control.
        """
        return self._style
    


    @style.setter
    def style(self, value: Style):
        """
        Sets the style of the font used in the text input control.
        """
        self._style = value
        self._update_font()



    @property
    def text_color(self) -> Color:
        """
        Gets or sets the color of the text in the text input control.
        """
        return self._text_color
    


    @text_color.setter
    def text_color(self, value: Color):
        """
        Sets the color of the text in the text input control.
        """
        self._text_color = value
        self.ForeColor = value



    @property
    def location(self) -> Tuple[int, int]:
        """
        Gets or sets the (x, y) location of the text input control within its parent container.
        """
        return (self.Location.X, self.Location.Y)
    


    @location.setter
    def location(self, value: Tuple[int, int]):
        """
        Sets the (x, y) location of the text input control within its parent container.
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



    @property
    def multiline(self) -> bool:
        """
        Gets or sets whether the text input control supports multiple lines of text.
        """
        return self._multiline
    


    @multiline.setter
    def multiline(self, value: bool):
        """
        Sets whether the text input control supports multiple lines of text.
        """
        self._multiline = value
        self.Multiline = value



    def _update_font(self):
        self._font_object = Drawing.Font(self._font, self._size, self._style)
        self.Font = self._font_object
        self._adjust_size()



    def _adjust_size(self):
        if not self.Multiline:
            graphics = self.CreateGraphics()
            text_size = graphics.MeasureString(self.Text, self.Font)
            self.Size = Drawing.Size(int(text_size.Width) + 10, int(text_size.Height) + 10)
            graphics.Dispose()
        else:
            self.Size = Drawing.Size(200, 100)