"""
Island Perimetre

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.ans = 0
        self.g = grid
        self.visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.traverse(i,j)
                    break
        return self.ans
    
    def traverse(self, i,j):
        if not self.visited[i][j]:
            self.visited[i][j] = True
            nbrs = []
            if j + 1 < len(self.g[0]):
                if self.g[i][j+1] == 1:
                    nbrs.append([i, j+1])
            if j - 1 >= 0:
                if self.g[i][j-1] == 1:
                    nbrs.append([i, j-1])
            if i + 1 < len(self.g):
                if self.g[i+1][j] == 1:
                    nbrs.append([i+1, j])
            if i - 1 >= 0:
                if self.g[i-1][j] == 1:
                    nbrs.append([i-1, j])
            self.ans += 4 - len(nbrs)
            for n in nbrs:
                self.traverse(*n)
 """
 Solution Approach:
 since there is only one island, find a first one and traverse it recursively.
 keep track of nodes which are visited.
 contribution of a node = 4 - (no. of neighbours it has).
 somewhat similar to dfs traversal
 """
