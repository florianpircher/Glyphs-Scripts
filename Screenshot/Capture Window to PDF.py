__MenuTitle__ = {
	"de": "​Fenster als PDF sichern",
	"en": "​Capture Window to PDF",
}
__MenuDescription__ = {
	"de": "Schreibt ein PDF mit den Inhalten des vordersten Fensters auf den Schreibtisch.",
	"en": "Writes the contents of the frontmost window to a PDF file on the desktop.",
}

from CaptureWindowContent import (captureWindowContent, writeFile)


if info := captureWindowContent(Glyphs):
    data, name = info
    writeFile(data, name)
