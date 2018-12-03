from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.ping_list = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.ping_list.append(t)
        while t - 3000 > self.ping_list[0]:
            self.ping_list.popleft()

        return len(self.ping_list)


cntr = RecentCounter()

l = [642, 1849, 4921, 5936, 5957]
for i in l:
    print(cntr.ping(i))