# MenuTitle: Capture PDF With 5 Second Delay
__doc__ = """
Writes the contents of the frontmost window to a PDF file on the desktop 5 seconds after invoking the script.
"""

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
