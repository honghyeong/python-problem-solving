#78

# path, recursive, start index from itself.

from typing import *
import itertools

class Solution:
    def subsets(self,nums):
        result = []

        def dfs(start, path):

            result.append(path)

            if start >= len(nums):
                return

            for i in range(start, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result
