#MenuTitle: ​​​​​Make Window Transparent
__doc__ = """
Sets the alpha value of the frontmost window to 0. Helpful for screenshotting popovers (which are not affected by this script).
"""

from Cocoa import NSApp

NSApp.keyWindow().setAlphaValue_(0)
