class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick exit: anagrams must have identical lengths
        if len(s) != len(t):
            return False

        # Fixed-size frequency table for 26 lowercase English letters
        counts = [0] * 26

        # Increment for s, decrement for t in a single pass
        for char_s, char_t in zip(s, t):
            counts[ord(char_s) - 97] += 1
            counts[ord(char_t) - 97] -= 1

        # If any frequency is non-zero, they are not anagrams
        return all(c == 0 for c in counts)