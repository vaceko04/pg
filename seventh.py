from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position
       
    @staticmethod
    def is_position_on_board(position):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if self.is_position_on_board(new_position):
            self.__position = new_position
        else:
            raise ValueError("Position is outside the chessboard")

    @abstractmethod
    def possible_moves(self):
        pass

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        x, y = self.position
        moves = []

        if self.color == "white":
            new_position = (x, y + 1)
        else:
            new_position = (x, y - 1)

        if self.is_position_on_board(new_position):
            moves.append(new_position)

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'

class Knight(Piece):
    def possible_moves(self):
        x, y = self.position
        moves = []

        possible_positions = [
            (x + 1, y + 2),
            (x + 1, y - 2),
            (x - 1, y + 2),
            (x - 1, y - 2),
            (x + 2, y + 1),
            (x + 2, y - 1),
            (x - 2, y + 1),
            (x - 2, y - 1)
        ]

        for position in possible_positions:
            if self.is_position_on_board(position):
                moves.append(position)

        return moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'

class Bishop(Piece):
    def possible_moves(self):
        x, y = self.position
        moves = []

        new_x = x + 1
        new_y = y + 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x += 1
            new_y += 1

        new_x = x - 1
        new_y = y + 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x -= 1
            new_y += 1

        new_x = x + 1
        new_y = y - 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x += 1
            new_y -= 1

        new_x = x - 1
        new_y = y - 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x -= 1
            new_y -= 1

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'

class Rook(Piece):
    def possible_moves(self):
        x, y = self.position
        moves = []

        new_x = x + 1
        while self.is_position_on_board((new_x, y)):
            moves.append((new_x, y))
            new_x += 1

        new_x = x - 1
        while self.is_position_on_board((new_x, y)):
            moves.append((new_x, y))
            new_x -= 1

        new_y = y + 1
        while self.is_position_on_board((x, new_y)):
            moves.append((x, new_y))
            new_y += 1

        new_y = y - 1
        while self.is_position_on_board((x, new_y)):
            moves.append((x, new_y))
            new_y -= 1

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'

class Queen(Piece):
    def possible_moves(self):
        x, y = self.position
        moves = []

        new_x = x + 1
        while self.is_position_on_board((new_x, y)):
            moves.append((new_x, y))
            new_x += 1

        new_x = x - 1
        while self.is_position_on_board((new_x, y)):
            moves.append((new_x, y))
            new_x -= 1

        new_y = y + 1
        while self.is_position_on_board((x, new_y)):
            moves.append((x, new_y))
            new_y += 1

        new_y = y - 1
        while self.is_position_on_board((x, new_y)):
            moves.append((x, new_y))
            new_y -= 1

        new_x = x + 1
        new_y = y + 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x += 1
            new_y += 1

        new_x = x - 1
        new_y = y + 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x -= 1
            new_y += 1

        new_x = x + 1
        new_y = y - 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x += 1
            new_y -= 1

        new_x = x - 1
        new_y = y - 1
        while self.is_position_on_board((new_x, new_y)):
            moves.append((new_x, new_y))
            new_x -= 1
            new_y -= 1

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'

class King(Piece):
    def possible_moves(self):
        x, y = self.position
        moves = []

        possible_positions = [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1)
        ]

        for position in possible_positions:
            if self.is_position_on_board(position):
                moves.append(position)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'

if __name__ == "__main__":
    figurka = Knight("white", (1, 0))


    print(figurka)
    print("Possible moves:", figurka.possible_moves())