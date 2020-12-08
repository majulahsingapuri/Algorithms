def bruteForce(needle, haystack):

    needleLength = len(needle)
    haystackLength = len(haystack)
    indices = []

    found = False
    for haystackIdx in range(0, haystackLength - needleLength + 1):

        needleIdx = 0
        # loop through needle characters
        while (needleIdx < needleLength):
            # mismatch: return needle index to 0, compare with next char in haystack
            if haystack[needleIdx + haystackIdx] != needle[needleIdx]:
                break
            else:  # compare next char in needle
                needleIdx += 1
               
        if needleIdx == needleLength:
            found = True
            indices.append(haystackIdx)

    return indices
