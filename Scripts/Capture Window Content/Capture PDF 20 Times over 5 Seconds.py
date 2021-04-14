# MenuTitle: Capture PDF 20 Times over 5 Seconds
"""Print the content of the frontmost window to a PDF on the desktop 20 times within 5 seconds."""

from AppKit import (NSObject, NSTimer)
from CaptureWindowContent import (captureWindowContent, writeFile)

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
