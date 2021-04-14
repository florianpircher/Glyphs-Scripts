# MenuTitle: Toggle Select Segment Down
__doc__ = """
If an on-curve node is selected, selectes the handles below; otherwise the on-curve node below the selected handles is selected.
"""

from ToggleSelectSegment import toggleSelect


toggleSelect(Layer, OFFCURVE, 0, -1)
