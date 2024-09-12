import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Callable

class Button(Forms.Button):
    """
    A class to represent a Windows Forms Button with various configurable properties.

    Args:
        - text (str): The text displayed on the button.
        - size (tuple[int, int]): The size of the button (width, height).
        - location (tuple[int, int]): The location of the button (x, y).
        - background_color (Optional[Color]): The background color of the button.
        - text_color (Optional[Color]): The color of the text on the button.
        - on_click (Optional[Callable[[], None]]): Callback function to be executed when the button is clicked.
    """

    def __init__(
        self,
        text: str = "Button",
        size: tuple[int, int] = (100, 50),
        location: tuple[int, int] = (0, 0),
        background_color: Optional[any] = None,
        text_color: Optional[any] = None,
        on_click: Optional[Callable[[], None]] = None
    ):
        super().__init__()
        self._text = text
        self._size = size
        self._location = location
        self._background_color = background_color
        self._text_color = text_color
        self._on_click = on_click
        
        self.Text = self._text
        self.Size = Drawing.Size(*self._size)
        self.Location = Drawing.Point(*self._location)
        if self._background_color:
            self.BackColor = self._background_color
        if self._text_color:
            self.ForeColor = self._text_color
        if self._on_click:
            self.Click += self._handle_click

            

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
    def size(self) -> tuple[int, int]:
        """
        Gets or sets the size of the button (width, height).
        """
        return self._size

    @size.setter
    def size(self, value: tuple[int, int]):
        """
        Sets the size of the button.
        
        Args:
            value (tuple[int, int]): The width and height of the button.
        """
        self._size = value
        self.Size = Drawing.Size(*value)

    @property
    def location(self) -> tuple[int, int]:
        """
        Gets or sets the location of the button (x, y).
        """
        return self._location

    @location.setter
    def location(self, value: tuple[int, int]):
        """
        Sets the location of the button.
        
        Args:
            value (tuple[int, int]): The x and y coordinates of the button.
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
