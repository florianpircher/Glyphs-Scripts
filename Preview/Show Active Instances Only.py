__MenuTitle__ = {
	"de": "​​Nur aktive Instanzen anzeigen",
	"en": "​​Show Active Instances Only",
}
__MenuDescription__ = {
	"de": "Zeigt nur aktiven Instanzen für die „Alle Instanzen anzeigen“-Option in der Instanzenvorschau und im Vorschau-Fenster. Aktiviere und deaktiviere Instanzen in Datei → Schrift-Info… → Exportieren.",
	"en": "Shows only active instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel. Set the active state of an instance in File → Font Info… → Exports.",
}

Font.disableUpdateInterface()

for instance in Font.instances:
	instance.visible = instance.active

Font.enableUpdateInterface()
