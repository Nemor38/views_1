from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, category_create: CategoryCreate) -> Category:
        db_category = Category(**category_create.dict())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def get(self, category_id: int) -> Category:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_all(self, skip: int = 0, limit: int = 10) -> list[Category]:
        return self.db.query(Category).offset(skip).limit(limit).all()

    def update(self, db_category: Category, category_update: CategoryUpdate) -> Category:
        for key, value in category_update.dict(exclude_unset=True).items():
            setattr(db_category, key, value)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def delete(self, category_id: int) -> None:
        db_category = self.db.query(Category).filter(Category.id == category_id).first()
        self.db.delete(db_category)
        self.db.commit()
