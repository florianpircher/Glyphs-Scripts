from typing import FrozenSet
import math


def targetNodes(source, OFFCURVE):
    targets = set()

    if isinstance(source, FrozenSet):
        for handle in source:
            if handle.nextNode.type != OFFCURVE:
                targets.add(handle.nextNode)
            if handle.prevNode.type != OFFCURVE:
                targets.add(handle.prevNode)
    else:
        targets.add(source.prevNode)
        targets.add(source.nextNode)

    return targets


def sourcePosition(source):
    if isinstance(source, FrozenSet):
        x = 0
        y = 0

        for handle in source:
            x += handle.position.x
            y += handle.position.y

        n = len(source)
        nx = x / n
        ny = y / n

        return (nx, ny)

    else:
        return (source.position.x, source.position.y)


def expandMatch(match, OFFCURVE):
    if match.type == OFFCURVE:
        fullMatch = [match]

        if match.nextNode.type == OFFCURVE:
            fullMatch.append(match.nextNode)
        if match.prevNode.type == OFFCURVE:
            fullMatch.append(match.prevNode)

        return fullMatch
    else:
        return [match]


def distanceBetween(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def toggleSelect(layer, OFFCURVE, h, v):
    selectionGroups = set()

    for node in layer.selection:
        if node.type == OFFCURVE:
            off = [node]

            if node.nextNode.type == OFFCURVE:
                off.append(node.nextNode)
            if node.prevNode.type == OFFCURVE:
                off.append(node.prevNode)

            group = frozenset(off)
            selectionGroups.add(group)
        else:
            selectionGroups.add(node)

    markUnselect = set()
    select = set()

    for group in selectionGroups:
        targets = targetNodes(group, OFFCURVE)
        (fx, fy) = sourcePosition(group)
        minDistance = math.inf
        match = None
        hasVPIMatch = False

        for target in targets:
            (tx, ty) = (target.position.x, target.position.y)

            if h == 1 and v == 0:  # right
                if tx <= fx:
                    continue
            elif h == -1 and v == 0:  # left
                if tx >= fx:
                    continue
            elif h == 0 and v == 1:  # up
                if ty <= fy:
                    continue
            elif h == 0 and v == -1:  # down
                if ty >= fy:
                    continue

            isVPIMatch = target.type == OFFCURVE

            if hasVPIMatch and not isVPIMatch:
                continue

            distance = distanceBetween((fx, fy), (tx, ty))

            if distance < minDistance:
                minDistance = distance
                match = target
                hasVPIMatch = hasVPIMatch or isVPIMatch

        if match is not None:
            if isinstance(group, FrozenSet):
                for handle in group:
                    markUnselect.add(handle)
            else:
                markUnselect.add(group)

            fullMatch = expandMatch(match, OFFCURVE)
            select.update(fullMatch)

    unselect = markUnselect - select

    for node in unselect:
        node.selected = False

    for node in select:
        node.selected = True
