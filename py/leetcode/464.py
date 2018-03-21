# 有两个人玩一个游戏，给定一个最大可取整数 maxChoosableInteger，
# 两个人轮流从1~maxChoosableInteger 中取一个数，取过的数不可再取，若其中一方取过以后，
# 所有取过的数加起来的和大于等于desiredTotal，那么这个人获胜。
# 现在给你maxChoosableInteger和desiredTotal，问先手是否必胜，假定游戏双方均采取最优策略。
# 你可以假定给出的 maxChoosableInteger不超过20,desiredTotal不超过300。
class Solution(object):
    # 这道题给了我们一堆数字，然后两个人，每人每次选一个数字，看数字总数谁先到给定值，
    # 有点像之前那道Nim Game，但是比那题难度大。我刚开始想肯定说用递归啊，结果写完发现TLE了，
    # 后来发现我们必须要优化效率，使用哈希表来记录已经计算过的结果。我们首先来看如果给定的数字范围大于等于目标值的话，
    # 直接返回true。如果给定的数字总和小于目标值的话，说明谁也没法赢，返回false。
    # 然后我们进入递归函数，首先我们查找当前情况是否在哈希表中存在，有的话直接返回即可。
    # 我们使用一个整型数按位来记录数组中的某个数字是否使用过，我们遍历所有数字，将该数字对应的mask算出来，
    # 如果其和used相与为0的话，说明该数字没有使用过，我们看如果此时的目标值小于等于当前数字，说明已经赢了，
    # 或者我们调用递归函数，如果返回false，说明也是第一个人赢了。为啥呢，因为当前我们已经选过数字了，
    # 此时就该对第二个人调用递归函数，只有他的结果是false，我们才能赢，所以此时我们标记true，返回true。
    # 如果遍历完所有数字，我们标记false，返回false，参见代码如下：
    def canIwin(self, maxChoosableInteger,desiredTotal):
        total=(maxChoosableInteger+1)*maxChoosableInteger/2
        if total<desiredTotal:
            return False
        if maxChoosableInteger>=desiredTotal:
            return True
        dp=[None for _ in range(1<<maxChoosableInteger)]
        def help(total,choosed):
            if dp[choosed] is not None:
                return dp[choosed]
            for i in range(maxChoosableInteger):
                cur=1<<i
                if choosed&cur==0:
                    if total<=i+1 or not help(total-i-1,choosed|cur):
                        dp[choosed]=True
                        return True
            dp[choosed]=False
            return False
        return help(desiredTotal,0)

print(Solution().canIwin(10,11))

        




