class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            start = str(i)
            if i >= 10:
                break
            while int(start) <= high:
                if start[-1] == '9':
                    break
                start = start + str(int(str(start)[-1]) + 1)
                if int(start) >= low and int(start) <= high:
                    ans.append(int(start))
        return sorted(ans)
