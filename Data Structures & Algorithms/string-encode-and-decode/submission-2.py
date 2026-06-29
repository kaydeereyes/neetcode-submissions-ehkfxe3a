class Solution:

    def encode(self, strs: List[str]) -> str:
        string = str()

        for word in strs:
            string += word + '\x00'
        print(string)
        return string
    def decode(self, s: str) -> List[str]:
        decoded = s.split("\x00")
        return decoded[:-1]
