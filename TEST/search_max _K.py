# -*- coding: utf-8 -*-
__author__ = 'Guanshanyou'
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        listnum = []
        for i in nums:
            listnum.append(i)
        listnum.sort()
        return listnum[-n]

if __name__ =='__main__':
    sou = Solution()
    print(sou.kthLargestElement(1, [1, 4, 3, 5, 6, 8]))
