# 13.10 Team Photo Day -1
# Design an algorithm that takes as input two teams and the heights of the
# players in the teams and checks if it is possible to place players to take
# the photo subject to the placement constraint.

# Hint: First try some concrete inputs, then make a general conclusion.

import collections
from typing import List
class Team:
    Player = collections.namedtuple('Player',('height'))

    def __init__(self,height: List[int]) -> None:
        self._players = [Team.Player(h) for h in height]

    def valid_placement(self,team1:'Team', team2: 'Team')-> bool:
        for p1,p2 in zip(sorted(team1._players),sorted(team2._players)):
            if p1 < p2:
                print(p1,p2)
                return False
        return True


if __name__ =="__main__":
    team1 = Team([70,80,22,33,45,60,30,33,200])
    team2 = Team([69,79,21,22,40,58,29,30,195])

    print(team2.valid_placement(team1,team2))
