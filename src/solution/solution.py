class Solution:
    def can_transform(self, starting_board: str, ending_board: str) -> bool:
        if starting_board.count('R') != ending_board.count('R') \
            or starting_board.count('L') != ending_board.count('L') \
            or starting_board.replace('_', '') != ending_board.replace('_', ''):
            return False

        start_L = [i for i in range(len(starting_board)) if starting_board[i] == 'L']
        end_L = [i for i in range(len(ending_board)) if ending_board[i] == 'L']
        for i in range(len(start_L)):
            if start_L[i] < end_L[i]:
                return False

        start_R = [i for i in range(len(starting_board)) if starting_board[i] == 'R']
        end_R = [i for i in range(len(ending_board)) if ending_board[i] == 'R']
        for i in range(len(start_R)):
            if start_R[i] > end_R[i]:
                return False
        
        return True