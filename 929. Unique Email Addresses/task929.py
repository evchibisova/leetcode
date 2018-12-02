class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        target_list = set()

        for i in emails:
            local, domain = i.split("@")
            plus_position = i.find("+")
            if plus_position != -1:
                local = i[:plus_position]
            local = local.replace(".", "")
            target_list.add((local, domain))

        return len(target_list)

# s = Solution()
# print(s.numUniqueEmails(["test.email+alex@leetcode.com",
#                          "test.e.mail+bob.cathy@leetcode.com",
#                          "testemail+david@lee.tcode.com"]))