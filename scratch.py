from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]    # parent to hold indexes of each item in accounts array, we know we cannot use names and instead use indexes to uniquely identify parents
        size = [1] * (len(accounts) + 1)  # We do union by size

        def union(n1, n2):
            nonlocal parent, size
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if size[p1] > size[p2]:
                parent[p2] = p1
                size[p1] += size[p2]
            else:
                parent[p1] = p2
                size[p2] += size[p1]
            return True

        def find(n):
            nonlocal parent
            p = n
            if parent[p] == p:
                return p
            else:
                parent[p] = find(parent[p])
                return parent[p]

        # Logic
        emailToIndex = {}  # we cannot map to names, as different person can have same name, the unique identifier is the index
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToIndex:  # different index same email, union them
                    union(i, emailToIndex[email])  # unioning 2 indexes as they belong to same person. Union would modify the parent of email of same person which was found 2nd/ later time. We later do a find operation to check parents and whatever belongs to same parents (index) are grouped together
                else:
                    emailToIndex[email] = i
        
        groupedEmails = defaultdict(list)
        for email, idx in emailToIndex.items():
            parent_idx = find(idx)
            groupedEmails[parent_idx].append(email)
        
        # convert index back to name
        res = []
        for idx, emails in groupedEmails.items():
            name = accounts[idx][0]
            ans = [name] + sorted(emails)
            res.append(ans)

        return res
    
print(Solution().accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
                                           ["John","johnsmith@mail.com","john00@mail.com"],
                                           ["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))