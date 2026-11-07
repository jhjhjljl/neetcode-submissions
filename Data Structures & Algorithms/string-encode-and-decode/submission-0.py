"""
["hello", "world", "nice", "people"]

5|hello5|world4|nice6|people

5     hello5|world4|nice6|people
num       remaining_str
"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = []
        for x in strs:
            new_str.append(str(len(x)))
            new_str.append("|")
            new_str.append(x)
        return "".join(new_str)

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        while s:
            n, remaining_str = s.split("|", 1)
            n = int(n)
            decoded_strs.append(remaining_str[:n])
            s = remaining_str[n:]
        return decoded_strs


