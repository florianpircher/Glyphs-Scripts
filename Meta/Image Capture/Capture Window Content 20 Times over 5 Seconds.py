#MenuTitle: Capture Window Content 20 Times over 5 Seconds
"""Print the content of the frontmost window to a PDF on the desktop 20 times within 5 seconds."""

from AppKit import (NSObject, NSTimer)

TOTAL_TIME = 5
TOTAL_COUNT = 20

try:
  saveWindowContentWithDelay = SaveWindowContentWithDelay.new()
except Exception as e:
  class SaveWindowContentWithDelay(NSObject):
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
      
      if document := Glyphs.keyWindow():
        window = document.windowController().window()
  
        contentView = window.contentView()
        rect = contentView.bounds()
        data = contentView.dataWithPDFInsideRect_(rect)
  
        with open(f"/Users/Florian/Desktop/{TOTAL_COUNT - self.count}.pdf", "wb") as writer:
          writer.write(data)
  
  saveWindowContentWithDelay = SaveWindowContentWithDelay.new()

saveWindowContentWithDelay.setTimer()
