from typing import List


class Codec:
    # Time: o(n*k)=~ o(n), If n is the number of strings and k is the average length of the strings
    # Space: o(n*k)=~ o(n), If n is the number of strings and k is the average length of the strings
    def encode(self, strs: List[str]) -> str:
        # Encoding each string by prefixing with length followed by '#'..like 5#Hello
        encode_str = ""
        for s in strs:
            encode_str += str(len(s)) + "#" + s
        return encode_str

    def decode(self, s: str) -> List[str]:
        '''5#Hello5#World7#sh#reya'''
        # Decoding the encoded string back to list of strings
        decode_str = []
        i = 0
        while i < len(s):
            # Find the next '#' to determine where the length ends
            j = i
            while s[j] != '#':
                j += 1
            # Extract the length of the next substring
            length = int(s[i:j])

            extractedString = s[j + 1:j + 1 + length]  # Extract the substring based on the extracted length
            decode_str.append(extractedString)
            i = j + 1 + length  # Move the index `i` to the start of the next encoded part

        return decode_str


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))