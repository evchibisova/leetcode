# https://leetcode.com/problems/reveal-cards-in-increasing-order


class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        if not deck:
            return []
        deck.sort(reverse=True)
        result = [deck[0]]
        for i in deck[1:]:
            result = [i, result[-1]] + result[:-1]
        return result


s = Solution()
print(s.deckRevealedIncreasing([17,13,11,2,3,5,7]))
print(s.deckRevealedIncreasing([2, 1]))