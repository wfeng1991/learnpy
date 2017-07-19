class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        l = len(flowerbed)
        if l<1:
            return n<=l
        if l==1:
            return l==n and flowerbed[0]==0
        jump=False
        next=0
        i = 0
        cnt=0
        while i<l-1:
            next = flowerbed[i+1]
            cur=flowerbed[i]
            if next==1:
                jump=True
            else:
                if cur==1:
                    jump=True
                else:
                    if not jump:
                        cnt+=1
                        jump=True
                    else:
                        jump=False
            i+=1
        if not jump and not flowerbed[-1]:
            cnt+=1
        if cnt>=n:
            return True
        else:
            return False