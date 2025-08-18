class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Cleaner Solution:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".": 
                    continue
                b = (r // 3) * 3 + (c // 3)
                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False
                rows[r].add(v); cols[c].add(v); boxes[b].add(v)
        return True


        # Original Solution:

        # # check rows
        # for r in range(9):
        #     seen = set()
        #     for c in range(9):
        #         cell = board[r][c]
        #         if cell == ".": continue
        #         if cell in seen: return False
        #         seen.add(cell)

        # # check columns
        # for c in range(9):
        #     seen = set()
        #     for r in range(9):
        #         cell = board[r][c]
        #         if cell == ".": continue
        #         if cell in seen: return False
        #         seen.add(cell)

        # # check boxes
        # for br in range(0, 9, 3):
        #     for bc in range(0, 9, 3):
        #         seen = set()
        #         for r in range(br, br + 3):
        #             for c in range(bc, bc + 3):
        #                 cell = board[r][c]
        #                 if cell == ".": continue
        #                 if cell in seen: return False
        #                 seen.add(cell)

        # return True

