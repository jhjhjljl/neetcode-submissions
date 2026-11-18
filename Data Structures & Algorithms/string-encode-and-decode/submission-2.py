class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for x in strs:
            result.extend([str(len(x)), "|", x])
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        while s:
            length, remaining = s.split("|", 1)
            length = int(length)
            result.append(remaining[:length])
            s = remaining[length:]
        return result

