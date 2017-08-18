class Solution(object):
    def originalDigits1(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic=[
            ['0','zero'],
            ['1','one'],
            ['2','two'],
            ['3','three'],
            ['4','four'],
            ['5','five'],
            ['6','six'],
            ['7','seven'],
            ['8','eight'],
            ['9','nine'],
        ]
        chrs=dict()
        for c in s:
            if c in chrs:
                chrs[c]+=1
            else:
                chrs[c]=1
        r=''
        ff=True
        while ff:
            for n in dic:
                f=True
                for c in n[1]:
                    if c not in chrs or chrs[c]==0:
                        f=False
                        break
                if f:
                    r+=n[0]
                    for c in n[1]:
                        chrs[c]-=1
            ff=False
            for c in chrs:
                if chrs[c]:
                    ff=True
        return ''.join(sorted(r,key=lambda x:x))


    # The idea is:
    # for zero, it's the only word has letter 'z',
    # for two, it's the only word has letter 'w',
    # ......
    # so we only need to count the unique letter of each word, Coz the input is always valid.
    # int[] count = new int[10];
    # for (int i = 0; i < s.length(); i+=1){
    #     char c = s.charAt(i);
    #     if (c == 'z') count[0]+=1;
    #     if (c == 'w') count[2]+=1;
    #     if (c == 'x') count[6]+=1;
    #     if (c == 's') count[7]+=1; #7-6
    #     if (c == 'g') count[8]+=1;
    #     if (c == 'u') count[4]+=1; 
    #     if (c == 'f') count[5]+=1; #5-4
    #     if (c == 'h') count[3]+=1; #3-8
    #     if (c == 'i') count[9]+=1; #9-8-5-6
    #     if (c == 'o') count[1]+=1; #1-0-2-4
    # }
    # count[7] -= count[6];
    # count[5] -= count[4];
    # count[3] -= count[8];
    # count[9] = count[9] - count[8] - count[5] - count[6];
    # count[1] = count[1] - count[0] - count[2] - count[4];
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        count=[0]*10
        for c in s:
            if c == 'z':
                count[0]+=1
            if c == 'w':
                count[2]+=1
            if c == 'x': 
                count[6]+=1
            if c == 's': 
                count[7]+=1 #7-6
            if c == 'g': 
                count[8]+=1
            if c == 'u': 
                count[4]+=1 
            if c == 'f': 
                count[5]+=1 #5-4
            if c == 'h': 
                count[3]+=1 #3-8
            if c == 'i': 
                count[9]+=1 #9-8-5-6
            if c == 'o': 
                count[1]+=1 #1-0-2-4
        count[7] -= count[6]
        count[5] -= count[4]
        count[3] -= count[8]
        count[9] = count[9] - count[8] - count[5] - count[6]
        count[1] = count[1] - count[0] - count[2] - count[4]
        r=''
        for i,n in enumerate(count):
            r+=str(i)*n
        return r
print(Solution().originalDigits("zerozero"))