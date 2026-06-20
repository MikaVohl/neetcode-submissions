class Solution:

    def encode(self, strs: List[str]) -> str:
        # out = ""
        # for s in strs:
        #     out += chr(len(s)) + s
        # return out
        return "".join(chr(len(s)) + s for s in strs)

    def decode(self, s: str) -> List[str]:
        out = []
        i, n = 0, len(s)
        while i < n:
            length = ord(s[i])
            i += 1
            out.append(s[i:i + length])
            i += length
        return out

                