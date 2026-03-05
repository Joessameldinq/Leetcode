class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        solution = []
        candidates.sort()
        def backtrack(target,cur,start):
            if target == 0:
                solution.append(cur)
                return
            for i in range(start,len(candidates)):
                if target - candidates[i] < 0:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                backtrack(target-candidates[i],cur + [candidates[i]],i+1)

        backtrack(target,[],0)
        return solution
