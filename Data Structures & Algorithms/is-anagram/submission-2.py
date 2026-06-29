class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n_s =len(s)
        n_t =len(t)
        if n_s != n_t:
            return False

        chars = set(s)

        for char in chars:
            s_count = s.count(char)
            t_count = t.count(char)
            if s_count != t_count:
                return False
        return True