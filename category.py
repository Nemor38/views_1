from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryInDBBase(CategoryBase):
    id: int

    class Config:
        orm_mode = True

class Category(CategoryInDBBase):
    pass

class CategoryInDB(CategoryInDBBase):
    pass
