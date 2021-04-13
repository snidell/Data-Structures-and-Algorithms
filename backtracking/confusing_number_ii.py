class Solution:
    def __init__(self):
        self.count = 0

    def confusingNumberII(self, N: int) -> int:
        rotations = {1:1, 6:9, 8:8, 9:6, 0:0}
        valid = [0, 1, 6, 8, 9]

        def backtrack(num, rotation, position):
            if num > N:
                return

            if num != rotation:
                self.count += 1

            for digit in valid:
                backtrack(num * 10 + digit, rotations[digit] * position + rotation, position * 10)


        for digit in valid[1:]:
            backtrack(digit, rotations[digit], 10)
        return self.count


if __name__ =="__main__":
    mySolution = Solution()
    N = 100
    print(mySolution.confusingNumberII(100))
