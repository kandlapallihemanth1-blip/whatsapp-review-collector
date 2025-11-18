from pydantic import BaseModel

class ReviewSchema(BaseModel):
    id: int
    contact_number: str
    user_name: str
    product_name: str
    product_review: str
    created_at: str

    class Config:
        orm_mode = True