from sqlalchemy.orm import Session
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate, Category

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def create_category(self, category_create: CategoryCreate) -> Category:
        return self.repository.create(category_create)

    def get_category(self, category_id: int) -> Category:
        return self.repository.get(category_id)

    def get_all_categories(self, skip: int = 0, limit: int = 10) -> list[Category]:
        return self.repository.get_all(skip, limit)

    def update_category(self, category_id: int, category_update: CategoryUpdate) -> Category:
        db_category = self.repository.get(category_id)
        return self.repository.update(db_category, category_update)

    def delete_category(self, category_id: int) -> None:
        self.repository.delete(category_id)
