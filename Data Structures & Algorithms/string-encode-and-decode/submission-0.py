class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for s in strs:
            encoded+=f"{len(s)}#{s}"
        return encoded    


    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        n = len(s)

        while i < n:
            length = 0

            # Extract the length
            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i += 1

            i += 1  # skip '#'

            # Extract the actual string using the length
            temp = s[i:i + length]
            result.append(temp)

            i += length

        return result

