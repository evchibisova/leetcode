class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        result = []

        for word in words:
            for row in keyboard:
                if all(char.lower() in row for char in word):
                    result.append(word)
                    break

        return result
