#MenuTitle: ​​​Select Node/Handles Up
__doc__ = """
Selects the on-curve node or the two off-curve nodes above the current selection.
"""

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, 0, 1)
