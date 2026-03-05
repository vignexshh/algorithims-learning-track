def findRepeatedDnaSequences(s):
    visited = {}
    for i in range(len(s)):

        window = s[0+i:10+i]
        if len(window) == 10:

            if window in visited:
                visited[window] += 1

            if window not in visited:
                visited[window] = 0

        else:
            break

    return [name for name, value in visited.items() if value > 0]


print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))