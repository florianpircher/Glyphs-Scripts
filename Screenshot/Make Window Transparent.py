__MenuTitle__ = {
	"de": "​​​​​Fenster transparent machen",
	"en": "​​​​​Make Window Transparent",
}
__MenuDescription__ = {
	"de": "Setzt den Alpha-Wert des vordersten Fensters auf 0. Hilfreich, falls Bildschirmfotos von Popover-Fenstern gemacht werden sollen (welche nicht von diesem Skript beeinflusst werden).",
	"en": "Sets the alpha value of the frontmost window to 0. Helpful for screenshotting popovers (which are not affected by this script).",
}

from Cocoa import NSApp

NSApp.keyWindow().setAlphaValue_(0)
