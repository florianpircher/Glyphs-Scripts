#MenuTitle: ​Show All Instances
__doc__ = """
Shows all instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.
"""

Font.disableUpdateInterface()

for instance in Font.instances:
	instance.visible = True

Font.enableUpdateInterface()
