# MenuTitle: Select Nodes Between Bounding Nodes

__doc__="""
For each path on the active layer:
1. If the path has two selected nodes, select all nodes in between.
2. If a path has a single contiguous chain of selected nodes, invert the selection but keep the first and last nodes selected.
3. Otherwise, do nothing with the path.
"""

def process_path(path):
    nodes = path.nodes
    nodes_count = len(nodes)
    
    if nodes_count < 2:
        return
    
    is_closed = path.closed
    selected_nodes = []
    previous_node = nodes[-1] if is_closed else None
    is_wrapping_selection = previous_node and previous_node.selected and nodes[0].selected
    contiguous_selection_ranges = []
    
    for i, node in enumerate(nodes):
        if node.selected:
            selected_nodes.append(node)
            is_continuation = previous_node and previous_node.selected
            if i == nodes_count - 1 and is_wrapping_selection:
                if len(contiguous_selection_ranges) < 2:
                    return
                continuation_start_index = contiguous_selection_ranges[-1][0] if is_continuation else i
                if is_continuation:
                    contiguous_selection_ranges.pop()
                contiguous_selection_ranges[0] = (continuation_start_index, contiguous_selection_ranges[0][-1])
            elif is_continuation and len(contiguous_selection_ranges) > 0:
                contiguous_selection_ranges[-1] = (contiguous_selection_ranges[-1][0], i)
            else:
                contiguous_selection_ranges.append((i, i))
        previous_node = node
    
    selected_count = len(selected_nodes)
    
    # Rule 1: Two selected nodes, select all nodes in between
    if selected_count == 2:
        start_node, end_node = selected_nodes
        start_index = nodes.index(start_node)
        end_index = nodes.index(end_node)
        if abs(end_index - start_index) == 1 or (is_closed and abs(end_index - start_index) == nodes_count - 1):
            # Boudning nodes are next to each other: select all nodes
            for node in nodes:
                node.selected = True
        else:
            # Select all nodes between the selected nodes
            is_forward = start_index < end_index
            range_start_index = start_index + 1 if is_forward else end_index + 1
            range_end_index = end_index if is_forward else start_index
            for i in range(range_start_index, range_end_index):
                nodes[i].selected = True
    
    # Rule 2: Single contiguous chain of selected nodes, invert selection but keep first and last nodes selected
    elif selected_count > 2 and len(contiguous_selection_ranges) == 1:
        for node in nodes:
            node.selected = not node.selected
        start_index, end_index = contiguous_selection_ranges[0]
        nodes[start_index].selected = True
        nodes[end_index].selected = True

for path in Layer.paths:
    process_path(path)
