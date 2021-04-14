# MenuTitle: Toggle Select Segment Left
"""
If an on-curve node is selected, selectes the handles to the left; otherwise the on-curve node to the left of the selected handles is selected.
"""

from ToggleSelectSegment import toggleSelect


toggleSelect(Layer, OFFCURVE, -1, 0)
