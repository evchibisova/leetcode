class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S or not widths:
            return None

        last_string_len, string_count = 0, 1
        for i in S:
            new_letter = widths[ord(i) - ord("a")]
            if last_string_len + new_letter > 100:
                string_count += 1
                last_string_len = new_letter
            else:
                last_string_len += new_letter
        return [string_count, last_string_len]
