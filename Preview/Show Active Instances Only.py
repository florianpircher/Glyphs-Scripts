#MenuTitle: ​​Show Active Instances Only
__doc__ = """
Shows only active instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel. Set the active state of an instance in File → Font Info… → Exports.
"""

Font.disableUpdateInterface()

for instance in Font.instances:
	instance.visible = instance.active

Font.enableUpdateInterface()
