#MenuTitle: ​​​Show No Instances
__doc__ = """
Hides all instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.
"""

Font.disableUpdateInterface()

for instance in Font.instances:
	instance.visible = False

Font.enableUpdateInterface()
