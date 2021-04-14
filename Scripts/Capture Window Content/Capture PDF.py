# MenuTitle: Capture PDF
"""Writes the contents of the frontmost window to a PDF file on the desktop."""

from CaptureWindowContent import (captureWindowContent, writeFile)

if info := captureWindowContent(Glyphs):
    data, name = info
    writeFile(data, name)
