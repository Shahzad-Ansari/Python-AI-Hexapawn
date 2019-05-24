class HexaPawnNode:
    def __init__(self,board, parent_node=None , move = None):
        self.board = board
        self.parent = parent_node
        self.move = move
        setPuzzle(board)

    children_list = ()
    x = 0
    col = 3
    row = 3
    depth = None
    heuristic = None
    Fcost = None

    def setPuzzle(self , current_board ):
        for board in current_board:
            self.board_state = current_board

    def goalTest(self):
        for




