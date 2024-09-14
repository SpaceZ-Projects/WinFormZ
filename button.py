import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Callable, Tuple
from pathlib import Path
from .color import Color
from .font import Font, Style

class Button(Forms.Button):
    """
    Args:
        - text (str): The text displayed on the button.
        - size (Tuple[int, int]): The size of the button (width, height).
        - location (Tuple[int, int]): The location of the button (x, y).
        - background_color (Optional[Color]): The background color of the button.
        - text_color (Optional[Color]): The color of the text on the button.
        - text_size (Optional[int]): The font size of the text on the button.
        - text_font (Optional[Font]): The font of the text on the button.
        - text_style (Optional[Style]): The style of the font (e.g., regular, bold, italic).
        - icon (Optional[str]): The path to the icon file (.ico, .png, .bmp), absolute path.
        - popup (Optional[str]): The text to display as a tooltip when hovering over the button.
        - on_click (Optional[Callable[[], None]]): Callback function to be executed when the button is clicked.
    """

    def __init__(
        self,
        text: str = None,
        size: Tuple[int, int] = (100, 50),
        location: Tuple[int, int] = (0, 0),
        background_color: Optional[Color] = Color.TRANSPARENT,
        text_color: Optional[Color] = None,
        text_size: Optional[int] = None,
        text_font: Optional[Font] = None,
        text_style: Optional[Style] = None,
        icon: Optional[Path] = None,
        popup: Optional[str] = None,
        on_click: Optional[Callable[[], None]] = None
    ):
        """
        Args:
            - text (str): The text displayed on the button.
            - size (Tuple[int, int]): The size of the button (width, height).
            - location (Tuple[int, int]): The location of the button (x, y).
            - background_color (Optional[Color]): The background color of the button.
            - text_color (Optional[Color]): The color of the text on the button.
            - text_size (Optional[int]): The font size of the text on the button.
            - text_style (Optional[Style]): The style of the font (e.g., regular, bold, italic).
            - icon (Optional[str]): The path to the icon file (.ico, .png, .bmp), absolute path.
            - popup (Optional[str]): The text to display as a tooltip when hovering over the button.
            - on_click (Optional[Callable[[], None]]): Callback function to be executed when the button is clicked.
        """
        super().__init__()
        self._text = text
        self._size = size
        self._location = location
        self._background_color = background_color
        self._text_color = text_color
        self._text_size = text_size
        self._text_font = text_font
        self._text_style = text_style
        self._icon = icon
        self._popup = popup
        self._on_click = on_click

        self._tooltip = Forms.ToolTip()
        
        if self._text:
            self.Text = self._text

        self.Size = Drawing.Size(*self._size)
        self.Location = Drawing.Point(*self._location)
        self.BackColor = self._background_color

        if self._text_color:
            self.ForeColor = self._text_color

        if self._icon:
            self.Image = Drawing.Image.FromFile(self._icon)

        self._set_font()

        if self._on_click:
            self.Click += self._handle_click

        if self._popup:
            self._tooltip.SetToolTip(self, self._popup)


    def _set_font(self):
        """Sets the font for the button based on the provided text_font, text_size, and text_style."""
        font_family = self._text_font or Font.SERIF
        font_size = self._text_size or 10
        font_style = self._text_style or Style.REGULAR
        
        self.Font = Drawing.Font(font_family, font_size, font_style)

            

    @property
    def text(self) -> str:
        """
        Gets or sets the text displayed on the button.
        """
        return self._text

    @text.setter
    def text(self, value: str):
        """
        Sets the text displayed on the button.
        
        Args:
            value (str): The text to be displayed on the button.
        """
        self._text = value
        self.Text = value

    @property
    def size(self) -> Tuple[int, int]:
        """
        Gets or sets the size of the button (width, height).
        """
        return self._size

    @size.setter
    def size(self, value: Tuple[int, int]):
        """
        Sets the size of the button.
        
        Args:
            value (Tuple[int, int]): The width and height of the button.
        """
        self._size = value
        self.Size = Drawing.Size(*value)

    @property
    def location(self) -> Tuple[int, int]:
        """
        Gets or sets the location of the button (x, y).
        """
        return self._location

    @location.setter
    def location(self, value: Tuple[int, int]):
        """
        Sets the location of the button.
        
        Args:
            value (Tuple[int, int]): The x and y coordinates of the button.
        """
        self._location = value
        self.Location = Drawing.Point(*value)

    @property
    def background_color(self) -> Optional[any]:
        """
        Gets or sets the background color of the button.
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value: Optional[any]):
        """
        Sets the background color of the button.
        
        Args:
            value (Optional[Color]): The background color of the button. 
                                     If None, the background color will not be changed.
        """
        self._background_color = value
        if value:
            self.BackColor = value

    @property
    def text_color(self) -> Optional[any]:
        """
        Gets or sets the color of the text on the button.
        """
        return self._text_color

    @text_color.setter
    def text_color(self, value: Optional[any]):
        """
        Sets the color of the text on the button.
        
        Args:
            value (Optional[Color]): The color of the text on the button. 
                                     If None, the text color will not be changed.
        """
        self._text_color = value
        if value:
            self.ForeColor = value


    @property
    def text_size(self) -> Optional[int]:

        return self._text_size
    


    @text_size.setter
    def text_size(self, value: Optional[int]):
        self._text_size = value
        if value:
            self.Font = Drawing.Font(self.Font.FontFamily, value)
        else:
            # Optionally, you can reset to a default font size if needed
            self.Font = Drawing.Font(self.Font.FontFamily, 10)




    @property
    def icon(self) -> Optional[str]:
        """
        Gets or sets the path to the icon file for the button.
        """
        return self._icon

    @icon.setter
    def icon(self, value: Optional[str]):
        """
        Sets the path to the icon file for the button.
        
        Args:
            value (Optional[str]): The path to the icon file (.ico, .png, .bmp). 
                                   If None, the icon will be removed.
        """
        self._icon = value
        if value:
            self.Image = Drawing.Image.FromFile(value)
        else:
            self.Image = None


    @property
    def popup(self) -> Optional[str]:
        return self._popup



    @popup.setter
    def popup(self, value: Optional[str]):
        self._popup = value
        if value:
            self._tooltip.SetToolTip(self, value)
        else:
            self._tooltip.RemoveAll()

    

    @property
    def on_click(self) -> Optional[Callable[[], None]]:
        """
        Gets or sets the callback function to be executed when the button is clicked.
        """
        return self._on_click

    @on_click.setter
    def on_click(self, value: Optional[Callable[[], None]]):
        """
        Sets the callback function to be executed when the button is clicked.
        
        Args:
            value (Optional[Callable[[], None]]): The callback function to be executed on click. 
                                                   If None, the event handler will be removed.
        """
        self._on_click = value
        if value:
            self.Click += self._handle_click
        else:
            self.Click -= self._handle_click

    def _handle_click(self, sender, event_args):
        """
        Handles the click event and executes the on_click callback if defined.
        
        Args:
            sender: The source of the event.
            event_args: The event data.
        """
        if self._on_click:
            self._on_click()
