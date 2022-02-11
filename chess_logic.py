from abc import ABC, abstractmethod


class Figure(ABC):  # Abstract Base Class
    def __init__(self, square):
        self.square = square.lower()

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field):
        pass


def check_available_move(axis_x, axis_y, available_moves):
    if (axis_x < 9) and (axis_x > 0) and (axis_y < 9) and (axis_y > 0):
        available_moves.append(f"{chr(axis_x+64)}{axis_y}")


def check_validate_move(dest_field, available_moves):
    if dest_field.upper() in available_moves:
        return "valid"
    else:
        return "invalid"


class King(Figure):
    def list_available_moves(self):
        x = ord(self.square[0]) - 96
        y = int(self.square[1])
        available_moves = []
        if x < 1 or x > 8 or y < 1 or y > 8 or (len(self.square) > 2):
            return available_moves
        else:
            check_available_move(x + 1, y + 1, available_moves)
            check_available_move(x + 1, y, available_moves)
            check_available_move(x + 1, y - 1, available_moves)
            check_available_move(x, y + 1, available_moves)
            check_available_move(x, y - 1, available_moves)
            check_available_move(x - 1, y + 1, available_moves)
            check_available_move(x - 1, y, available_moves)
            check_available_move(x - 1, y - 1, available_moves)
            return available_moves

    def validate_move(self, dest_field):
        return check_validate_move(dest_field, self.list_available_moves)


class Queen(Figure):
    def list_available_moves(self):
        x = ord(self.square[0]) - 96
        y = int(self.square[1])
        available_moves = []
        if x < 1 or x > 8 or y < 1 or y > 8 or (len(self.square) > 2):
            return available_moves
        else:
            for i in range(1, 8):
                check_available_move((x + i), (y + i), available_moves)
                check_available_move((x - i), (y + i), available_moves)
                check_available_move((x + i), (y - i), available_moves)
                check_available_move((x - i), (y - i), available_moves)
                check_available_move((x + i), y, available_moves)
                check_available_move((x - i), y, available_moves)
                check_available_move(x, (y + i), available_moves)
                check_available_move(x, (y - i), available_moves)
            return available_moves

    def validate_move(self, dest_field):
        return check_validate_move(dest_field, self.list_available_moves())


class Rook(Figure):
    def list_available_moves(self):
        x = ord(self.square[0]) - 96
        y = int(self.square[1])
        available_moves = []
        if x < 1 or x > 8 or y < 1 or y > 8 or (len(self.square) > 2):
            return available_moves
        else:
            for i in range(1, 8):
                check_available_move((x + i), y, available_moves)
                check_available_move((x - i), y, available_moves)
                check_available_move(x, (y + i), available_moves)
                check_available_move(x, (y - i), available_moves)
            return available_moves

    def validate_move(self, dest_field):
        return check_validate_move(dest_field, self.list_available_moves())


class Bishop(Figure):
    def list_available_moves(self):
        x = ord(self.square[0]) - 96
        y = int(self.square[1])
        available_moves = []
        if x < 1 or x > 8 or y < 1 or y > 8 or (len(self.square) > 2):
            return available_moves
        else:
            for i in range(1, 8):
                check_available_move((x + i), (y + i), available_moves)
                check_available_move((x - i), (y + i), available_moves)
                check_available_move((x + i), (y - i), available_moves)
                check_available_move((x - i), (y - i), available_moves)
            return available_moves

    def validate_move(self, dest_field):
        return check_validate_move(dest_field, self.list_available_moves())


class Knight(Figure):
    def list_available_moves(self):
        x = ord(self.square[0]) - 96
        y = int(self.square[1])
        available_moves = []
        if x < 1 or x > 8 or y < 1 or y > 8 or (len(self.square) > 2):
            return available_moves
        else:
            check_available_move((x + 2), (y + 1), available_moves)
            check_available_move((x + 2), (y - 1), available_moves)
            check_available_move((x + 1), (y + 2), available_moves)
            check_available_move((x + 1), (y - 2), available_moves)
            check_available_move((x - 2), (y + 1), available_moves)
            check_available_move((x - 2), (y - 1), available_moves)
            check_available_move((x - 1), (y + 2), available_moves)
            check_available_move((x - 1), (y - 2), available_moves)
            return available_moves

    def validate_move(self, dest_field):
        return check_validate_move(dest_field, self.list_available_moves())


class Pawn(Figure):
    def list_available_moves(self):
        x = ord(self.square[0]) - 96
        y = int(self.square[1])
        available_moves = []
        if x < 1 or x > 8 or y < 1 or y > 8 or (len(self.square) > 2):
            return available_moves
        else:
            check_available_move(x, (y + 1), available_moves)
            if y == 2:
                available_moves.append(f"{chr(x+96)}{y+2}")
            return available_moves

    def validate_move(self, dest_field):
        return check_validate_move(dest_field, self.list_available_moves())
