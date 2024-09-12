import clr
clr.AddReference('System.Drawing')

from System.Drawing import Font as DrawingFont, FontFamily, FontStyle

class Font:
    """
    A class containing commonly used fonts and a method for custom font creation.
    """
    # Define some commonly used fonts
    ARIAL = DrawingFont(FontFamily.GenericSansSerif, 12, FontStyle.Regular)
    TIMES_NEW_ROMAN = DrawingFont(FontFamily.GenericSerif, 12, FontStyle.Regular)
    COURIER_NEW = DrawingFont(FontFamily.GenericMonospace, 12, FontStyle.Regular)
    VERDANA = DrawingFont(FontFamily.GenericSansSerif, 12, FontStyle.Regular)

    @staticmethod
    def font(family_name, size, style=FontStyle.Regular):
        """
        Create a custom font with specified family, size, and style.

        Args:
            - family_name (str): The name of the font family.
            - size (float): The size of the font.
            - style (System.Drawing.FontStyle): The style of the font (e.g., Regular, Bold, Italic).

        Returns:
            - System.Drawing.Font: A custom font with the specified attributes.
        """
        try:
            font_family = FontFamily(family_name)
            return DrawingFont(font_family, size, style)
        except Exception as e:
            raise ValueError(f"Error creating font: {e}")