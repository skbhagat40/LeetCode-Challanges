"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.b = board
        self.visited = [[False]*len(board[0]) for _ in range(len(board))]
        self.ans = None
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0]:
                    self.visited[row][col] = True
                    self.search(row, col, word, 1)
                    if self.ans:
                        return True
                    else:
                        self.visited = [[False]*len(board[0]) for _ in range(len(board))]
        
    def search(self, i,j, word, idx):
        if self.ans == True:
            return             # optimization for avoiding TLE
        if idx == len(word):
            self.ans = True
            return True
        for child in self.getChildren(i,j):
            if not self.visited[child[0]][child[1]] and word[idx] == self.b[child[0]][child[1]]:
                self.visited[child[0]][child[1]] = True
                res = self.search(child[0], child[1], word, idx + 1)
                if not res:
                    self.visited[child[0]][child[1]] = False # reset the state if alternative path fails. IMP!!
                    
    def getChildren(self,i,j):
        res = []
        if i + 1 < len(self.b):
            res.append([i+1, j])
        if i-1 >=0:
            res.append([i-1, j])
        if j + 1 < len(self.b[0]):
            res.append([i, j+1])
        if j - 1 >= 0:
            res.append([i,j-1])
        return res
  """
  Approach - use backtracking.
  """
