# 16.1 COUNT THE NUMBER OF SCORE COMBINATIONS

# In an American football game, a play can lead to 2 points (safety), 3 points
# (field goal), or 7 points (touchdown, assuming the extra point). Many different
# combinations of 2, 3, and 7 point plays can make up a final score. For example,
# four combinations of plays yield a score of 12:

# • 6safeties(2x6=12),
# • 3safeties and 2 field goals(2X3+3x2=12),
# • 1safety,1 field goal and 1 touchdown(2x1+3x1+7x1=12),and
# • 4 field goals(3x4=12).

# Write a program that takes a final score and scores for individual plays, and
# returns the number of combinations of plays that result in the final score.
#
# Hint: Count the number of combinations in which there are 0 w0 plays, then 1
# w0 plays, etc.

from typing import List

class Solution:
    def num_combinations_for_final_score(self,final_score: int,
                                    individual_play_scores: List[int]) ->int:
        # One way to reach Zero
        # make arrays of final scores long and rows of indivdual scores tall
        num_combinations_for_score = [[1] + [0] * final_score for _ in individual_play_scores]
        print(num_combinations_for_score)
        for i in range(len(individual_play_scores)):
            for j in range(1, final_score+1):
                # look above you for the without score
                without_this_play = (num_combinations_for_score[i-1][j]
                                     if i >= 1 else 0)
                print("index: row,col: ",i-1,j,num_combinations_for_score[i-1][j]," without: ",without_this_play)
                with_this_play = (
                    # with this score can i reach this index with another combination ?
                    num_combinations_for_score[i][j - individual_play_scores[i]]
                    if j>= individual_play_scores[i] else 0)


                num_combinations_for_score[i][j] = (without_this_play + with_this_play)
        print(num_combinations_for_score)
        return num_combinations_for_score[-1][-1]




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.num_combinations_for_final_score(12,[2,3,7]))
    #    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12
    # 2 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    # 3 [1, 0, 1, 1, 1, 1, 2, 1, 2, 2, 2, 2, 3],
    # 4 [1, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]]

    given i = 2 and j=12 look up and look back the current value
    look up [i-]1[j] = 3, look by 7 [i][j-individual_play_scores[i]] == [i][j-7] ==> [2][5]==> 1
