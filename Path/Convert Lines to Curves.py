#MenuTitle: Convert Lines to Curves
__doc__ = """
Converts the selected line segments to cubic curve segments.
If nothing is selected, converts all line segments in the layer.
"""

from Foundation import NSMakePoint

for layer in Glyphs.font.selectedLayers:
	if not layer.paths:
		continue
	
	for currPath in layer.paths:
		has_selection = any(node.selected for node in currPath.nodes)
		
		nodes_to_convert = []
		
		for nodeIdx, currNode in enumerate(currPath.nodes):
			if currNode.type == LINE:
				# if something is selected => only convert selected nodes
				# if nothing is selected => convert all line nodes
				if not has_selection or currNode.selected:
					nodes_to_convert.append(nodeIdx)
		
		for nodeIdx in reversed(sorted(nodes_to_convert)):
			currNode = currPath.nodes[nodeIdx]
			
			# previous on-curve node index
			prevIdx = nodeIdx - 1
			while prevIdx >= 0 and currPath.nodes[prevIdx].type == OFFCURVE:
				prevIdx -= 1
			
			if prevIdx < 0:
				prevIdx = len(currPath.nodes) - 1
				while prevIdx >= 0 and currPath.nodes[prevIdx].type == OFFCURVE:
					prevIdx -= 1
			
			if prevIdx >= 0:
				previousNode = currPath.nodes[prevIdx]
				P1 = previousNode.position
				P2 = currNode.position
				
				N2 = NSMakePoint(P1.x + ((P2.x - P1.x) / 3 * 2), P1.y + ((P2.y - P1.y) / 3 * 2))
				N1 = NSMakePoint(P1.x + ((P2.x - P1.x) / 3), P1.y + ((P2.y - P1.y) / 3))
				
				layer.stopUpdates()
				
				newNode2 = GSNode()
				newNode2.position = N2
				newNode2.type = OFFCURVE
				currPath.nodes.insert(nodeIdx, newNode2)
				
				newNode1 = GSNode()
				newNode1.position = N1
				newNode1.type = OFFCURVE
				currPath.nodes.insert(nodeIdx, newNode1)
				
				currNode.type = CURVE
				
				layer.startUpdates()
