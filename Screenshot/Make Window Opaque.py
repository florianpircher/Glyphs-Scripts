__MenuTitle__ = {
	"de": "​​​​​​Fenster opak machen",
	"en": "​​​​​​Make Window Opaque",
}
__MenuDescription__ = {
	"de": "Setzt den Alpha-Wert des vordersten Fensters auf 1. Hilfreich, um den Effekt des „Fenster transparent machen”-Skripts zu reversieren.",
	"en": "Sets the alpha value of the frontmost window to 1. Helpful for resetting the effects of the “Make Window Transparent” script.",
}

from Cocoa import NSApp

NSApp.keyWindow().setAlphaValue_(1)
