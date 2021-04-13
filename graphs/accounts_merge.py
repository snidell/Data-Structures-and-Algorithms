# # Leetcode 721 Accounts Merge
# Given a list of accounts where each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name, and the rest of the elements
# are emails representing emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to
# the same person if there is some common email to both accounts. Note that even
# if two accounts have the same name, they may belong to different people as
# people could have the same name. A person can have any number of accounts
# initially, but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order. The accounts themselves can be returned in any order.

import collections

class Solution:
    # time complexity is O(nlog(n)) nlog(n) for sorting at the end and n for looping through the accounts to load the DS
    #  space is O(n) as we store bot a visited, email to name and graph
    def accoutnsMerge(self,accounts):
        # first we need a linkage between the email and the account names
        email_to_name = {}
        # then we need to construct the graph between emails
        graph = collections.defaultdict(set)

        # now we need to populate the above structures
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_to_name[email] = name

        # now our data is orgainzed its time to search via DFS
        visited = set()
        ans = []

        for email in graph:
            if email not in visited:
                visited.add(email)
                name = email_to_name[email]
                # will hold sorted emails
                components =[]
                stack = [email]
                while stack:
                    item = stack.pop()
                    components.append(item)
                    for subEmail in graph[item]:
                        if subEmail not in visited:
                            visited.add(subEmail)
                            stack.append(subEmail)
                print("name:", name," components",sorted(components))
                ans.append([[name]+sorted(components)])
        return ans




if __name__ =="__main__":
    mySolution = Solution()
    accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    print(mySolution.accoutnsMerge(accounts))
