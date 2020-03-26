class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        
        negatives = []
        positives = []
        
        for el in A:
            if el < 0:
                negatives.append(el)
            else:
                positives.append(el)
                
        for _ in A:
            if len(negatives) > 0 and len(positives) > 0:
                n = negatives[len(negatives) - 1]
                p = positives[0]

                if (n * n) < (p * p):
                    n = negatives.pop()
                    result.append(n * n)
                else:
                    p = positives.pop(0)
                    result.append(p * p)
            elif len(negatives) > 0:
                n = negatives.pop()
                result.append(n * n)
            else:
                p = positives.pop(0)
                result.append(p * p)
        
        return result
