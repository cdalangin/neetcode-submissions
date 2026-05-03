class Solution:

    def encode(self, strs: List[str]) -> str:
        enStr = ""
        for i in strs:
            enStr += str(len(i)) + "#" + i
        return enStr

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            currNum = int(s[i:j])

            startDigit = j+1
            endDigit = startDigit+currNum

            orgStr = s[startDigit:endDigit]
            strs.append(orgStr)
            i = endDigit
        return strs