class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        carry = '0'

        while a_idx >= 0 or b_idx >= 0:
            if a_idx >= 0 and b_idx >= 0:
                carry, total = self.add([a[a_idx], b[b_idx], carry])
                a_idx -= 1
                b_idx -= 1
            elif a_idx >= 0:
                carry, total = self.add([a[a_idx], carry])
                a_idx -= 1
            elif b_idx >= 0:
                carry, total = self.add([b[b_idx], carry])
                b_idx -= 1

            result.append(total)

        if carry == '1':
            result.append(carry)

        result.reverse()
        return "".join(result)

    def add(self, arr: List[str]) -> (str, str):
        num_1 = 0
        for el in arr:
            if el == '1':
                num_1 += 1

        if num_1 == 3:
            return ('1', '1')
        elif num_1 == 2:
            return ('1', '0')
        elif num_1 == 1:
            return ('0', '1')
        else:
            return ('0', '0')
