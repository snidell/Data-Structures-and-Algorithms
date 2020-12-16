
from typing import List
class Solution:
    # works only on Square matrices
    def matrix_in_spiral_order(self,square_matrix: [[int]]) -> [int]:
        def matrix_layer_in_clockwise(offset):
            if offset == len(square_matrix) - offset - 1:
                spiral_ordering.append(square_matrix[offset][offset])
                return
            spiral_ordering.extend(square_matrix[offset][offset:-1 - offset])
            spiral_ordering.extend(
                list(zip(*square_matrix))[-1 - offset][offset:-1 - offset])
            spiral_ordering.extend(square_matrix[-1 - offset] [-1 -offset:offset:-1])
            spiral_ordering.extend(list(zip(*square_matrix))[offset][-1-offset:offset:-1])

        spiral_ordering: [int] = []
        for offset in range((len(square_matrix) + 1) // 2):
            matrix_layer_in_clockwise(offset)

        return spiral_ordering
    # Leetcode Solution works on non-square matrices
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
    # Leetcode O(n) time O(1) space
    def spiralOrderOptimized(self, matrix):
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                ans.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		# iteration variable
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        direction = 0
        result = []

        while left <= right and top <= bottom:
            if direction % 4 == 0:
                #left to right
                for i in range(left, right + 1):
                    result.append(matrix[top][i])
                top += 1
            elif direction % 4 == 1:
                # top to bottom
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
            elif direction % 4 == 2:
                # right to left
                for i in reversed(range(left, right + 1)):
                    result.append(matrix[bottom][i])
                bottom -= 1
            else:
                # bottom to top
                for i in reversed(range(top, bottom + 1)):
                    result.append(matrix[i][left])
                left += 1
            direction += 1

        return result


if __name__ == "__main__":
    mySolution = Solution()
    A = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(mySolution.matrix_in_spiral_order(A))
    print(mySolution.spiralOrder(A))
    print(mySolution.spiralOrderOptimized(A))
    print(mySolution.spiralOrder(A))
