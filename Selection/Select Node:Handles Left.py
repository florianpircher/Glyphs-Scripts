__MenuTitle__ = {
	"de": "​Linken Knoten/linkes Anfasser-Paar auswählen",
	"en": "​Select Node/Handles Left",
}
__MenuDescription__ = {
	"de": "Wählt den Knoten oder die zwei Anfasser links der aktuellen Auswahl aus.",
	"en": "Selects the on-curve node or the two off-curve nodes to the left of the current selection.",
}

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, -1, 0)
