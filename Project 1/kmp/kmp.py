import sys, time

def preprocessNeedle(needle, N, processedNeedle):
    """
    needle: substring to be searched for
    N: len(needle)
    processedNeedle: array storing length of longest (prefix, suffix) pairs which would tell us how many indices to jump if mismatch happens in haystack
    """
    leftCursor = 0 # also represents length of longest (prefix, suffix) pair
    rightCursor = 1

    # note (prefix, suffix) pair will be referred to as pair from here on out
    while rightCursor < N:
        # if match found
        if needle[leftCursor] == needle[rightCursor]:
            leftCursor += 1 # pairLength += 1
            processedNeedle[rightCursor] = leftCursor # update pairLength to processedNeedle
            rightCursor += 1
        else:
            # if there wasnt any match at all OR
            # leftCursor bumped down due to mismatch
            # basically leftCursor index 0 of needle
            if leftCursor == 0:
                rightCursor += 1
            # mismatch but leftCursor != 0
            else:
                leftCursor = processedNeedle[leftCursor - 1] # bump down leftCursor based on last stored pairLength/leftCursor value in processedNeedle

def KMPhn(needle, haystack):
    H = len(haystack)
    N = len(needle)
    cursorN = 0
    cursorH = 0
    indices = []
    
    processedNeedle = [0]*N # init processedNeedle (see preprocessNeedle for definition of processedNeedle
    preprocessNeedle(needle, N, processedNeedle)

    # iterate through haystack
    while cursorH < H:
        # if match found continue searching
        if needle[cursorN] == haystack[cursorH]:
            cursorH += 1
            cursorN += 1
        # mismatch occurs
        else:
            # either no match found at all so far OR
            # cursorN bumped down to index 0
            # basically as long as cursorN is at index 0
            if cursorN == 0:
                cursorH += 1 # move cursor in haystack only
            else:
                cursorN = processedNeedle[cursorN - 1] # bump cursorN to last knownindex of processedNeedle, which is the longest pairLength
        if cursorN == N:
            indices.append(cursorH - N)
            cursorN = processedNeedle[cursorN - 1] # bump cursorN to last knownindex of processedNeedle, which is the longest pairLength
    return indices
