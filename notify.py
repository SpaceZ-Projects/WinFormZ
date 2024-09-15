import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, List, Type
from pathlib import Path


class NotifyIcon(Forms.NotifyIcon):
    """
    Args:
        - icon (Path): A Path object pointing to the icon file to be displayed in the system tray.
        - commands : Optional. A list of tuples representing context menu commands. If None, no context menu will be set up.
        - popup (Optional[str]): The text to display as a tooltip when hovering over the notify icon.
    """
    def __init__(
        self,
        icon: Path = None,
        commands: Optional[List[Type]] = None,
        popup: Optional[str] = None
    ):
        """
        Args:
            - icon: A Path object pointing to the icon file to be displayed in the system tray.
            - commands: Optional. A list of tuples representing context menu commands. If None, no context menu will be set up.
            - popup (Optional[str]): The text to display as a tooltip when hovering over the notify icon.
        """
        super().__init__()
        self._icon = icon
        self._commands = commands
        self._popup = popup

        if self._icon:
            self.Icon = Drawing.Icon(str(self._icon))

        if self._popup:
            self.Text = self._popup
        
        if self._commands:
            self.context_menu = Forms.ContextMenuStrip()
            for command in self._commands:
                self.context_menu.Items.Add(command)
            self.ContextMenuStrip = self.context_menu

    

    @property
    def popup(self) -> Optional[str]:
        """
        Gets the current tooltip text for the NotifyIcon.
        """
        return self._popup
    


    @popup.setter
    def popup(self, value: Optional[str]):
        """
        Sets the tooltip text for the NotifyIcon and updates the NotifyIcon's Text property.
        """
        self._popup = value
        if self._popup is not None:
            self.Text = self._popup
        else:
            self.Text = ""



    def show(self):
        """
        Displays the NotifyIcon in the system tray.
        """
        self.Visible = True

    def hide(self):
        """
        Hides the NotifyIcon from the system tray and disposes of the icon resources.
        """
        self.Visible = False
        self.Dispose()