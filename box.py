import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

import System.Drawing as Drawing
import System.Windows.Forms as Forms

from typing import Optional, Union, List, Tuple
from .color import Color

class Box(Forms.Panel):
    """
    Args:
        - size (Tuple[int, int]): The size of the box (width, height).
        - location (Tuple[int, int]): The location of the box (x, y).
        - background_color (Optional[Color]): The background color of the box.
    """

    def __init__(
        self,
        size: Tuple[int, int] = (100, 100),
        location: Tuple[int, int] = (0, 0),
        background_color: Optional[Color] = None
    ):
        """
        Args:
            - size (Tuple[int, int]): The size of the box (width, height).
            - location (Tuple[int, int]): The location of the box (x, y).
            - background_color (Optional[Color]): The background color of the box.
        """
        super().__init__()
        self._size = size
        self._location = location
        self._background_color = background_color
        
        self.Size = Drawing.Size(*self._size)
        self.Location = Drawing.Point(*self._location)
        if self._background_color:
            self.BackColor = self._background_color


    @property
    def size(self) -> Tuple[int, int]:
        """
        Gets or sets the size of the box (width, height).
        """
        return self._size

    @size.setter
    def size(self, value: Tuple[int, int]):
        """
        Sets the size of the box.
        
        Args:
            value (Tuple[int, int]): The width and height of the box.
        """
        self._size = value
        self.Size = Drawing.Size(*value)

    @property
    def location(self) -> Tuple[int, int]:
        """
        Gets or sets the location of the box (x, y).
        """
        return self._location

    @location.setter
    def location(self, value: tuple[int, int]):
        """
        Sets the location of the box.
        
        Args:
            value (tuple[int, int]): The x and y coordinates of the box.
        """
        self._location = value
        self.Location = Drawing.Point(*value)

    @property
    def background_color(self) -> Optional[Drawing.Color]:
        """
        Gets or sets the background color of the box.
        """
        return self._background_color

    @background_color.setter
    def background_color(self, value: Optional[Drawing.Color]):
        """
        Sets the background color of the box.
        
        Args:
            value (Optional[Drawing.Color]): The background color of the box. 
                                              If None, the background color will be set to Transparent.
        """
        self._background_color = value
        if value:
            self.BackColor = value


    
    def insert(self, controls: Union[Forms.Control, List[Forms.Control]]):
        """
        Inserts a list of objects into the box.
        
        Args:
            controls (Union[Forms.Control, List[Forms.Control]]): A single control or a list of controls to be added to the box.
        """
        if isinstance(controls, Forms.Control):
            self.Controls.Add(controls)
        elif isinstance(controls, list):
            for control in controls:
                if isinstance(control, Forms.Control):
                    self.Controls.Add(control)
                else:
                    raise TypeError("All items in the list must be instances of Forms.Control.")
        else:
            raise TypeError("controls must be a Forms.Control or a list of Forms.Control.")
        

    
    def remove(self, controls: Union[Forms.Control, List[Forms.Control]]):
        """
        Removes one or more controls from the box.
        
        Args:
            controls (Union[Forms.Control, List[Forms.Control]]): A single control or a list of controls to be removed from the box.
        """
        if isinstance(controls, Forms.Control):
            self.Controls.Remove(controls)
        elif isinstance(controls, list):
            for control in controls:
                if isinstance(control, Forms.Control):
                    self.Controls.Remove(control)
                else:
                    raise TypeError("All items in the list must be instances of Forms.Control.")
        else:
            raise TypeError("controls must be a Forms.Control or a list of Forms.Control.")
