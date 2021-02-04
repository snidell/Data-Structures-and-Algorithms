# 13.9 PARTITIONING AND SORTING AN ARRAY WITH MANY REPEATED ENTRIES

import collections
from typing import List
Person = collections.namedtuple('Person',('age','name'))

class Solution:
    # time complexity is O(n)
    # space is O(m) where m is the number if distinct ages
    def group_by_age(self,people: List[Person])-> None:
        age_count = collections.Counter((person.age for person in people))
        age_offset, offset = {}, 0
        for age, count in age_count.items():
            age_offset[age] = offset
            offset += count
        print(age_offset)

        while age_offset:
            from_age = next(iter(age_offset))
            from_idx = age_offset[from_age]

            to_age = people[from_idx].age
            to_idx = age_offset[people[from_idx].age]
            print("form age: ",from_age," from_idx: ",from_idx,"---> to age: ",to_age," to_idx: ",to_idx)

            people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
            print(people)
            # Use age_count to see when we are done with a particular age
            age_count[to_age] -= 1

            if age_count[to_age]:
                age_offset[to_age] = to_idx+1
            else:
                del age_offset[to_age]


if __name__=="__main__":
    mySolution = Solution()
    p1 = Person(14,"Greg")
    p2 = Person(12,"John")
    p3 = Person(11,"Andy")
    p4 = Person(13,"Jim")
    p5 = Person(12,"Phil")
    p6 = Person(13,"Bob")
    p7 = Person(13,"Chip")
    p8 = Person(14,"Tim")
    people = [p1,p8,p2,p3,p4,p5,p6,p7   ]
    mySolution.group_by_age(people)
    print(people)
