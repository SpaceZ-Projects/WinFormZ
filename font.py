import clr
clr.AddReference('System.Drawing')

from System.Drawing import FontFamily, FontStyle

class Font:
    """
    A class containing commonly used fonts and a method for custom font creation.
    """
    # Define some commonly used fonts
    SERIF = FontFamily.GenericSerif
    MONOSPACE = FontFamily.GenericMonospace
    SANSSERIF = FontFamily.GenericSansSerif


class Style:
    """
    A class containing commonly used fonts_style and a method for custom font creation.
    """
    # Define some commonly used fonts_style

    REGULAR = FontStyle.Regular
    BOLD = FontStyle.Bold
    ITALIC = FontStyle.Italic