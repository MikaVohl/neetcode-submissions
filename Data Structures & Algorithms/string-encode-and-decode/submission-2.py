class Solution:

    def encode(self, strs: List[str]) -> str:
        # out = ""
        # for s in strs:
        #     out += chr(len(s)) + s
        # return out
        return "".join(chr(len(s)) + s for s in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        string = ""
        if len(s) == 0: return []
        remaining = ord(s[0])
        for c in s[1:]:
            if remaining == 0:
                remaining = ord(c)
                output.append(string)
                string = ""
                continue
            string += c
            remaining -= 1
        output.append(string)
        return output

                