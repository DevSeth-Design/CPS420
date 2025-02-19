from model.square import Square

_squares = [

]

def get_all() -> list[Square]:
    """Return all explorers"""
    return _squares

def get_one(length: float, width: float) -> Square | None:
    for square in _squares:
        if square.Length == length and square.Width == width:
            print(f"DBUG: {square}")
            return square
    return None

def create(square: Square) -> Square:
    """Add a square"""
    print(f"DEBUG: Creating square {square}")  # Debugging
    _squares.append(square)
    print(f"DEBUG: _squares now contains: {_squares}")  # Debugging
    return square


def modify(index: int, square: Square) -> Square | None:
    """Modify a square at a given index"""
    if 0 <= index < len(_squares):
        _squares[index] = square
        return square
    return None

def replace(index: int, square: Square) -> Square | None:
    """Replace a square at a given index"""
    if 0 <= index < len(_squares):
        _squares[index] = square
        return square
    return None

def delete(length: float, width: float) -> bool:
    """Delete a square by its length and width"""
    global _squares
    _squares = [square for square in _squares if not (square.Length == length and square.Width == width)]
    return True
def get_area(length: float, width: float) -> float:
    """Get the area of a square"""
    square = get_one(length, width)
    if square:
        return square.area()
    return 0  

def get_circumference(length: float, width: float) -> float:
    """Get the circumference of a square"""
    square = get_one(length, width)
    if square:
        return square.circumference()
    return 0  
