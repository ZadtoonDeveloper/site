from pydantic import BaseModel

class Data(BaseModel):
    name: str
class Rectangle(BaseModel):
    a : int
    b : int
class Triangle_90(BaseModel):
    a : int
    b : int