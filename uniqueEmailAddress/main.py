from typing import List
from typing import Set

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mySet = set()
        for i in range(len(emails)):
            mySet.add(self.transformPeriod(self.transformPlus(emails[i])))
        return len(mySet)

    def transformPeriod(self,email: str)-> str:
        emailParts = email.split("@")
        return emailParts[0].replace(".","")+"@"+emailParts[1]

    def transformPlus(self,email: str)->str:
        emailParts = email.split("@")
        firstPlus = emailParts[0].find("+")
        if firstPlus >=0:
            return emailParts[0][0:firstPlus]+"@"+emailParts[1]
        else:
            return email



if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    emails2 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    s = Solution()
    print(s.numUniqueEmails(emails))
