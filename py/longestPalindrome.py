def longestPalindrome(s):
    max1 = 0
    max2 = 0
    l = len(s)
    idx1 = 0
    idx2 = 0
    for i, c in enumerate(s):
        if i != 0:
            t = 0
            j = i-1
            k = i+1
            while j>=0 and k < l and s[j]==s[k]:
                t = t + 1
                j = j-1
                k = k+1
                if t >= max1:
                    idx1 = i
            max1 = max(t,max1)
            if s[i]==s[i-1]:
                t = 1
                j = i-2
                k = i+1
                if idx2==0:
                    idx2 = i
                while j>=0 and k < l and s[j]==s[k]:
                    t = t + 1
                    j = j-1
                    k = k+1
                    if t >= max2:
                        idx2 = i
                max2 = max(t,max2)
    if max2*2>max1*2+1:
        return s[idx2-max2:idx2+max2]
    else:
        return s[idx1-max1:idx1+max1+1]

print(longestPalindrome('aaaa'))