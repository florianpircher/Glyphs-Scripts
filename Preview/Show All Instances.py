__MenuTitle__ = {
	"de": "​Alle Instanzen anzeigen",
	"en": "​Show All Instances",
}
__MenuDescription__ = {
	"de": "Zeigt alle Instanzen für die „Alle Instanzen anzeigen“-Option in der Instanzenvorschau und im Vorschau-Fenster.",
	"en": "Shows all instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.",
}

Font.disableUpdateInterface()

for instance in Font.instances:
	instance.visible = True

Font.enableUpdateInterface()
