__MenuTitle__ = {
	"de": "​​​Fenster als PDF 20 Mal über 5 Sekunden sichern",
	"en": "​​​Capture Window to PDF 20 Times over 5 Seconds",
}
__MenuDescription__ = {
	"de": "Schreibt ein PDF mit den Inhalten des vordersten Fensters 20 Mal auf den Schreibtisch innerhalb von 5 Sekunden.",
	"en": "Writes the contents of the frontmost window to a PDF file on the desktop 20 times within 5 seconds.",
}

from CaptureWindowContent import (captureWindowContent, writeFile)
from AppKit import (NSObject, NSTimer)


TOTAL_TIME = 5
TOTAL_COUNT = 20

try:
    saveWindowContentRepeatedly = SaveWindowContentRepeatedly.new()
except Exception as e:
    class SaveWindowContentRepeatedly(NSObject):
        timer = None
        count = 0

        @objc.python_method
        def setTimer(self):
            self.count = TOTAL_COUNT
            self.timer = NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
                TOTAL_TIME / TOTAL_COUNT, self, self.handleTimer, None, True)

        def handleTimer(self):
            self.count -= 1

            if self.count < 1:
                self.timer.invalidate()

            counter = TOTAL_COUNT - self.count

            if info := captureWindowContent(Glyphs):
                data, name = info
                writeFile(data, name, counter=counter)

    saveWindowContentRepeatedly = SaveWindowContentRepeatedly.new()

saveWindowContentRepeatedly.setTimer()
