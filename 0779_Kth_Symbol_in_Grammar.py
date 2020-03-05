class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0

        if K % 2 != 0:
            prev_K = (K + 1) / 2
            sub_prob = self.kthGrammar(N - 1, prev_K)

            if sub_prob == 0:
                return 0
            else:
                return 1

        else:
            prev_K = K / 2
            sub_prob = self.kthGrammar(N - 1, prev_K)

            if sub_prob == 0:
                return 1
            else:
                return 0
