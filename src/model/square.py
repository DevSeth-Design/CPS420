from pydantic import BaseModel

class Square(BaseModel):
    Length: float
    Width: float


    def area(self) -> float:
        """Calculate and return the area of the square"""
        return self.Length * self.Width

    def circumference(self) -> float:
        """Calculate and return the circumference of the square"""
        return 2 * (self.Length + self.Width)