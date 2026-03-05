def lengthOfLongestSubstring(s: str) -> int:
    """
    char_map is a dictionary used to track elements and their last index position.
    """
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            # Move left pointer to the right of the last seen duplicate
            left = max(left, char_map[s[right]] + 1)

        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length


print(lengthOfLongestSubstring('pwwkew'))

