class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        # stack = []
        # for i, t in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < t:
        #         prev = stack.pop()
        #         res[prev] = i - prev
        #     stack.append(i)
        # return res

        for i, t in enumerate(temperatures):
            j = i + 1

            while j < n:
                if temperatures[j] > temperatures[i]:
                    res[i] = j - i
                    break
                j += 1
        return res 
        