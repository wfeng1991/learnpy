class Solution(object):
    def leastInterval1(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        tasksN=[0]*26
        taskInterval=[0]*26
        for c in tasks:
            tasksN[ord(c)-ord('A')]+=1
        r=0
        s=sum(tasksN)
        while s>0:
            k=-1
            m=0
            for i,t in enumerate(tasksN):
                if t>m and taskInterval[i]==0:
                    m=t
                    k=i
            if k!=-1:
                taskInterval[k]=n
                tasksN[k]-=1
                s-=1
                p=0
                r+=1
                while p<26:
                    if p==k:
                        p+=1
                        continue
                    if taskInterval[p]>0:
                        taskInterval[p]-=1
                    p+=1
            else:
                r+=1
                p=0
                while p<26:
                    if taskInterval[p]>0:
                        taskInterval[p]-=1  
                    p+=1
        return r

    def leastInterval2(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic=[0]*26
        for c in tasks:
            dic[ord(c)-ord('A')]+=1
        dic.sort()
        time=0
        while dic[25]>0:
            i=0
            while i<=n:
                if dic[25]==0:
                    break
                if i<26 and dic[25-i]>0:
                    dic[25-i]-=1
                time+=1
                i+=1
            dic.sort()
        return time

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic=[0]*26
        for c in tasks:
            dic[ord(c)-ord('A')]+=1
        dic.sort()
        max_val=dic[25]-1
        idle_slots = max_val*n
        i=24
        while i>=0 and dic[i]>0:
            idle_slots-=min(max_val,dic[i])
            i-=1
        return len(tasks) if idle_slots==0 else idle_slots+len(tasks)
print(Solution().leastInterval(['A','A','A','A','A','A','B','C','D','E','F','G'], 2))
        
                