class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        cpdomains_dict = dict()
        for i in cpdomains:
            val, key = i.split(" ")
            while key:
                if key not in cpdomains_dict:
                    cpdomains_dict[key] = 0
                cpdomains_dict[key] += int(val)
                if "." in key:
                    key = key[key.find(".") + 1:]
                else:
                    key = ""
        all_cpdomains = ["{} {}".format(val, key) for (key, val) in cpdomains_dict.items()]

        return all_cpdomains
