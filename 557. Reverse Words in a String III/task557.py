class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split(" ")
        word_list = [i[::-1] for i in word_list]
        return " ".join(word_list)
