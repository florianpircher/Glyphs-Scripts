#MenuTitle: Capture Window Content
"""Print the content of the frontmost window to a PDF on the desktop."""

if document := Glyphs.keyWindow():
  window = document.windowController().window()
  
  contentView = window.contentView()
  rect = contentView.bounds()
  data = contentView.dataWithPDFInsideRect_(rect)
  
  with open(f"/Users/Florian/Desktop/Window Content.pdf", "wb") as writer:
    writer.write(data)
