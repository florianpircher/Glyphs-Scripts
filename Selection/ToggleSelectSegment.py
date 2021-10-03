from typing import FrozenSet
import math


def expandGroup(group, OFFCURVE):
    if group.type == OFFCURVE:
        fullGroup = [group]

        if group.nextNode.type == OFFCURVE:
            fullGroup.append(group.nextNode)
        if group.prevNode.type == OFFCURVE:
            fullGroup.append(group.prevNode)

        return frozenset(fullGroup)
    else:
        return frozenset([group])


def targetGroups(source, OFFCURVE):
    targets = set()

    if isinstance(source, FrozenSet):
        for handle in source:
            if handle.nextNode.type != OFFCURVE:
                targets.add(frozenset([handle.nextNode]))
            if handle.prevNode.type != OFFCURVE:
                targets.add(frozenset([handle.prevNode]))
    else:
        targets.add(expandGroup(source.prevNode, OFFCURVE))
        targets.add(expandGroup(source.nextNode, OFFCURVE))

    return targets


def groupPosition(group):
    if isinstance(group, FrozenSet):
        x = 0
        y = 0

        for handle in group:
            x += handle.position.x
            y += handle.position.y

        n = len(group)
        nx = x / n
        ny = y / n

        return (nx, ny)
    else:
        return (group.position.x, group.position.y)


def distanceBetween(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def isVIPGroup(group, OFFCURVE):
    if isinstance(group, FrozenSet):
        for handle in group:
            if handle.type == OFFCURVE:
                return True

        return False
    else:
        return group.type == OFFCURVE


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
        targets = targetGroups(group, OFFCURVE)
        (fx, fy) = groupPosition(group)
        minDistance = math.inf
        match = None
        hasVPIMatch = False

        for target in targets:
            (tx, ty) = groupPosition(target)

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

            isVPIMatch = isVIPGroup(target, OFFCURVE)

            if hasVPIMatch and not isVPIMatch:
                continue

            distance = distanceBetween((fx, fy), (tx, ty))

            if (distance < minDistance) or (isVPIMatch and not hasVPIMatch):
                minDistance = distance
                match = target
                hasVPIMatch = hasVPIMatch or isVPIMatch

        if match is not None:
            if isinstance(group, FrozenSet):
                for handle in group:
                    markUnselect.add(handle)
            else:
                markUnselect.add(group)

            select.update(match)

    unselect = markUnselect - select

    for node in unselect:
        node.selected = False

    for node in select:
        node.selected = True
