__MenuTitle__ = {
	"de": "​​​​Unteren Knoten/unteres Anfasser-Paar auswählen",
	"en": "​​​​Select Node/Handles Down",
}
__MenuDescription__ = {
	"de": "Wählt den Knoten oder die zwei Anfasser unterhalb der aktuellen Auswahl aus.",
	"en": "Selects the on-curve node or the two off-curve nodes below the current selection.",
}

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, 0, -1)
