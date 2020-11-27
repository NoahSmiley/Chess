'''
This class stores all info about current state of game.
Also will determine valid moves at the current state of game.
Keeps a Move Log.(undo moves & view previous moves)
'''

class GameState:
    def __init__(self):
        #Board 2x2 nested list - each piece is 2 char, 
        # 1st char being color, 2nd being type. -- rep empty
        self.board = [
            ['bR','bN','bB','bQ','bK','bB','bK','bR'],
            ['bP','bP','bP','bP','bP','bP','bP','bP'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wP','wP','wP','wP','wP','wP','wP','wP'],
            ['wR','wN','wB','wQ','wK','wB','wK','wR'],
        ] 
        self.whiteToMove = True
        self.moveLog = []


