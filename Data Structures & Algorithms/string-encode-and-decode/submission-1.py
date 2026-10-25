class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("|")
            result.append(s)
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            length, remaining = s.split("|", maxsplit=1)
            length = int(length)
            found_str = remaining[:length]
            result.append(found_str)
            s = remaining[length:]
        return result
