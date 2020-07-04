"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
"""




class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        temp = cells[:]
        t = [0]*len(temp)
        if N > 14:
            N = N % 14 + 14
        for idx in range(N):
            if idx != 0:
                temp = t[:]
            for i in range(1,len(temp)-1):
                if (temp[i-1] == 0 and temp[i+1] == 0) or (temp[i-1] == 1 and temp[i+1] == 1):
                    t[i] = 1
                    # print('t', t)
                else:
                    t[i] = 0
        return t
