class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        max_result = float('-inf')
        
        # Iterate over all 8 combinations of signs
        for p1 in [1, -1]:
            for p2 in [1, -1]:
                for p3 in [1, -1]:
                    max_val = float('-inf')
                    min_val = float('inf')
                    
                    for i in range(n):
                        value = p1 * arr1[i] + p2 * arr2[i] + p3 * i
                        max_val = max(max_val, value)
                        min_val = min(min_val, value)
                    
                    max_result = max(max_result, max_val - min_val)
        
        return max_result
