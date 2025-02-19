from fastapi import APIRouter
from model.square import Square
import service.square as service

router = APIRouter(prefix="/squares")  # Changed prefix to plural for better convention

@router.get("/")
def get_all() -> list[Square]:
    """Retrieve all squares"""
    return service.get_all()

@router.get("/{length}/{width}")
def get_one(length: float, width: float) -> Square | None:
    """Retrieve a specific square by length and width"""
    return service.get_one(length, width)

@router.get("/{length}/{width}/area")
def get_area(length: float, width: float) -> float | None:
    """Retrieve the area of a specific square"""
    return service.get_area(length, width)

@router.get("/{length}/{width}/circumference")
def get_circumference(length: float, width: float) -> float | None:
    """Retrieve the circumference of a specific square"""
    return service.get_circumference(length, width)

@router.post("/")
def create(square: Square) -> Square:
    """Create a new square"""
    return service.create(square)

@router.patch("/{index}")
def modify(index: int, square: Square) -> Square | None:
    """Modify a square at a given index"""
    return service.modify(index, square)

@router.put("/{index}")
def replace(index: int, square: Square) -> Square | None:
    """Replace a square at a given index"""
    return service.replace(index, square)

@router.delete("/{length}/{width}")
def delete(length: float, width: float) -> bool:
    """Delete a square by length and width"""
    return service.delete(length, width)