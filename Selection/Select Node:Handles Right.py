#MenuTitle: ​​Select Node/Handles Right
__doc__ = """
Selects the on-curve node or the two off-curve nodes to the right of the current selection.
"""

from ToggleSelectSegment import toggleSelect

toggleSelect(Layer, OFFCURVE, 1, 0)
