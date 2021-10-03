# Florian Pircher’s Scripts

Florian Pircher’s Python scripts for the [Glyphs](https://glyphsapp.com) font editor.

## Screenshot

### Capture PDF

Writes the contents of the frontmost window to a PDF file on the desktop.

### Capture PDF With 5 Second Delay

Writes the contents of the frontmost window to a PDF file on the desktop 5 seconds after invoking the script.

### Capture PDF 20 Times over 5 Seconds

Writes the contents of the frontmost window to a PDF file on the desktop 20 times within 5 seconds.

### Isolate Sheet

Moves the topmost sheet of the current window to a separate, zero sized window.

### Make Window Transparent

Sets the alpha value of the frontmost window to 0.
Helpful for screenshotting popovers (which are not affected by this script).

### Make Window Opaque

Sets the alpha value of the frontmost window to 1.
Helpful after the “Make Window Transparent” script.

## Selection

### Toggle Select Segment {Left, Right, Up, Down}

If an on-curve node is selected, selectes the handles {to the left, to the right, above, below}; otherwise the on-curve node {to the left, to the right, above, below} the selected handles is selected.
