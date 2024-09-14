
import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms
import System as Sys

from typing import Callable, Optional, Type, Tuple
from pathlib import Path
from .color import Color


class App:
    _icon = None

    @classmethod
    def set_icon(cls, icon_path: Optional[Path]):
        if icon_path:
            try:
                cls._icon = Drawing.Icon(str(icon_path))
            except Exception as e:
                print(f"Error setting icon: {e}")
        else:
            cls._icon = None

    @classmethod
    def get_icon(cls) -> Optional[Drawing.Icon]:
        return cls._icon



class MainWindow(Forms.Form):
    """
    Args:
        - title (str): The title of the window.
        - size (Tuple[int, int]): The size of the window.
        - content (Optional[Type], None): set the window's content.
        - location (Tuple[int, int]): The location of the window.
        - center_screen (bool): Whether to center the window on the screen.
        - background_color (Color): The background color of the window.
        - resizable (bool): Whether the window should be resizable.
        - minimizable (bool): Whether to show the MinimizeBox in the window.
        - maxmizable (bool): Whether to show the MaximizeBox in the window.
        - closable (bool): Whether to show the CloseBox in the window.
        - borderless (bool): Whether the window should have a border or not. Default is True. if set to False it cancel the resizable.
        - icon (Optional[Path]): The path to the window's icon.
        - on_exit (Callable[[Type], None]): A callback function to run when the window is closing.
        - on_minimize (Callable[[Type], None]): A callback function to run when the window is minimized.
        - draggable (bool): Whether the window can be dragged by holding down the mouse button.

    Methods:
        run: Starts the application and displays the window.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            print("Warning: An instance of MainWindow already exists")
            return cls._instance
        cls._instance = super(MainWindow, cls).__new__(cls)
        return cls._instance
    

    def __init__(
        self,
        title: str = "SpaceZ App",
        size: Tuple[int, int] = (800, 600),
        content: Optional[Type] = None,
        location: Tuple[int, int] = (100, 100),
        center_screen: bool = False,
        background_color: Optional[Color] = None,
        resizable: bool = True,
        minimizable: bool = True,
        maxmizable: bool = True,
        closable: bool = True,
        borderless: bool = True,
        icon: Optional[Path] = None,
        on_exit: Optional[Callable[[Type], bool]] = None,
        on_minimize: Optional[Callable[[Type], None]] = None,
        draggable: bool = False
    ):
        if hasattr(self, '_initialized') and self._initialized:
            return
        
        """
        Args:
            - title (str): The title of the window.
            - size (Tuple[int, int]): The size of the window.
            - content (Optional[Type], None): set the window's content.
            - location (Tuple[int, int]): The location of the window.
            - center_screen (bool): Whether to center the window on the screen.
            - background_color (Color): The background color of the window.
            - resizable (bool): Whether the window should be resizable.
            - minimizable (bool): Whether to show the MinimizeBox in the window.
            - maxmizable (bool): Whether to show the MaximizeBox in the window.
            - closable (bool): Whether to show the CloseBox in the window.
            - borderless (bool): Whether the window should have a border or not. Default is True. if set to False it cancel the resizable.
            - icon (Optional[Path]): The path to the window's icon.
            - on_exit (Callable[[Type], None]): A callback function to run when the window is closing.
            - on_minimize (Callable[[Type], None]): A callback function to run when the window is minimized.
            - draggable (bool): Whether the window can be dragged by holding down the mouse button.
        Methods:
            - run: Starts the application and displays the window.
        """
        super().__init__()
        self._title = title
        self._size = Drawing.Size(size[0], size[1])
        self._content = content
        self._location = location
        self._center_screen = center_screen
        self._background_color = background_color
        self._resizable = resizable
        self._minimizable = minimizable
        self._maxmizable = maxmizable
        self._closable = closable
        self._borderless = borderless
        self._icon = icon

        self._on_exit = on_exit
        self._on_minimize = on_minimize
        self._draggable = draggable

        self._dragging = False
        self._drag_start = Drawing.Point(0, 0)

        self.Text = self._title
        self.Size = self._size

        if self._icon:
            App.set_icon(self._icon)
            self.Icon = App.get_icon()

        if background_color:
            self.BackColor = self._background_color

        self.MinimizeBox = self._minimizable
        self.MaximizeBox = self._maxmizable
        self.ControlBox = self._closable

        if content:
            self.Controls.Add(self._content)

        if center_screen:
            self.StartPosition = Forms.FormStartPosition.CenterScreen
        else:
            self.StartPosition = Forms.FormStartPosition.Manual
            self.Location = Drawing.Point(self._location[0], self._location[1])

        if not self._borderless:
            self.FormBorderStyle = Forms.FormBorderStyle(0)
        elif not self._resizable:
            self.FormBorderStyle = Forms.FormBorderStyle.FixedDialog

        if draggable:
            self._update_draggable()

        self.FormClosing += self._handle_form_closing
        self.Resize += self._handle_minimize_window

        self._initialized = True

    
    @property
    def title(self):
        """
        Get the window's title.
        """
        return self._title
    

    @title.setter
    def title(self, new_title: str):
        """
        Set the window's title.

        Args:
            new_title (str): The new title of the window.
        """
        self._title = new_title
        self.Text = new_title


    @property
    def size(self):
        """
        Get the window's size as a tuple.
        """
        return (self.Size.Width, self.Size.Height)
    

    @size.setter
    def size(self, new_size: tuple[int, int]):
        """
        Set the window's size.

        Args:
            new_size (tuple[int, int]): The new size of the window (width, height).
        """
        self._size = Drawing.Size(new_size[0], new_size[1])
        self.Size = self._size


    @property
    def content(self) -> Optional[Type]:
        return self._content
    

    @content.setter
    def content(self, new_content: Optional[Type]):
        # Remove old content if any
        if self._content and self._content in self.Controls:
            self.Controls.Remove(self._content)
        # Add new content if provided
        self._content = new_content
        if new_content:
            self.Controls.Add(new_content)

    
    @property
    def location(self) -> tuple[int, int]:
        """
        Get the window's location.

        Returns:
            tuple[int, int]: The location of the window (x, y).
        """
        return (self.Location.X, self.Location.Y)

    @location.setter
    def location(self, new_location: tuple[int, int]):
        """
        Set the window's location.

        Args:
            new_location (tuple[int, int]): The new location of the window (x, y).
        """
        self._set_location(new_location)

    def _set_location(self, location: Tuple[int, int]):
        """
        Set the window's location.

        Args:
            location (tuple[int, int]): The new location of the window (x, y).
        """
        self._location = location  # Update internal location state
        if not self._center_screen:
            self.Location = Drawing.Point(location[0], location[1])


    @property
    def background_color(self) -> Optional[Color]:
        """
        Get the background color of the window.

        Returns:
            Optional[Color]: The background color of the window.
        """
        return self._background_color

    @background_color.setter
    def background_color(self, color: Optional[Color]):
        """
        Set the background color of the window.

        Args:
            color (Optional[Color]): The new background color of the window.
        """
        self._background_color = color
        if color is not None:
            self.BackColor = color
        else:
            self.BackColor = None


    @property
    def resizable(self):
        """
        Get whether the window is resizable based on the FormBorderStyle.
        """
        return self.FormBorderStyle == Forms.FormBorderStyle.Sizable

    @resizable.setter
    def resizable(self, value: bool):
        """
        Set whether the window should be resizable.

        Args:
            value (bool): True if the window should be resizable, False otherwise.
        """
        if value:
            self.FormBorderStyle = Forms.FormBorderStyle.Sizable
        else:
            self.FormBorderStyle = Forms.FormBorderStyle.FixedDialog
        self._resizable = value


    @property
    def minimizable(self) -> bool:
        """
        Get whether the MinimizeBox is enabled for the window.

        Returns:
            bool: True if the window can be minimized (i.e., MinimizeBox is enabled), False otherwise.
        """
        return self.MinimizeBox

    @minimizable.setter
    def minimizable(self, value: bool):
        """
        Set whether the MinimizeBox should be enabled for the window.

        Args:
            value (bool): True to enable the MinimizeBox, allowing the window to be minimized, False to disable it.
        """
        self.MinimizeBox = value
        self._minimizable = value


    @property
    def maxmizable(self) -> bool:
        """
        Get whether the MaximizeBox is enabled for the window.

        Returns:
            bool: True if the window can be maximized (i.e., MaximizeBox is enabled), False otherwise.
        """
        return self.MaximizeBox

    @maxmizable.setter
    def maxmizable(self, value: bool):
        """
        Set whether the MaximizeBox should be enabled for the window.

        Args:
            value (bool): True to enable the MaximizeBox, allowing the window to be maximized, False to disable it.
        """
        self.MaximizeBox = value
        self._maxmizable = value


    @property
    def closable(self) -> bool:
        """
        Get whether the ControlBox (the close button) is enabled for the window.

        Returns:
            bool: True if the window can be closed (i.e., ControlBox is enabled), False otherwise.
        """
        return self.ControlBox

    @closable.setter
    def closable(self, value: bool):
        """
        Set whether the ControlBox should be enabled for the window.

        Args:
            value (bool): True to enable the ControlBox, allowing the window to be closed, False to disable it.
        """
        self.ControlBox = value
        self._closable = value


    
    @property
    def borderless(self) -> bool:
        """
        Get the borderless state of the window.
        """
        return self._borderless

    @borderless.setter
    def borderless(self, value: bool):
        """
        Set the borderless state of the window.
        """
        if value:
            self.FormBorderStyle = Forms.FormBorderStyle(1)
            self._borderless = True
        else:
            self.FormBorderStyle = Forms.FormBorderStyle(0)
            self._borderless = False



    @property
    def icon(self) -> Optional[Path]:
        """
        Get the path to the app icon file.
        """
        return self._icon
    


    @icon.setter
    def icon(self, value: Optional[Drawing.Icon]):
        """
        Set the path to the app icon file.
        """
        self._icon = value
        App.set_icon(value)
        self.Icon = App.get_icon()


    
    @property
    def on_exit(self) -> Optional[Callable[[], bool]]:
        """
        Get the callback function to run when the window is closing.
        """
        return self._on_exit

    @on_exit.setter
    def on_exit(self, handler: Optional[Callable[[], bool]]):
        """
        Set the callback function to run when the window is closing.

        Args:
            handler (Callable[[], None]): A callback function to run when the window is closing.
        """
        self._on_exit = handler

    
    @property
    def on_minimize(self) -> Optional[Callable[[], None]]:
        return self._on_minimize
    

    @on_minimize.setter
    def on_minimize(self, handler: Optional[Callable[[], None]]):
        self._on_minimize = handler


    @property
    def draggable(self) -> bool:
        return self._draggable
    

    @draggable.setter
    def draggable(self, value: bool):
        if self._draggable != value:
            self._draggable = value
            self._update_draggable()


    def _update_draggable(self):
        if self._draggable:
            self.MouseDown += self._on_mouse_down
            self.MouseMove += self._on_mouse_move
            self.MouseUp += self._on_mouse_up
        else:
            self.MouseDown -= self._on_mouse_down
            self.MouseMove -= self._on_mouse_move
            self.MouseUp -= self._on_mouse_up



    def _on_mouse_down(self, sender: object, e: Forms.MouseEventArgs):
        if e.Button == Forms.MouseButtons.Left:
            self._dragging = True
            self._drag_start = e.Location



    def _on_mouse_move(self, sender: object, e: Forms.MouseEventArgs):
        if self._dragging:
            self.Location = Drawing.Point(self.Location.X + e.X - self._drag_start.X,
                                          self.Location.Y + e.Y - self._drag_start.Y)
            
            

    def _on_mouse_up(self, sender: object, e: Forms.MouseEventArgs):
        if e.Button == Forms.MouseButtons.Left:
            self._dragging = False



    def _handle_form_closing(self, sender, e: Forms.FormClosingEventArgs):
        """
        Handle the FormClosing event to execute the on_exit callback and potentially cancel closing.

        Args:
            sender: The sender of the event.
            e (FormClosingEventArgs): Event arguments containing information about the closing event.
        """
        if self._on_exit:
            result = self._on_exit()
            if result is False:
                e.Cancel = True 


    def _handle_minimize_window(self, sender, e: Sys.EventArgs):
        """
        Handle the Resize event to check if the window is minimized.
        """
        if self.WindowState == Forms.FormWindowState.Minimized:
            if Callable(self._on_minimize):
                self._on_minimize()



    def minimize(self):
        """
        Minimizes the window.
        """
        self.WindowState = Forms.FormWindowState.Minimized
        if self._on_minimize:
            self._on_minimize()

    
    def activate(self):
        """
        Set as current window
        """
        self.Activate()


    def hide(self):
        """
        Hide the window.
        """
        self.Hide()

    def show(self):
        """
        Show the window.
        """
        self.Show()


    def run(self):
        """
        Starts the application and displays the window.
        """
        Forms.Application.Run(self)


    def exit(self):
        """
        EXit the application.
        """
        Forms.Application.Exit()