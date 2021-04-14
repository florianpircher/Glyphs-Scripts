from pathlib import Path
import datetime


def captureWindowContent(Glyphs):
    if document := Glyphs.keyWindow():
        window = document.windowController().window()

        name = window.title() or "Window"

        contentView = window.contentView()
        rect = contentView.bounds()
        data = contentView.dataWithPDFInsideRect_(rect)

        return data, name

    return None


def writeFile(data, label, counter=None):
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H-%M-%S")

    if counter is not None:
        basename = f"{label} {counter}"
    else:
        basename = f"{label} {time}"

    filename = Path.home() / "Desktop" / f"{basename}.pdf"

    with open(filename, "wb") as writer:
        writer.write(data)
