from model.square import Square

_squares = [
    Square(Length=1, Width=1),
    Square(Length=2, Width=2),
    Square(Length=3, Width=3),
]

# def get_all() -> list[Square]:
#     """Return all explorers"""
#     return _squares

# def get_one(length: float, width: float) -> Square | None:
#     for square in _squares:
#         if square.Length == length and square.Width == width:
#             return square
#     return None

# def create(square: Square) -> Square:
#     """Add a square"""
#     _squares.append(square)
#     return square

# def modify(index: int, square: Square) -> Square | None:
#     """Modify a square at a given index"""
#     if 0 <= index < len(_squares):
#         _squares[index] = square
#         return square
#     return None

# def replace(index: int, square: Square) -> Square | None:
#     """Replace a square at a given index"""
#     if 0 <= index < len(_squares):
#         _squares[index] = square
#         return square
#     return None

# def delete(length: float, width: float) -> bool:
#     """Delete a square by its length and width"""
#     global _squares
#     _squares = [square for square in _squares if not (square.Length == length and square.Width == width)]
#     return True
# moved this to the model to apease the assignment instructions
# def area(length: float, width: float) -> float:
#     """Calculate the area of a square"""
#     return length * width
# def circumference(length: float, width: float) -> float:
#     """Calculate the circumference of a square"""
#     return 2 * (length + width)