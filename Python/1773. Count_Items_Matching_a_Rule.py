class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rule={"type":0,"color":1,"name":2}
        ans=0
        for item in items:
            if item[rule[ruleKey]]==ruleValue:
                ans+=1
        return ans