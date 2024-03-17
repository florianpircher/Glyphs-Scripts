# Florian Pircher’s Scripts

Make change that gets overwritten by a force push.

- one

Florian Pircher’s Python scripts for the [Glyphs](https://glyphsapp.com) font editor.

## Preview

### Show All Instances

Shows all instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.

### Show Active Instances Only

Shows only active instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.
Set the active state of an instance in File → Font Info… → Exports.

### Show No Instances

Hides all instances when “Show All Instances” is selected in the preview in Edit View and in the Preview Panel.

## Selection

### Select Nodes Between Bounding Nodes

For each path on the active layer:

1. If the path has two selected nodes, select all nodes in between.
2. If a path has a single contiguous chain of selected nodes, invert the selection but keep the first and last nodes selected.
3. Otherwise, do nothing with the path.

### ​Select Node/Handles {Left, Right, Up, Down}

Selects the on-curve node or the two off-curve nodes {to the left of, to the right of, above, below} the current selection

These scripts are an extension to the [Keyboard Selection Travel](https://github.com/florianpircher/Keyboard-Selection-Travel) plugin.

## Screenshot

The screenshot scripts are helpful when documenting Glyphs, Glyphs workflows, or Glyphs extensions.

### Capture Window to PDF

Writes the contents of the frontmost window to a PDF file on the desktop.

### Capture Window to PDF With 5 Second Delay

Writes the contents of the frontmost window to a PDF file on the desktop 5 seconds after invoking the script.

### Capture Window to PDF 20 Times over 5 Seconds

Writes the contents of the frontmost window to a PDF file on the desktop 20 times within 5 seconds.

### Make Window Transparent

Sets the alpha value of the frontmost window to 0.
Helpful for screenshotting popovers (which are not affected by this script).

### Make Window Opaque

Sets the alpha value of the frontmost window to 1.
Helpful for resetting the effects of the “Make Window Transparent” script.
