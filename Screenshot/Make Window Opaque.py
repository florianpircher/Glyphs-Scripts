# MenuTitle: Make Window Opaque
__doc__ = """
Sets the alpha value of the frontmost window to 1. Helpful after the “Make Window Transparent” script.
"""

from Cocoa import NSApp

NSApp.keyWindow().setAlphaValue_(1)
