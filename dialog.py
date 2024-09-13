import clr
clr.AddReference('System.Windows.Forms')

import System.Windows.Forms as Forms

from typing import Callable, Type

class Dialog(Forms.MessageBox):
    """
    Args:
        - message (str): The message to display in the message box.
        - title (str): The title of the message box. Defaults to "Message".
        - buttons (MessageButtons): The buttons to display in the message box.
        - icon (MessageIcon): The icon to display in the message box.
        - result (Callable[[DialogResult], None]): A function that takes a DialogResult and performs actions based on the result.
    """
    def __init__(
        self,
        message: str = None,
        title: str = None,
        buttons: Type[any] = None,
        icon: Type[any] = None,
        result: Callable = None
    ):
        """
        Args:
            - message (str): The message to display in the message box.
            - title (str): The title of the message box. Defaults to "Message".
            - buttons (MessageButtons): The buttons to display in the message box.
            - icon (MessageIcon): The icon to display in the message box.
            - result (Callable[[DialogResult], None]): A function that takes a DialogResult and performs actions based on the result.
        """
        self.message = message
        self.title = title
        if buttons:
            self.buttons = buttons
        else:
            self.buttons = Forms.MessageBoxButtons.OK
        if icon:
            self.icon = icon
        else:
            self.icon = Forms.MessageBoxIcon(0)
        self.result = result
        
        result = self.Show(self.message, self.title, self.buttons, self.icon)
        if self.result:
            self.result(result)
            return result
    


class MessageButtons:
    """The message box contains Abort, Retry, and Ignore buttons."""
    ABORTRETRYIGNORE = Forms.MessageBoxButtons.AbortRetryIgnore
    """The message box contains an OK button."""
    OK = Forms.MessageBoxButtons.OK
    """The message box contains OK and Cancel buttons."""
    OKCANCEL = Forms.MessageBoxButtons.OKCancel
    """The message box contains Retry and Cancel buttons."""
    RETRYCANCEL = Forms.MessageBoxButtons.RetryCancel
    """Forms.MessageBoxButtons."""
    YESNO = Forms.MessageBoxButtons.YesNo
    """The message box contains Yes, No, and Cancel buttons."""
    YESNOCANCEL = Forms.MessageBoxButtons.YesNoCancel


class MessageIcon:
    """The message box contains a symbol consisting of a lowercase letter i in a circle."""
    ASTERISK = Forms.MessageBoxIcon.Asterisk
    """The message box contains a symbol consisting of white X in a circle with a red background."""
    ERROR = Forms.MessageBoxIcon.Error
    """The message box contains a symbol consisting of an exclamation point in a triangle with a yellow background."""
    EXCLAMATION = Forms.MessageBoxIcon.Exclamation
    """The message box contains a symbol consisting of a white X in a circle with a red background."""
    HAND = Forms.MessageBoxIcon.Hand
    """The message box contains a symbol consisting of a lowercase letter i in a circle."""
    INFORMATION = Forms.MessageBoxIcon.Information
    """The message box contains no symbols."""
    NONE = Forms.MessageBoxIcon(0)
    """The message box contains a symbol consisting of a question mark in a circle."""
    QUESTION = Forms.MessageBoxIcon.Question
    """The message box contains a symbol consisting of white X in a circle with a red background."""
    STOP = Forms.MessageBoxIcon.Stop
    """The message box contains a symbol consisting of an exclamation point in a triangle with a yellow background."""
    WARNING = Forms.MessageBoxIcon.Warning