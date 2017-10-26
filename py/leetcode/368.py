class Solution(object):
    def largestDivisibleSubset1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def help(nums,index,t,res):
            if index==len(nums) and t:
                res.append(t)
            elif index<len(nums):
                can=True
                if t and nums[index]%t[-1]:
                    can=False
                if can:
                    help(nums,index+1,t+[nums[index]],res)
                    help(nums,index+1,t,res)
                else:
                    help(nums,index+1,t,res)
        res=[]
        help(sorted(nums),0,[],res)
        m=0
        r=[]
        for p in res:
            if len(p)>m:
                m=len(p)
                r=p
        return r
    
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[1]*len(nums)
        parent=[x for x in range(len(nums))]
        nums=sorted(nums)
        maxlen,maxidx=0,-1
        for i,n in enumerate(nums):
            m=0
            for j in range(i):
                if n%nums[j]==0 and l[j]>m:
                    m=l[j]
                    l[i]=l[j]+1
                    parent[i]=j
            if l[i]>maxlen:
                maxlen=l[i]
                maxidx=i
        res=[]
        if maxidx>-1:
            i=maxidx
            res.append(nums[parent[i]])
            while parent[i]!=i:
                res.append(nums[parent[i]])
                i=parent[i]
        return res

print(Solution().largestDivisibleSubset([3,2,8,16]))
