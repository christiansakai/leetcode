class Solution:
    num_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        result = []
        letters = []

        self.recurse(digits, 0, letters, result)
        return result

    def recurse(
            self,
            digits: str,
            index: int,
            letters: List[str],
            result: List[str]):
        if index == len(digits):
            string = "".join(letters)
            result.append(string)
            return

        digit = digits[index]
        for letter in self.num_letters[digit]:
            letters.append(letter)
            self.recurse(digits, index + 1, letters, result)
            letters.pop()
