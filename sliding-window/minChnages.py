class Solution:
    def minOperations(self, s: str) -> int:
        changes = 0
        i=0

        while i+1 <= (len(s)):
            changes += int(s[i-1]) + int(s[i])
            i+=1

        return changes

x = Solution()
print(x.minOperations(("0100")))