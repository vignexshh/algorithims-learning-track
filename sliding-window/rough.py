"""
s = "p w w k e w"

p, right=0, left=0 notepad = {p:1}, maxlen = 1
w, right=1, left = 0, notepad = {p:0, w:1}, maxlen = 2
w, right=2, left = 2, notepad = {p:0, w:}

"""

def comp(s):
    maxlen = 0
    left = 0
    notepad = {}
    for right in range(len(s)):
        if s[right] in notepad:

            left = max(left, notepad[s[right]]+ 1) #capture the index for the next new left new window lenght start

        notepad[s[right]] = right # capture letter frequency
        maxlen = max(maxlen, right - left +1) # maxlen = (get the current window length and previous length)


print(comp("abcabcbc"))
