class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the position of the '#' character
            while s[j] != '#':
                j += 1

            # Extract the length of the next string
            length = int(s[i:j])
            # Extract the actual string of that length
            extrc = s[j + 1:j + 1 + length]
            res.append(extrc)
            # Move `i` to the start of the next encoded string
            i = j + 1 + length
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
