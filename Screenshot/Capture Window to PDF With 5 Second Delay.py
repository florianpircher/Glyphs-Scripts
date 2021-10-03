__MenuTitle__ = {
	"de": "​​Fenster als PDF mit 5 Sekunden Verzögerung sichern",
	"en": "​​Capture Window to PDF With 5 Second Delay",
}
__MenuDescription__ = {
	"de": "Schreibt ein PDF mit den Inhalten des vordersten Fensters auf den Schreibtisch mit einer Verzögerung von 5 Sekunden.",
	"en": "Writes the contents of the frontmost window to a PDF file on the desktop 5 seconds after invoking the script.",
}

from AppKit import (NSObject, NSTimer)
from CaptureWindowContent import (captureWindowContent, writeFile)


try:
    saveWindowContentWithDelay = SaveWindowContentWithDelay.new()
except Exception as e:
    class SaveWindowContentWithDelay(NSObject):
        @objc.python_method
        def setTimer(self):
            NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                5, self, self.handleTimer, None, False)

        def handleTimer(self):
            if info := captureWindowContent(Glyphs):
                data, name = info
                writeFile(data, name)

    saveWindowContentWithDelay = SaveWindowContentWithDelay.new()

saveWindowContentWithDelay.setTimer()
