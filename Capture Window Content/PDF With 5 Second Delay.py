#MenuTitle: Capture Window Content With 5 Second Delay
"""Print the content of the frontmost window to a PDF on the desktop 5 seconds after invoking the script."""

from AppKit import (NSObject, NSTimer)

try:
  saveWindowContentWithDelay = SaveWindowContentWithDelay.new()
except Exception as e:
  class SaveWindowContentWithDelay(NSObject):
    @objc.python_method
    def setTimer(self):
      NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_(
        5, self, self.handleTimer, None, False)
  
    def handleTimer(self):
      if document := Glyphs.keyWindow():
        window = document.windowController().window()
  
        contentView = window.contentView()
        rect = contentView.bounds()
        data = contentView.dataWithPDFInsideRect_(rect)
  
        with open(f"/Users/Florian/Desktop/Window Content.pdf", "wb") as writer:
          writer.write(data)
  
  saveWindowContentWithDelay = SaveWindowContentWithDelay.new()

saveWindowContentWithDelay.setTimer()
