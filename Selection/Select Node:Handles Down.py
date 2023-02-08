#MenuTitle: ​​​​Select Node/Handles Down
__doc__ = """
Selects the on-curve node or the two off-curve nodes below the current selection.
"""

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, 0, -1)
