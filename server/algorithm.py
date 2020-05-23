# Knuth Morris Pratt Algorithm
def borderFunction(pattern, M):
    prev = 0
    res = [0]*M
    i = 1
    while i < M:
        if pattern[i] == pattern[prev]:
            prev += 1
            res[i] = prev
            i += 1
        else:
            if prev != 0:
                prev = res[prev - 1]
            else:
                res[i] = 0
                i += 1
    return res


def searchKMP(pattern, text):
    pattern = pattern
    text = text
    M = len(pattern)
    N = len(text)

    border = borderFunction(pattern, M)

    i, j = 0, 0  # index text, pattern
    while i < N: 
        if pattern[j] == text[i]: 
            i += 1
            j += 1
        if j == M: 
            return i - j
        elif i < N and pattern[j] != text[i]:
            if j != 0: 
                j = border[j-1] 
            else: 
                i += 1
    return -1


# Boyer-Moore Algorithm
def lastOccurrence(pattern, M):
    last = [-1]*128  # ASCII

    for i in range(M):
        last[ord(pattern[i])] = i  # char to int, ASCII code

    return last


def searchBM(pattern, text):
    pattern = pattern
    text = text
    M = lengthPattern = len(pattern)
    N = lengthText = len(text)

    lastO = lastOccurrence(pattern, M)

    idxFound = 0
    while(idxFound <= N - M):
        j = M-1
        while j >= 0 and pattern[j] == text[idxFound + j]:
            j -= 1
        if j < 0:
            return idxFound
        else:
            idxFound += max(1, j - lastO[ord(text[idxFound + j])])

    return -1


# Regex
def searchRegex(pattern, text):
    import re
    return re.search(pattern, text)
