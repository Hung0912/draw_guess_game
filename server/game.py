from .player import Player
from .round import Round
from .board import Board

class Game(object):

    def __init__(self, id, players):
        self.id = id
        self.players = players
        self.words_used = []
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0
        self.connected_thread = thread
        self.start_new_round()

    def start_new_round(self):
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= lend(self.players):
            self.end_round()
            self.end_game()

    def player_guess(self, player, guess):
        return self.round.guess(player, guess)
    
    def player_disconnected(self, player):
        pass
    
    def skip(self):
        
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet!")

    def round_ended(self):
        self.round.skips = 0
        self.start_new_round()
        self.board.clear()
        pass
    
    def update_board(self, x, y, color):

        if not self.board:
            raise Exception("No board created!")
        self.board.update(x,y,color)
    
    def end_game(self):
        pass
    
    def get_word(self):
        # todo get a list of word from swh
        pass
        