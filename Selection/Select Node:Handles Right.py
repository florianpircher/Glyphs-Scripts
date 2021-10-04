__MenuTitle__ = {
	"de": "​​Knoten/Anfasser-Paar rechts auswählen",
	"en": "​​Select Node/Handles Right",
}
__MenuDescription__ = {
	"de": "Wählt den Knoten oder die zwei Anfasser rechts der aktuellen Auswahl aus.",
	"en": "Selects the on-curve node or the two off-curve nodes to the right of the current selection.",
}

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, 1, 0)
