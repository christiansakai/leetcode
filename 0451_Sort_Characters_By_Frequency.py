class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1

        tuples = []
        for ch in dic:
            tuples.append((ch, dic[ch]))

        tuples.sort(key=lambda tpl: tpl[1], reverse=True)

        string = []
        for tpl in tuples:
            for i in range(0, tpl[1]):
                string.append(tpl[0])

        return ''.join(string)
