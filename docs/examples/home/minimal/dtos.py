from pydantic import BaseModel


# Response short data structure
class ShortData(BaseModel):
    pk: int = 1
    q: bool | None = None


# Response data structure
class Data(ShortData):
    nested: ShortData
