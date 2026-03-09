def findSubString(s, words):


    clone = words.copy()
    wordlen = len(words[0])
    right = 0

    while right != len(s):
        if s[right:wordlen] in clone:
            clone.remove(s[right:wordlen])
        if s[right:wordlen] not in clone:
            index = wordlen - right
            pass

        right += wordlen
        wordlen += wordlen
        # right = None



print(findSubString("barfoothefoobarman", ["foo","bar"]))