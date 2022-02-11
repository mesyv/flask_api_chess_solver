import chess_logic

class Test:
    def can_the_queen_move_from_h2_to_g3(self):
        figure = getattr(chess_logic, "Queen")("h2")
        result = figure.validate_move("g3")
        assert result == "valid"