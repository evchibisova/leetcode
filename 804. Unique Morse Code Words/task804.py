class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                       "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        diff_words = set()
        for word in words:
            morse_word = "".join([morse_list[ord(i)-97] for i in word])
            diff_words.add(morse_word)
        return(len(diff_words))
