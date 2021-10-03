# MenuTitle: Isolate Sheet
__doc__ = """
Moves the topmost sheet of the current window to a separate, zero sized window.
"""

from Cocoa import (
    NSApp,
    NSWindow,
    NSWindowStyleMaskBorderless,
    NSWindowStyleMaskFullSizeContentView,
    NSZeroRect,
)


def isolateSheet():
    window = NSApp.keyWindow()

    if not window:
        return

    if window.isSheet():
        window = window.sheetParent()

    sheet = window.attachedSheet()

    if not sheet:
        return

    window.endSheet_(sheet)

    blankWindow = NSWindow.new()
    blankWindow.setStyleMask_(NSWindowStyleMaskFullSizeContentView | NSWindowStyleMaskBorderless)
    blankWindow.setFrame_display_(NSZeroRect, True)
    blankWindow.makeKeyAndOrderFront_(None)
    blankWindow.center()
    blankWindow.beginSheet_completionHandler_(sheet, None)


isolateSheet()
