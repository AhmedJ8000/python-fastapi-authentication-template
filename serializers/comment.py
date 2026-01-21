from pydantic import BaseModel


class CommentSchema(BaseModel):
    id: int
    content: str

    class Config:
        from_attributes = True


class CommentCreateSchema(BaseModel):
    content: str

    class Config:
        from_attributes = True


class CommentUpdateSchema(BaseModel):
    content: str

    class Config:
        from_attributes = True
