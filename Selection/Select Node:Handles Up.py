__MenuTitle__ = {
	"de": "​​​Knoten/Anfasser-Paar oben auswählen",
	"en": "​​​Select Node/Handles Up",
}
__MenuDescription__ = {
	"de": "Wählt den Knoten oder die zwei Anfasser oberhalb der aktuellen Auswahl aus.",
	"en": "Selects the on-curve node or the two off-curve nodes above the current selection.",
}

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, 0, 1)
