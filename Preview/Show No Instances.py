__MenuTitle__ = {
	"de": "​​​Keine Instanzen anzeigen",
	"en": "​​​Show No Instances",
}
__MenuDescription__ = {
	"de": "Versteckt alle Instanzen für die „Alle Instanzen anzeigen“-Option in der Instanzenvorschau und im Vorschau-Fenster.",
	"en": "Hides all instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.",
}

Font.disableUpdateInterface()

for instance in Font.instances:
	instance.visible = False

Font.enableUpdateInterface()
