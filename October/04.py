# https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3483/
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        removed = set()
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i==j:
                    continue
                # if tuple(i) not in removed an
                c_i = intervals[i]
                n_i = intervals[j]
                if tuple(c_i) in removed:
                    continue
                if c_i[0] >= n_i[0] and c_i[1] <= n_i[1]:
                    count += 1
                    removed.add(tuple(c_i))
        return len(intervals) - count
