from pydantic import BaseModel, ValidationInfo, field_validator
class User(BaseModel):
    id: int
    name: str
    age: int
    @field_validator('age')
    def validate_age(cls, v):
        if v < 18:
            aw