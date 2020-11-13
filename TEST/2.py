# -*- coding: utf-8 -*-
__author__ = 'Guanshanyou'


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        listnum = [1]
        for i in range(n):
            for j in (2,3,5):
                if listnum[i]*j in listnum:
                    pass
                else:
                    listnum.append(listnum[i]*j)
                    listnum =list(set(listnum))
                    listnum.sort()
        print(listnum[n-1])
        print(listnum)
sou = Solution ()
sou.nthUglyNumber(1)



