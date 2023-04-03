class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        short = ""
        for i in range(1, len(strs)):
            short = min(strs[0], strs[i])
        for i in range(len(short)):
            for j in strs:
                print(i)
                print(len(j))
                if i > len(j) - 1:
                    return ans
                if short[i] != j[i]:
                    return ans
            ans += short[i]
        if len(strs) < 2:
            ans = strs[0]
        return ans

        """
        :type strs: List[str]
        :rtype: str
        """