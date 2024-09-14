import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Tuple, Callable, Type
from .color import Color
from .font import Font, Style

class TextInput(Forms.TextBox):
    """
    Args:
        - value (str): The initial value to display.
        - placeholder (Optional[str]): The placeholder text displayed when the input is empty.
        - font (Optional[Font]): The font of the text.
        - style (Optional[Style]): The style of the font.
        - text_color (Optional[Color]): The color of the text.
        - placeholder_color (Optional[Color]): The color of the placeholder text. Defaults to Color.GRAY.
        - background_color (Optional[Color]): The background color of the text input. Defaults to Color.WHITE.
        - location (Tuple[int, int]): The (x, y) location of the text input within the parent control.
        - text_size (Optional[int]): The font size. If None, a default size is used.
        - width (Optional[int]): The width of the text input control. If None, a default width is used.
        - multiline (bool): Whether the text input should support multiple lines.
        - on_enter (Optional[Callable[[Type], None]]): Handler for the Enter event.
        - on_leave (Optional[Callable[[Type], None]]): Handler for the Leave event.
        - on_confirm (Optional[Callable[[str], None]]): Handler for the Enter key press event.
        - on_change (Optional[Callable[[str], None]]): Handler for the text change event.
    """
    def __init__(
        self,
        value: str = "",
        placeholder: Optional[str] = None,
        font: Optional[Font] = Font.SERIF,
        style: Optional[Style] = Style.REGULAR,
        text_color: Optional[Color] = Color.BLACK,
        placeholder_color: Optional[Color] = Color.GRAY,
        background_color: Optional[Color] = Color.WHITE,
        location: Tuple[int, int] = (0, 0),
        text_size: Optional[int] = 12,
        width: Optional[int] = None,
        multiline: bool = False,
        on_enter: Optional[Callable[[Type], None]] = None,
        on_leave: Optional[Callable[[Type], None]] = None,
        on_confirm: Optional[Callable[[Type], None]] = None,
        on_change: Optional[Callable[[Type], None]] = None
    ):
        """
        Args:
            - value (str): The initial value to display.
            - placeholder (Optional[str]): The placeholder text displayed when the input is empty.
            - font (Optional[Font]): The font of the text.
            - style (Optional[Style]): The style of the font.
            - text_color (Optional[Color]): The color of the text.
            - placeholder_color (Optional[Color]): The color of the placeholder text. Defaults to Color.GRAY.
            - background_color (Optional[Color]): The background color of the text input. Defaults to Color.WHITE.
            - location (Tuple[int, int]): The (x, y) location of the text input within the parent control.
            - text_size (Optional[int]): The font size. If None, a default size is used.
            - width (Optional[int]): The width of the text input control. If None, a default width is used.
            - multiline (bool): Whether the text input should support multiple lines.
            - on_enter (Optional[Callable[[Type], None]]): Handler for the Enter event.
            - on_leave (Optional[Callable[[Type], None]]): Handler for the Leave event.
            - on_confirm (Optional[Callable[[Type], None]]): Handler for the Enter key press event.
            - on_change (Optional[Callable[[Type], None]]): Handler for the text change event.
        """
        super().__init__()

        self._value = value
        self._placeholder = placeholder
        self._font = font
        self._style = style
        self._text_color = text_color
        self._placeholder_color = placeholder_color
        self._background_color = background_color
        self._location = location
        self._text_size = text_size
        self._width = width
        self._multiline = multiline

        self._font_object = Drawing.Font(self._font, self._text_size, self._style)

        self.Text = self._value
        self.ForeColor = self._text_color
        self.BackColor = self._background_color
        self.Location = Drawing.Point(self._location[0], self._location[1])
        self.Font = self._font_object
        self.Multiline = self._multiline

        if self._width:
            self.Width = self._width

        self._placeholder_color = placeholder_color
        self._on_enter_handler = on_enter
        self._on_leave_handler = on_leave
        self._on_confirm_handler = on_confirm
        self._on_change_handler = on_change
        self._update_placeholder()

        if not self._width:
            self._adjust_text_size()

        if self._on_enter_handler:
            self.Enter += self._on_enter_handler
        if self._on_leave_handler:
            self.Leave += self._on_leave_handler
        if self._on_confirm_handler:
            self.KeyDown += self._on_key_down
        if self._on_change_handler:
            self.TextChanged += self._on_text_changed



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
        self._update_placeholder()



    @property
    def placeholder(self) -> Optional[str]:
        """
        Gets or sets the placeholder text shown when the text input is empty.
        
        Returns:
            Optional[str]: The placeholder text.
        """
        return self._placeholder
    


    @placeholder.setter
    def placeholder(self, value: Optional[str]):
        """
        Sets the placeholder text shown when the text input is empty.
        
        Args:
            value (Optional[str]): The new placeholder text.
        """
        self._placeholder = value
        self._update_placeholder()



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
    def placeholder_color(self) -> Color:
        """
        Gets or sets the color of the placeholder text.
        
        Returns:
            Color: The current placeholder text color.
        """
        return self._placeholder_color
    


    @placeholder_color.setter
    def placeholder_color(self, value: Color):
        """
        Sets the color of the placeholder text.
        
        Args:
            value (Color): The new placeholder text color.
        """
        self._placeholder_color = value
        self._update_placeholder()



    @property
    def background_color(self) -> Color:
        """
        Gets or sets the background color of the text input control.
        
        Returns:
            Color: The current background color.
        """
        return self._background_color
    


    @background_color.setter
    def background_color(self, value: Color):
        """
        Sets the background color of the text input control.
        
        Args:
            value (Color): The new background color.
        """
        self._background_color = value
        self.BackColor = value



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
    def text_size(self) -> int:
        """
        Gets or sets the font size of the text.
        """
        return self._text_size
    


    @text_size.setter
    def size(self, value: int):
        """
        Sets the font size of the text and updates the label.
        """
        if value <= 0:
            raise ValueError("Font size must be a positive integer.")
        self._text_size = value
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


    
    @property
    def on_enter(self) -> Optional[Callable[[Type], None]]:
        """
        Gets or sets the handler for the Enter event.
        """
        return self._on_enter_handler
    



    @on_enter.setter
    def on_enter(self, handler: Optional[Callable[[Type], None]]):
        """
        Sets the handler for the Enter event.
        """
        if self._on_enter_handler:
            self.Enter -= self._on_enter_handler
        self._on_enter_handler = handler




    @property
    def on_leave(self) -> Optional[Callable[[Type], None]]:
        """
        Gets or sets the handler for the Leave event.
        """
        return self._on_leave_handler
    



    @on_leave.setter
    def on_leave(self, handler: Optional[Callable[[Type], None]]):
        """
        Sets the handler for the Leave event.
        """
        if self._on_leave_handler:
            self.Leave -= self._on_leave_handler
        self._on_leave_handler = handler




    @property
    def on_confirm(self) -> Optional[Callable[[Type], None]]:
        """
        Gets or sets the handler for the Enter key press event.
        """
        return self._on_confirm_handler
    
    


    @on_confirm.setter
    def on_confirm(self, handler: Optional[Callable[[Type], None]]):
        """
        Sets the handler for the Enter key press event.
        """
        if self._on_confirm_handler:
            self.KeyDown -= self._on_key_down
        self._on_confirm_handler = handler




    @property
    def on_change(self) -> Optional[Callable[[Type], None]]:
        """
        Gets or sets the handler for the text change event.
        """
        return self._on_change_handler
    



    @on_change.setter
    def on_change(self, handler: Optional[Callable[[Type], None]]):
        """
        Sets the handler for the text change event.
        """
        if self._on_change_handler:
            self.TextChanged -= self._on_text_changed
        self._on_change_handler = handler


    
    def focus(self):
        """
        Set the focus to this TextInput control.
        """
        self.Focus()



    def _update_font(self):
        """
        Updates the font of the text input control based on the current font settings.
        """
        self._font_object = Drawing.Font(self._font, self._text_size, self._style)
        self.Font = self._font_object
        self._adjust_text_size()




    def _adjust_text_size(self):
        """
        Adjusts the size of the text input control based on the current text and font settings.
        """
        if not self.Multiline:
            graphics = self.CreateGraphics()
            try:
                text_size = graphics.MeasureString(self.Text, self.Font)
                self.Size = Drawing.Size(int(text_size.Width) + 10, int(text_size.Height) + 10)
            finally:
                graphics.Dispose()
        else:
            self.Size = Drawing.Size(200, 100)



    def _update_placeholder(self):
        """
        Updates the display of the placeholder text based on whether the text input is empty or not.
        If the text input is empty and a placeholder is provided, the placeholder text is displayed in the placeholder color.
        Otherwise, the text color is used.
        """
        if not self.Text and self._placeholder:
            self.ForeColor = self._placeholder_color
            self.Text = self._placeholder
        else:
            self.ForeColor = self._text_color



    def _on_enter(self, sender, event):
        """
        Event handler for when the text input control receives focus. Clears the placeholder text if it is currently displayed.
        """
        if self._on_enter_handler:
            self._on_enter_handler(sender, event)
        if self.Text == self._placeholder:
            self.Text = ""
            self.ForeColor = self._text_color


            
    def _on_leave(self, sender, event):
        """
        Event handler for when the text input control loses focus. Re-displays the placeholder text if the input is empty.
        """
        if self._on_leave_handler:
            self._on_leave_handler(sender, event)
        if not self.Text:
            self._update_placeholder()


    
    def _on_key_down(self, sender, event):
        """
        If the Enter key is pressed, the on_confirm handler (if defined) is called with
        the current text. The event is marked as handled to prevent further processing.
        """
        if event.KeyCode == Forms.Keys.Enter:
            if self._on_confirm_handler:
                self._on_confirm_handler(sender, self.Text)
            event.Handled = True



    def _on_text_changed(self, sender, event):
        """
        The on_change handler (if defined) is called with the current text whenever the
        text in the input control changes.
        """
        if self._on_change_handler:
            self._on_change_handler(sender, self.Text)
