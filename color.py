import clr
clr.AddReference('System.Drawing')

from System.Drawing import Color as DrawingColor

class Color:
    """
    A class containing commonly used colors.
    """
    AQUA = DrawingColor.Aqua
    ANTIQUEWHITE = DrawingColor.AntiqueWhite
    AQUAMARINE = DrawingColor.Aquamarine
    AZURE = DrawingColor.Azure
    WHITE = DrawingColor.White
    WHITESMOKE = DrawingColor.WhiteSmoke
    BLACK = DrawingColor.Black
    RED = DrawingColor.Red
    GREEN = DrawingColor.Green
    BLUE = DrawingColor.Blue
    ALICEBLUE = DrawingColor.AliceBlue
    LIGHT_BLUE = DrawingColor.LightBlue
    LIGHT_GRAY = DrawingColor.LightGray
    DARK_GRAY = DrawingColor.DarkGray
    YELLOW = DrawingColor.Yellow
    CYAN = DrawingColor.Cyan
    MAGENTA = DrawingColor.Magenta
    GRAY = DrawingColor.Gray
    TOMATO = DrawingColor.Tomato
    TURQUOISE = DrawingColor.Turquoise
    VIOLET = DrawingColor.Violet
    SILVER = DrawingColor.Silver
    SEAGREEN = DrawingColor.SeaGreen
    SANDYBROWN = DrawingColor.SandyBrown
    SALMON = DrawingColor.Salmon
    SADDLEBRWON = DrawingColor.SaddleBrown
    PURPLE = DrawingColor.Purple
    PINK = DrawingColor.Pink
    TRANSPARENT = DrawingColor.Transparent

    @staticmethod
    def rgb(r, g, b):
        """
        Create a custom color from RGB values.

        Args:
            r (int): The red component (0-255).
            g (int): The green component (0-255).
            b (int): The blue component (0-255).

        Returns:
            System.Drawing.Color: A custom color based on the given RGB values.
        """
        # Ensure RGB values are within the valid range
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return DrawingColor.FromArgb(r, g, b)