class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt=[0]*26
        start=maxCount=maxLength=0
        for end,c in enumerate(s):
            cnt[ord(c)-ord('A')]+=1
            maxCount=max(maxCount,cnt[ord(c)-ord('A')])
            while end-start+1-maxCount>k:
                cnt[ord(s[start])-ord('A')]-=1
                start+=1
            maxLength=max(maxLength,end-start+1)
        return maxLength